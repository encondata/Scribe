# zpl_templates.py
# Auto-generated ZPL templates for each combination of label_format and label_type.
# Fill in the triple-quoted strings with the appropriate ZPL for each case.

Vegas_Top = """
# TODO: ZPL template for Vegas Top
"""

Vegas_Rail = """
# TODO: ZPL template for Vegas Rail
"""

Vegas_Crate = """
# TODO: ZPL template for Vegas Crate
"""

Vegas_Front = """
# TODO: ZPL template for Vegas Front
"""

Vegas_All = """
# TODO: ZPL template for Vegas All
"""

Amsterdam_Top = """
    ^XA
    ^MMT
    ^PR2
    ^PW1200^LL600^LS0
    ^CWK,E:TT0003M_.TTF
    ^FO38,295^GB1120,5,5^FS
    ^LRY

    ^FO100,10^GB200,110,90^FS
    ^FT120,100^AKN,100,^FD{row['floor']}^FS
    ^FT375,100^AKN,100,^FD{row['room']}^FS

    ^FO580,10^GB250,110,90^FS
    ^FT620,100^AKN,100,^FD{row['asset track']}^FS
    ^FT950,100^AKN,100,^FD{row['asset tpos']}^FS

    ^FT38,173^AKN,42,^FDName:^FS
    ^FT185,173^AKN,35,^FD{row['asset name']}^FS
    ^FT38,270^AKN,42,^FDModel:^FS
    ^FT185,270^AKN,35,^FD{row['asset model']}^FS
    ^FT38,220^AKN,42,^FDSerial:^FS
    ^FT185,220^AKN,35,^FD{row['asset serial num']}^FS
    
    ^FT38,351^AKN,35,^FDFLOOR:^FS
    ^FT185,351^AKN,35,^FD{row['floor']}^FS
    ^FT627,351^AKN,35,^FDROOM:^FS
    ^FT759,351^AKN,35,^FD{row['room']}^FS
    ^FT38,420^AKN,35,^FDPOD:^FS
    ^FT185,420^AKN,35,^FD{row['pod']}^FS
    ^FT627,420^AKN,35,^FDROW:^FS
    ^FT759,420^AKN,35,^FD{row['row']}^FS
    ^FT38,489^AKN,35,^FDRACK:^FS
    ^FT185,489^AKN,35,^FD{row['asset track']}^FS
    ^FT627,489^AKN,35,^FDRU:^FS
    ^FT759,489^AKN,35,^FD{row['asset tpos']}^FS   
    ^FX Bottom Aeest Bar Code
    ^FO440,500^BY4^BC,50^FD{row['asset id']}^FS
    ^FX QR Code
    ^FT1000,300^BY2,2.0,65^BQN,2,7^FD<{row['asset id']}^FS
    ^FX Move ID
    ^FT1120,580^AKB,45,45^FD{row['source site']}^FS
    ^FT1160,580^AKB,45,45^FD{row['move date']}^FS
    ^PQ1,0,1,Y
    ^XZ
    """

Amsterdam_Rail = """
    
    """

Amsterdam_Crate = """
    
    """

Amsterdam_Front = """
# TODO: ZPL template for Amsterdam Front
"""

Amsterdam_All = """
    
    """

Bengaluru_Top = """
    ^XA
    ^MMT
    ^PR2
    ^PW1200^LL600^LS0
    ^CWK,E:TT0003M_.TTF
    ^FO38,295^GB1120,5,5^FS
    ^LRY
        
    ^FO300,10^GB300,110,90^FS
    ^FT400,100^AKN,100,^FD{row['asset track']}^FS
    ^FT800,100^AKN,100,^FD{row['asset tpos']}^FS
        
    ^FT38,173^AKN,42,^FDName:^FS
    ^FT246,173^AKN,35,^FD{row['asset name']}^FS
    ^FT38,270^AKN,42,^FDModel:^FS
    ^FT246,270^AKN,35,^FD{row['asset model']}^FS
    ^FT38,220^AKN,42,^FDSerial:^FS
    ^FT246,220^AKN,35,^FD{row['asset serial num']}^FS
    ^FT38,351^AKN,35,^FDNAP:^FS
    ^FT165,351^AKN,35,^FD{row['nap']}^FS
    ^FT627,351^AKN,35,^FDSEC:^FS
    ^FT739,351^AKN,35,^FD{row['sector']}^FS
    ^FT38,420^AKN,35,^FDPOD:^FS
    ^FT165,420^AKN,35,^FD{row['pod']}^FS
    ^FT627,420^AKN,35,^FDROW:^FS
    ^FT739,420^AKN,35,^FD{row['row']}^FS
    ^FT38,489^AKN,35,^FDRACK:^FS
    ^FT165,489^AKN,35,^FD{row['asset track']}^FS
    ^FT627,489^AKN,35,^FDRU:^FS
    ^FT739,489^AKN,35,^FD{row['asset tpos']}^FS
    ^FX Bottom Aeest Bar Code
    ^FO440,500^BY4^BC,50^FD{row['asset id']}^FS
    ^FX QR Code
    ^FT1000,300^BY2,2.0,65^BQN,2,7^FDM<{row['asset id']}^FS
    ^FX Move ID
    ^FT1120,580^AKB,45,45^FD{row['source site']}^FS
    ^FT1160,580^AKB,45,45^FD{row['move date']}^FS
    ^PQ1,0,1,Y
    ^XZ
    """

Bengaluru_Rail = """
    ^XA
    ^MMT
    ^PR2
    ^PW1200^LL600^LS0
    ^CWK,E:TT0003M_.TTF
    ^FO38,295^GB1120,5,5^FS
    ^LRY
        
    ^FO300,10^GB300,110,90^FS
    ^FT400,100^AKN,100,^FD{row['asset track']}^FS
    ^FT800,100^AKN,100,^FD{row['asset tpos']}^FS
        
    ^FT38,173^AKN,42,^FDName:^FS
    ^FT246,173^AKN,35,^FD{row['asset name']}^FS
    ^FT38,270^AKN,42,^FDModel:^FS
    ^FT246,270^AKN,35,^FD{row['asset model']}^FS
    ^FT38,220^AKN,42,^FDSerial:^FS
    ^FT246,220^AKN,35,^FD{row['asset serial num']}^FS
    ^FT38,351^AKN,35,^FDNAP:^FS
    ^FT165,351^AKN,35,^FD{row['nap']}^FS
    ^FT627,351^AKN,35,^FDSEC:^FS
    ^FT739,351^AKN,35,^FD{row['sector']}^FS
    ^FT38,420^AKN,35,^FDPOD:^FS
    ^FT165,420^AKN,35,^FD{row['pod']}^FS
    ^FT627,420^AKN,35,^FDROW:^FS
    ^FT739,420^AKN,35,^FD{row['row']}^FS
    ^FT38,489^AKN,35,^FDRACK:^FS
    ^FT165,489^AKN,35,^FD{row['asset track']}^FS
    ^FT627,489^AKN,35,^FDRU:^FS
    ^FT739,489^AKN,35,^FD{row['asset tpos']}^FS
    ^FX Bottom Aeest Bar Code
    ^FO440,500^BY4^BC,50^FD{row['asset id']}^FS
    ^FX QR Code
    ^FT1000,300^BY2,2.0,65^BQN,2,7^FDM<{row['asset id']}^FS
    ^FX Move ID
    ^FT1120,580^AKB,45,45^FD{row['source site']}^FS
    ^FT1160,580^AKB,45,45^FD{row['move date']}^FS
    ^PQ1,0,1,Y
    ^XZ
    """

Bengaluru_Crate = """
    ^XA
    ^MMT
    ^PR2
    ^PW1200^LL600^LS0
    ^CWK,E:TT0003M_.TTF
    ^FO38,295^GB1120,5,5^FS
    ^LRY
        
    ^FO300,10^GB300,110,90^FS
    ^FT400,100^AKN,100,^FD{row['asset track']}^FS
    ^FT800,100^AKN,100,^FD{row['asset tpos']}^FS
        
    ^FT38,173^AKN,42,^FDName:^FS
    ^FT246,173^AKN,35,^FD{row['asset name']}^FS
    ^FT38,270^AKN,42,^FDModel:^FS
    ^FT246,270^AKN,35,^FD{row['asset model']}^FS
    ^FT38,220^AKN,42,^FDSerial:^FS
    ^FT246,220^AKN,35,^FD{row['asset serial num']}^FS
    ^FT38,351^AKN,35,^FDNAP:^FS
    ^FT165,351^AKN,35,^FD{row['nap']}^FS
    ^FT627,351^AKN,35,^FDSEC:^FS
    ^FT739,351^AKN,35,^FD{row['sector']}^FS
    ^FT38,420^AKN,35,^FDPOD:^FS
    ^FT165,420^AKN,35,^FD{row['pod']}^FS
    ^FT627,420^AKN,35,^FDROW:^FS
    ^FT739,420^AKN,35,^FD{row['row']}^FS
    ^FT38,489^AKN,35,^FDRACK:^FS
    ^FT165,489^AKN,35,^FD{row['asset track']}^FS
    ^FT627,489^AKN,35,^FDRU:^FS
    ^FT739,489^AKN,35,^FD{row['asset tpos']}^FS
    ^FX Bottom Aeest Bar Code
    ^FO440,500^BY4^BC,50^FD{row['asset id']}^FS
    ^FX QR Code
    ^FT1000,300^BY2,2.0,65^BQN,2,7^FDM<{row['asset id']}^FS
    ^FX Move ID
    ^FT1120,580^AKB,45,45^FD{row['source site']}^FS
    ^FT1160,580^AKB,45,45^FD{row['move date']}^FS
    ^PQ1,0,1,Y
    ^XZ
    """

Bengaluru_Front = """
# TODO: ZPL template for Bengaluru Front
"""

Bengaluru_All = """
    ^XA
    ^MMT
    ^PR2
    ^PW1200^LL600^LS0
    ^CWK,E:TT0003M_.TTF
    ^FO38,295^GB1120,5,5^FS
    ^LRY
        
    ^FO300,10^GB300,110,90^FS
    ^FT400,100^AKN,100,^FD{row['asset track']}^FS
    ^FT800,100^AKN,100,^FD{row['asset tpos']}^FS
        
    ^FT38,173^AKN,42,^FDName:^FS
    ^FT246,173^AKN,35,^FD{row['asset name']}^FS
    ^FT38,270^AKN,42,^FDModel:^FS
    ^FT246,270^AKN,35,^FD{row['asset model']}^FS
    ^FT38,220^AKN,42,^FDSerial:^FS
    ^FT246,220^AKN,35,^FD{row['asset serial num']}^FS
    ^FT38,351^AKN,35,^FDNAP:^FS
    ^FT165,351^AKN,35,^FD{row['nap']}^FS
    ^FT627,351^AKN,35,^FDSEC:^FS
    ^FT739,351^AKN,35,^FD{row['sector']}^FS
    ^FT38,420^AKN,35,^FDPOD:^FS
    ^FT165,420^AKN,35,^FD{row['pod']}^FS
    ^FT627,420^AKN,35,^FDROW:^FS
    ^FT739,420^AKN,35,^FD{row['row']}^FS
    ^FT38,489^AKN,35,^FDRACK:^FS
    ^FT165,489^AKN,35,^FD{row['asset track']}^FS
    ^FT627,489^AKN,35,^FDRU:^FS
    ^FT739,489^AKN,35,^FD{row['asset tpos']}^FS
    ^FX Bottom Aeest Bar Code
    ^FO440,500^BY4^BC,50^FD{row['asset id']}^FS
    ^FX QR Code
    ^FT1000,300^BY2,2.0,65^BQN,2,7^FDM<{row['asset id']}^FS
    ^FX Move ID
    ^FT1120,580^AKB,45,45^FD{row['source site']}^FS
    ^FT1160,580^AKB,45,45^FD{row['move date']}^FS
    ^PQ1,0,1,Y
    ^XZ
    """

Ashburn_Top = """
    ^XA
    ^MMT
    ^PR2
    ^PW1200^LL600^LS0
    ^CWK,E:TT0003M_.TTF
    ^FO38,295^GB1120,5,5^FS
    ^LRY
        
    ^FO300,10^GB300,110,90^FS
    ^FT400,100^AKN,100,^FD{row['asset track']}^FS
    ^FT800,100^AKN,100,^FD{row['asset tpos']}^FS
        
    ^FT38,173^AKN,42,^FDName:^FS
    ^FT246,173^AKN,35,^FD{row['asset name']}^FS
    ^FT38,270^AKN,42,^FDModel:^FS
    ^FT246,270^AKN,35,^FD{row['asset model']}^FS
    ^FT38,220^AKN,42,^FDSerial:^FS
    ^FT246,220^AKN,35,^FD{row['asset serial num']}^FS
    ^FT38,351^AKN,35,^FDNAP:^FS
    ^FT165,351^AKN,35,^FD{row['nap']}^FS
    ^FT627,351^AKN,35,^FDSEC:^FS
    ^FT739,351^AKN,35,^FD{row['sector']}^FS
    ^FT38,420^AKN,35,^FDPOD:^FS
    ^FT165,420^AKN,35,^FD{row['pod']}^FS
    ^FT627,420^AKN,35,^FDROW:^FS
    ^FT739,420^AKN,35,^FD{row['row']}^FS
    ^FT38,489^AKN,35,^FDRACK:^FS
    ^FT165,489^AKN,35,^FD{row['asset track']}^FS
    ^FT627,489^AKN,35,^FDRU:^FS
    ^FT739,489^AKN,35,^FD{row['asset tpos']}^FS
    ^FX Bottom Aeest Bar Code
    ^FO440,500^BY4^BC,50^FD{row['asset id']}^FS
    ^FX QR Code
    ^FT1000,300^BY2,2.0,65^BQN,2,7^FDM<{row['asset id']}^FS
    ^FX Move ID
    ^FT1120,580^AKB,45,45^FD{row['source site']}^FS
    ^FT1160,580^AKB,45,45^FD{row['move date']}^FS
    ^PQ1,0,1,Y
    ^XZ
    """

Ashburn_Rail = """
    ^XA
    ^MMT
    ^PR2
    ^PW1200^LL600^LS0
    ^CWK,E:TT0003M_.TTF
    ^FO38,295^GB1120,5,5^FS
    ^LRY
        
    ^FO300,10^GB300,110,90^FS
    ^FT400,100^AKN,100,^FD{row['asset track']}^FS
    ^FT800,100^AKN,100,^FD{row['asset tpos']}^FS
        
    ^FT38,173^AKN,42,^FDName:^FS
    ^FT246,173^AKN,35,^FD{row['asset name']}^FS
    ^FT38,270^AKN,42,^FDModel:^FS
    ^FT246,270^AKN,35,^FD{row['asset model']}^FS
    ^FT38,220^AKN,42,^FDSerial:^FS
    ^FT246,220^AKN,35,^FD{row['asset serial num']}^FS
    ^FT38,351^AKN,35,^FDNAP:^FS
    ^FT165,351^AKN,35,^FD{row['nap']}^FS
    ^FT627,351^AKN,35,^FDSEC:^FS
    ^FT739,351^AKN,35,^FD{row['sector']}^FS
    ^FT38,420^AKN,35,^FDPOD:^FS
    ^FT165,420^AKN,35,^FD{row['pod']}^FS
    ^FT627,420^AKN,35,^FDROW:^FS
    ^FT739,420^AKN,35,^FD{row['row']}^FS
    ^FT38,489^AKN,35,^FDRACK:^FS
    ^FT165,489^AKN,35,^FD{row['asset track']}^FS
    ^FT627,489^AKN,35,^FDRU:^FS
    ^FT739,489^AKN,35,^FD{row['asset tpos']}^FS
    ^FX Bottom Aeest Bar Code
    ^FO440,500^BY4^BC,50^FD{row['asset id']}^FS
    ^FX QR Code
    ^FT1000,300^BY2,2.0,65^BQN,2,7^FDM<{row['asset id']}^FS
    ^FX Move ID
    ^FT1120,580^AKB,45,45^FD{row['source site']}^FS
    ^FT1160,580^AKB,45,45^FD{row['move date']}^FS
    ^PQ1,0,1,Y
    ^XZ
    """

Ashburn_Crate = """
    ^XA
    ^MMT
    ^PR2
    ^PW1200^LL600^LS0
    ^CWK,E:TT0003M_.TTF
    ^FO38,295^GB1120,5,5^FS
    ^LRY
        
    ^FO300,10^GB300,110,90^FS
    ^FT400,100^AKN,100,^FD{row['asset track']}^FS
    ^FT800,100^AKN,100,^FD{row['asset tpos']}^FS
        
    ^FT38,173^AKN,42,^FDName:^FS
    ^FT246,173^AKN,35,^FD{row['asset name']}^FS
    ^FT38,270^AKN,42,^FDModel:^FS
    ^FT246,270^AKN,35,^FD{row['asset model']}^FS
    ^FT38,220^AKN,42,^FDSerial:^FS
    ^FT246,220^AKN,35,^FD{row['asset serial num']}^FS
    ^FT38,351^AKN,35,^FDNAP:^FS
    ^FT165,351^AKN,35,^FD{row['nap']}^FS
    ^FT627,351^AKN,35,^FDSEC:^FS
    ^FT739,351^AKN,35,^FD{row['sector']}^FS
    ^FT38,420^AKN,35,^FDPOD:^FS
    ^FT165,420^AKN,35,^FD{row['pod']}^FS
    ^FT627,420^AKN,35,^FDROW:^FS
    ^FT739,420^AKN,35,^FD{row['row']}^FS
    ^FT38,489^AKN,35,^FDRACK:^FS
    ^FT165,489^AKN,35,^FD{row['asset track']}^FS
    ^FT627,489^AKN,35,^FDRU:^FS
    ^FT739,489^AKN,35,^FD{row['asset tpos']}^FS
    ^FX Bottom Aeest Bar Code
    ^FO440,500^BY4^BC,50^FD{row['asset id']}^FS
    ^FX QR Code
    ^FT1000,300^BY2,2.0,65^BQN,2,7^FDM<{row['asset id']}^FS
    ^FX Move ID
    ^FT1120,580^AKB,45,45^FD{row['source site']}^FS
    ^FT1160,580^AKB,45,45^FD{row['move date']}^FS
    ^PQ1,0,1,Y
    ^XZ
    """

Ashburn_Front = """
# TODO: ZPL template for Ashburn Front
"""

Ashburn_All = """
    ^XA
    ^MMT
    ^PR2
    ^PW1200^LL600^LS0
    ^CWK,E:TT0003M_.TTF
    ^FO38,295^GB1120,5,5^FS
    ^LRY
        
    ^FO300,10^GB300,110,90^FS
    ^FT400,100^AKN,100,^FD{row['asset track']}^FS
    ^FT800,100^AKN,100,^FD{row['asset tpos']}^FS
        
    ^FT38,173^AKN,42,^FDName:^FS
    ^FT246,173^AKN,35,^FD{row['asset name']}^FS
    ^FT38,270^AKN,42,^FDModel:^FS
    ^FT246,270^AKN,35,^FD{row['asset model']}^FS
    ^FT38,220^AKN,42,^FDSerial:^FS
    ^FT246,220^AKN,35,^FD{row['asset serial num']}^FS
    ^FT38,351^AKN,35,^FDNAP:^FS
    ^FT165,351^AKN,35,^FD{row['nap']}^FS
    ^FT627,351^AKN,35,^FDSEC:^FS
    ^FT739,351^AKN,35,^FD{row['sector']}^FS
    ^FT38,420^AKN,35,^FDPOD:^FS
    ^FT165,420^AKN,35,^FD{row['pod']}^FS
    ^FT627,420^AKN,35,^FDROW:^FS
    ^FT739,420^AKN,35,^FD{row['row']}^FS
    ^FT38,489^AKN,35,^FDRACK:^FS
    ^FT165,489^AKN,35,^FD{row['asset track']}^FS
    ^FT627,489^AKN,35,^FDRU:^FS
    ^FT739,489^AKN,35,^FD{row['asset tpos']}^FS
    ^FX Bottom Aeest Bar Code
    ^FO440,500^BY4^BC,50^FD{row['asset id']}^FS
    ^FX QR Code
    ^FT1000,300^BY2,2.0,65^BQN,2,7^FDM<{row['asset id']}^FS
    ^FX Move ID
    ^FT1120,580^AKB,45,45^FD{row['source site']}^FS
    ^FT1160,580^AKB,45,45^FD{row['move date']}^FS
    ^PQ1,0,1,Y
    ^XZ
    """

Tokyo_Top = """
# TODO: ZPL template for Tokyo Top
"""

Tokyo_Rail = """
# TODO: ZPL template for Tokyo Rail
"""

Tokyo_Crate = """
# TODO: ZPL template for Tokyo Crate
"""

Tokyo_Front = """
# TODO: ZPL template for Tokyo Front
"""

Tokyo_All = """
# TODO: ZPL template for Tokyo All
"""

Row_Rack_Top = """
# TODO: ZPL template for Row/Rack Top
"""

Row_Rack_Rail = """
# TODO: ZPL template for Row/Rack Rail
"""

Row_Rack_Crate = """
# TODO: ZPL template for Row/Rack Crate
"""

Row_Rack_Front = """
# TODO: ZPL template for Row/Rack Front
"""

Row_Rack_All = """
# TODO: ZPL template for Row/Rack All
"""

Custom_Top = """
# TODO: ZPL template for Custom Top
"""

Custom_Rail = """
# TODO: ZPL template for Custom Rail
"""

Custom_Crate = """
# TODO: ZPL template for Custom Crate
"""

Custom_Front = """
# TODO: ZPL template for Custom Front
"""

Custom_All = """
# TODO: ZPL template for Custom All
"""
