import serial
import serial.tools
import serial.tools.list_ports
import time

OPEN_CMD = b'\xA0\x01\x01\xA2'
CLOSE_CMD = b'\xA0\x01\x00\xA1'


while True:
    comports = serial.tools.list_ports.comports()
    target_port = None

    for port in comports:
        if 'VID:PID=1A86:7523' in port.hwid:
            target_port = port
            
    if not target_port:
        continue
        
    try:
        print('Opening Port: {}'.format(target_port.name))
        ser = serial.Serial(target_port.name)        
        ser.write(OPEN_CMD)
        time.sleep(0.5)
        ser.write(CLOSE_CMD)
        time.sleep(0.5)
    except Exception as ex:
        print(ex)
    finally:
        target_port = None
        print('Closing Port')
        ser.close()



    
    
    
    
    
    