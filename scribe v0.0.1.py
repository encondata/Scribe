import sys
import os
import csv
import platform
import subprocess
import re
import socket
from datetime import datetime
from zebra import Zebra

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout, QLabel,
    QTableWidget, QTableWidgetItem, QHeaderView,
    QPushButton, QFrame, QSizePolicy,
    QDialog, QFormLayout
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont

import zpl_templates  # our ZPL templates module

# Application version
app_version = 'v0.0.1'

# Dropdown options
label_type_options        = ['Top', 'Rail', 'Crate', 'Front', 'All']
label_format_options      = ['Vegas', 'Amsterdam', 'Bengaluru', 'Ashburn', 'Tokyo', 'Row / Rack', 'Custom']
num_to_print_options      = ['1', '2', '3', '0']
move_name_options         = ['Future Use', 'Future Use']
source_location_options   = ['Future Use', 'Future Use']
printer_selection_options = ['USB', 'Bluetooth', 'IP']

# Constants
COMBO_WIDTH      = 200
SCAN_LOG_FILE    = 'scan.log'
LOOKUP_LOG_FILE  = 'scan_lookup.log'
CURRENT_FT_FILE  = 'current_ft.csv'
SETTINGS_FILE    = 'settings.env'

def ping_host(host: str, timeout: int = 5):
    """Ping once and return (reachable, ping_ms)."""
    param = '-n' if platform.system().lower().startswith('win') else '-c'
    try:
        proc = subprocess.run(
            ['ping', param, '1', host],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            universal_newlines=True, timeout=timeout
        )
        if proc.returncode == 0:
            m = re.search(r'time[=<]\s*(\d+\.?\d*)\s*ms', proc.stdout)
            return True, float(m.group(1)) if m else None
        return False, None
    except Exception:
        return False, None

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setFixedSize(400, 500)

        layout = QVBoxLayout(self)
        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignLeft)
        form.setFormAlignment(Qt.AlignLeft)
        form.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)

        keys = [
            'MQTT_SERVER','MQTT_PORT','MQTT_USER','MQTT_PASS',
            'SQL_SERVER','SQL_PORT','SQL_USER','SQL_PASS',
            'INTERNET_TEST_ADDRESS','STATUS_CHECK_INTERVAL',
            'PRINTER_USB_NAME','PRINTER_BLUETOOTH_MAC','PRINTER_IP_ADDRESS'
        ]
        if not os.path.isfile(SETTINGS_FILE):
            with open(SETTINGS_FILE,'w') as f:
                for k in keys: f.write(f"{k}=\n")

        settings = {}
        with open(SETTINGS_FILE) as f:
            for line in f:
                if '=' in line:
                    k, v = line.strip().split('=',1)
                    settings[k] = v

        self.edits = {}
        for k in keys:
            edit = QLineEdit(settings.get(k,''))
            if k in ('MQTT_PASS','SQL_PASS'):
                edit.setEchoMode(QLineEdit.Password)
            edit.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
            form.addRow(f"{k.replace('_',' ').title()}:", edit)
            self.edits[k] = edit

        layout.addLayout(form)
        btns = QHBoxLayout()
        discard = QPushButton("Discard")
        discard.clicked.connect(self.reject)
        commit = QPushButton("Commit")
        commit.clicked.connect(self.commit)
        btns.addWidget(discard)
        btns.addWidget(commit)
        layout.addLayout(btns)

    def commit(self):
        with open(SETTINGS_FILE,'w') as f:
            for k, edit in self.edits.items():
                f.write(f"{k}={edit.text().strip()}\n")
        self.accept()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.load_settings()
        self.setWindowTitle(f"Scribe - Server Sherpa {app_version}")
        self.setFixedSize(1024, 600)

        # status flags
        self.status_internet = False
        self.internet_ping_ms = None
        self.status_mqtt = False
        self.status_sql = False
        self.status_printer = False
        self.labels_printed = 0

        central = QWidget()
        self.setCentralWidget(central)
        ml = QVBoxLayout(central)
        ml.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        ml.setContentsMargins(20,20,20,20)

        # scan entry
        self.scan_entry = QLineEdit()
        self.scan_entry.setPlaceholderText("Enter scan code here...")
        self.scan_entry.setFixedWidth(400)
        self.scan_entry.returnPressed.connect(self.record_scan)
        ml.addWidget(self.scan_entry, alignment=Qt.AlignHCenter)
        ml.addSpacing(20)

        # first dropdown row
        row1 = QHBoxLayout(); row1.setSpacing(40)
        for lbl_text, opts, attr in [
            ("Label Type", label_type_options, 'label_type'),
            ("Label Format", label_format_options, 'label_format'),
            ("Num to Print", num_to_print_options, 'num_to_print')
        ]:
            col = QVBoxLayout(); col.setSpacing(0)
            lbl = QLabel(lbl_text); lbl.setAlignment(Qt.AlignCenter)
            combo = QComboBox(); combo.addItems(opts); combo.setFixedWidth(COMBO_WIDTH)
            setattr(self, attr, combo)
            col.addWidget(lbl); col.addWidget(combo)
            row1.addLayout(col)
        ml.addLayout(row1)

        # second dropdown row
        row2 = QHBoxLayout(); row2.setSpacing(40)
        for lbl_text, opts, attr in [
            ("Move Name", move_name_options, 'move_name'),
            ("Scanning Location", source_location_options, 'source_location'),
            ("Printer Selection", printer_selection_options, 'printer_selection')
        ]:
            col = QVBoxLayout(); col.setSpacing(0)
            lbl = QLabel(lbl_text); lbl.setAlignment(Qt.AlignCenter)
            combo = QComboBox(); combo.addItems(opts); combo.setFixedWidth(COMBO_WIDTH)
            setattr(self, attr, combo)
            col.addWidget(lbl); col.addWidget(combo)
            row2.addLayout(col)
        ml.addLayout(row2)
        ml.addSpacing(20)

        # lookup log table
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(['Scan Entry','Match Found','Time'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setFixedWidth(COMBO_WIDTH*3 + 80)
        ml.addWidget(self.table, alignment=Qt.AlignHCenter)

        # buttons row1
        ml.addStretch()
        br1 = QHBoxLayout(); br1.setSpacing(40); br1.setAlignment(Qt.AlignHCenter)
        for txt, fn in [
            ("Download Current F-T", self.download_ft),
            ("Reset Log Files",       self.reset_logs),
            ("Rebuild Files",         self.rebuild_files)
        ]:
            btn = QPushButton(txt); btn.setFixedWidth(COMBO_WIDTH); btn.clicked.connect(fn)
            br1.addWidget(btn)
        ml.addLayout(br1)

        # buttons row2
        ml.addSpacing(5)
        br2 = QHBoxLayout(); br2.setSpacing(40); br2.setAlignment(Qt.AlignHCenter)
        for txt, fn in [
            ("Run Status Checks", self.status_checks),
            ("Self Test",         self.self_test),
            ("Settings",          self.open_settings)
        ]:
            btn = QPushButton(txt); btn.setFixedWidth(COMBO_WIDTH); btn.clicked.connect(fn)
            br2.addWidget(btn)
        ml.addLayout(br2)

        # status bar
        sf = QFrame(); sf.setFrameShape(QFrame.Box)
        sf.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sl = QHBoxLayout(sf); sl.setSpacing(20)
        self.lbl_internet = QLabel();   self.lbl_internet.setAlignment(Qt.AlignCenter); sl.addWidget(self.lbl_internet)
        self.lbl_mqtt     = QLabel('MQTT');    self.lbl_mqtt.setAlignment(Qt.AlignCenter);     sl.addWidget(self.lbl_mqtt)
        self.lbl_sql      = QLabel('SQL');     self.lbl_sql.setAlignment(Qt.AlignCenter);      sl.addWidget(self.lbl_sql)
        self.lbl_printer  = QLabel('Printer'); self.lbl_printer.setAlignment(Qt.AlignCenter);  sl.addWidget(self.lbl_printer)
        self.lbl_labels   = QLabel(f"Labels Printed: {self.labels_printed}"); self.lbl_labels.setAlignment(Qt.AlignCenter); sl.addWidget(self.lbl_labels)
        ml.addWidget(sf)

        # periodic status checks
        if self.status_check_interval > 0:
            t = QTimer(self); t.timeout.connect(self.status_checks); t.start(self.status_check_interval*1000)

        # initial load
        self.load_lookup_log()
        self.update_status_bar()

    def load_settings(self):
        self.mqtt_server=''; self.mqtt_port=0
        self.mqtt_user='';   self.mqtt_pass=''
        self.sql_server='';  self.sql_port=0
        self.sql_user='';    self.sql_pass=''
        self.internet_test_address=''
        self.status_check_interval=60
        self.printer_usb_name=''
        self.printer_bluetooth_mac=''
        self.printer_ip_address=''
        if os.path.isfile(SETTINGS_FILE):
            with open(SETTINGS_FILE) as f:
                for line in f:
                    k,v=line.strip().split('=',1)
                    if k=='MQTT_SERVER': self.mqtt_server=v
                    elif k=='MQTT_PORT': self.mqtt_port=int(v) if v.isdigit() else 0
                    elif k=='MQTT_USER': self.mqtt_user=v
                    elif k=='MQTT_PASS': self.mqtt_pass=v
                    elif k=='SQL_SERVER': self.sql_server=v
                    elif k=='SQL_PORT': self.sql_port=int(v) if v.isdigit() else 0
                    elif k=='SQL_USER': self.sql_user=v
                    elif k=='SQL_PASS': self.sql_pass=v
                    elif k=='INTERNET_TEST_ADDRESS': self.internet_test_address=v
                    elif k=='STATUS_CHECK_INTERVAL': self.status_check_interval=int(v) if v.isdigit() else 60
                    elif k=='PRINTER_USB_NAME': self.printer_usb_name=v
                    elif k=='PRINTER_BLUETOOTH_MAC': self.printer_bluetooth_mac=v
                    elif k=='PRINTER_IP_ADDRESS': self.printer_ip_address=v

    def status_checks(self):
        ok,ms = ping_host(self.internet_test_address)
        self.status_internet, self.internet_ping_ms = ok, ms
        try: s = socket.create_connection((self.mqtt_server, self.mqtt_port), timeout=5); s.close(); self.status_mqtt=True
        except: self.status_mqtt=False
        try: s = socket.create_connection((self.sql_server, self.sql_port), timeout=5); s.close(); self.status_sql=True
        except: self.status_sql=False
        self.update_status_bar()

    def update_status_bar(self):
        bg = 'green' if self.status_internet else 'red'
        pt = f"{self.internet_ping_ms:.0f} ms" if (self.status_internet and self.internet_ping_ms is not None) else 'N/A'
        self.lbl_internet.setText(f"Internet: {pt}")
        self.lbl_internet.setStyleSheet(f"background-color:{bg}; color:white; padding:2px;")
        self.lbl_mqtt.setStyleSheet(f"background-color:{'green' if self.status_mqtt else 'red'}; color:white; padding:2px;")
        self.lbl_sql.setStyleSheet(f"background-color:{'green' if self.status_sql else 'red'}; color:white; padding:2px;")
        self.lbl_printer.setStyleSheet(f"background-color:{'green' if self.status_printer else 'red'}; color:white; padding:2px;")
        self.lbl_labels.setText(f"Labels Printed: {self.labels_printed}")
        self.lbl_labels.setStyleSheet("background-color:green; color:white; padding:2px;")

    def record_scan(self):
        text = self.scan_entry.text().strip()
        if not text:
            return

        # log scan
        row_log = [
            text,
            self.label_type.currentText(),
            self.label_format.currentText(),
            self.num_to_print.currentText(),
            self.move_name.currentText(),
            self.source_location.currentText(),
            self.printer_selection.currentText(),
            datetime.now().isoformat()
        ]
        newf = not os.path.isfile(SCAN_LOG_FILE)
        with open(SCAN_LOG_FILE,'a',newline='') as f:
            w = csv.writer(f)
            if newf:
                w.writerow(['scan_code','label_type','label_format','num_to_print','move_name','source_location','printer_selection','timestamp'])
            w.writerow(row_log)

        # lookup
        if text.isdigit() and len(text) in (5,6):
            ltype, field = "Asset ID", "asset id"
        else:
            ltype, field = "Serial", "asset serial num"

        found = False
        lookup_row = None
        if os.path.isfile(CURRENT_FT_FILE):
            with open(CURRENT_FT_FILE,newline='') as f:
                dr = csv.DictReader(f)
                for r in dr:
                    if r.get(field,'').strip() == text:
                        found, lookup_row = True, r
                        break

        if not found:
            QApplication.beep()
            self.show_no_match_popup()
            ltype = "Not Found"
        else:
            QApplication.beep()
            self.generate_zpl_and_print(lookup_row)

        # log lookup
        ts = datetime.now().isoformat()
        newl = not os.path.isfile(LOOKUP_LOG_FILE)
        with open(LOOKUP_LOG_FILE,'a',newline='') as f:
            w = csv.writer(f)
            if newl:
                w.writerow(['scan_code','match_type','lookup_timestamp'])
            w.writerow([text, ltype, ts])

        self.load_lookup_log()
        self.scan_entry.clear()
        self.scan_entry.setFocus()

    def show_no_match_popup(self):
        dlg = QDialog(self)
        dlg.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        dlg.setStyleSheet("background-color:red;")

        lbl = QLabel("No Match Found", dlg)
        lbl.setStyleSheet("color:white;")
        font = QFont()
        font.setPointSize(48)  # larger text
        font.setBold(True)     # bold text
        lbl.setFont(font)
        lbl.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout(dlg)
        layout.addWidget(lbl)

        # Set popup size to 640x480
        dlg.setFixedSize(640, 480)
        dlg.show()
        QTimer.singleShot(2000, dlg.close)

    def generate_zpl_and_print(self, row):
        count = int(self.num_to_print.currentText())
        fmt_key = re.sub(r'\W+', '_', self.label_format.currentText())
        typ_key = re.sub(r'\W+', '_', self.label_type.currentText())
        tpl = getattr(zpl_templates, f"{fmt_key}_{typ_key}", None)
        if not tpl:
            print(f"Template '{fmt_key}_{typ_key}' not found.")
            return

        zpl_data = re.sub(
            r"\{row\['([^']+)'\]\}",
            lambda m: str(row.get(m.group(1), '')),
            tpl
        )

        if '^XZ' in zpl_data:
            zpl_data = zpl_data.replace('^XZ', f'^PQ{count}^XZ', 1)
        else:
            zpl_data += f'\n^PQ{count}^XZ'

        sel = self.printer_selection.currentText()
        try:
            if sel == 'USB':
                print(self.printer_usb_name)
                z = Zebra(self.printer_usb_name)
                z.output(zpl_data)
            elif sel == 'Bluetooth':
                z = Zebra(self.printer_usb_name)
                z.output(zpl_data)
            else:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5)
                s.connect((self.printer_ip_address, 9100))
                s.sendall(zpl_data.encode())
                s.close()
            self.status_printer = True
            self.labels_printed += count
        except Exception as e:
            print(f"Printing error: {e}")
            self.status_printer = False

        self.update_status_bar()

    def reset_logs(self):
        with open(SCAN_LOG_FILE, 'w', newline='') as f:
            csv.writer(f).writerow(['scan_code','label_type','label_format','num_to_print','move_name','source_location','printer_selection','timestamp'])
        with open(LOOKUP_LOG_FILE, 'w', newline='') as f:
            csv.writer(f).writerow(['scan_code','match_type','lookup_timestamp'])
        self.load_lookup_log()

    def load_lookup_log(self):
        entries = []
        if os.path.isfile(LOOKUP_LOG_FILE):
            with open(LOOKUP_LOG_FILE,newline='') as f:
                r = csv.reader(f); next(r,None)
                for row in r:
                    if len(row) >= 3:
                        entries.append((row[0], row[1], row[2]))
        latest = list(reversed(entries))[:10]
        self.table.setRowCount(len(latest))
        for i, (sc, mt, ts) in enumerate(latest):
            self.table.setItem(i, 0, QTableWidgetItem(sc))
            self.table.setItem(i, 1, QTableWidgetItem(mt))
            self.table.setItem(i, 2, QTableWidgetItem(ts))
        if latest:
            self.table.scrollToItem(self.table.item(0, 0), QTableWidget.PositionAtTop)

    # stub methods
    def download_ft(self):   print("Downloading current F-T...")
    def rebuild_files(self): print("Rebuilding files...")
    def self_test(self):     print("Running self test...")

    def open_settings(self):
        dlg = SettingsDialog(self)
        if dlg.exec() == QDialog.Accepted:
            os.execv(sys.executable, [sys.executable] + sys.argv)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
