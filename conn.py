import serial
import time
import logging
import pwr

# Enable Serial Communication
ser = serial.Serial()
ser.port = "/dev/ttyS0"
#ser.baudrate = 115200
ser.baudrate = 9600
ser.timeout = 1

AT_HELLO = b'AT'

logging.basicConfig(level=logging.INFO)

def open():
    if not ser.is_open:
        ser.open()

def response(q):
    try:
        cmd = b'' + q
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


def has_pwr():
    cmd = b'AT'
    if 'OK' in response(AT_HELLO):
        logging.debug("Modem says Hello") 
        return True
    return False


def test():
    open()
    if not has_pwr():
        logging.info("Switching modem on now") 
        pwr.toggle()
        time.sleep(2)
    if has_pwr():
        logging.info("Modem is ready now") 
    else:
        logging.warning("Modem is still not ready. Aborting") 

    time.sleep()
    logging.info("Modem is ready now") 
