import serial
import time
import logging
import sim868.pwr

ser = serial.Serial()
ser.port = "/dev/ttyS0"
ser.baudrate = 115200
ser.timeout = 1

logging.basicConfig(level=logging.INFO)

def open():
    if not ser.is_open:
        ser.open()

def send(q):
    try:
        cmd = b'' + q
        logging.info("sending: '" + cmd + "'")
        ser.write(cmd + '\r')
        logging.debug("ask_modem: " + cmd)
        read = True
        outp = b''
        while read:
            rcv = ser.readline().decode().strip("\n").strip("\r")
            logging.debug("modem output: *" + rcv + "*")
            if rcv == '':
                logging.debug("ask_modem returned void" )
                read = False;
            elif rcv != cmd:
                outp += rcv + "\n"
        if len(outp) > 0:
                outp = outp[:-1]
        logging.debug("ask_modem return value: *" + outp + "*")
        return outp
    except:
        pass
    return None




