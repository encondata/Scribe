import serial
import time

# Replace with your actual device path:
BT_PORT = '/dev/tty.zebra_zq520_12'
#BT_PORT = '/dev/tty.ZD410_1'  
BAUDRATE = 9600  # or 115200 depending on your printer

# Sample ZPL to print “Hello, World!”
ZPL = """
^XA
            
            ^FX Set Label Size
            ^PW406^LL203
            
            ^FO10,10^A@N,35,,E:85620388.TTF^BCN,35,Y,N,N,A^A@N,35,,E:85620388.TTF^FD{row['asset id']}^FS

            ^FX Target Line
            ^FT10,110^A@N,35,,E:85620388.TTF^FDTarget:^FS
            ^FT145,110^A@N,35,^FD{row['asset track']}^FS
            ^FT320,110^A@N,35,^FDRU:^FS
            ^FT385,110^A@N,35,^FD{row['asset tpos']}^FS
                            
                            
            ^FX Solid Dividing Line
            ^FO10,120^GB590,5,3,B,8^FS
                            
            ^FX Server Information
            ^FT10,155^A@N,35,^FDName:^FS
            ^FT120,155^A@N,35,^FD{row['asset name']}^FS
            ^FT10,190^A@N,35,^FDSerial:^FS
            ^FT120,190^A@N,35,^FD{row['asset serial num']}^FS
            ^FT10,225^A@N,35,^FDModel:^FS
            ^FT120,225^A@N,35,^FD{row['asset model']}^FS
            ^FX Source Line
            ^FT10,280^A@N,35,^FDSource:^FS
            ^FT130,280^A@N,35,^FD{row['asset srack']}^FS
            ^FT320,280^A@N,35,^FDRU:^FS
            ^FT385,280^A@N,35,^FD{row['asset spos']}^FS
                            
            ^FX Draw QR Code and Move Info
            ^FT480,280^A0B,36,20^FD{row['source site']}^FS
            ^FT480,180^A0N,36,20^FD{row['move date']}^FS
            ^FT485,285^BY1,2.0,5^BQN,2,4,Q,7^FDM<{row['asset id']}^FS
            
            ^FX PQ is number of labels
            ^PQ8,0,1,Y
            ^XZ
"""

def send_zpl(port: str, baud: int, zpl_data: str):
    try:
        # open serial connection
        with serial.Serial(port, baud, timeout=1) as ser:
            # small delay to ensure link is up
            time.sleep(1)
            ser.write(zpl_data.encode('utf-8'))
            ser.flush()
            print("Sent ZPL to printer.")
    except serial.SerialException as e:
        print(f"Error opening or writing to serial port: {e}")

if __name__ == "__main__":
    send_zpl(BT_PORT, BAUDRATE, ZPL)
