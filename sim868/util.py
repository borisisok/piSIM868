from sim868.at import AT
import sim868.conn as conn
import logging

logging.basicConfig(level=logging.DEBUG)

def has_pwr():
    cmd = b'AT'
    if 'OK' in conn.send(AT.GET_OK):
        logging.debug("Modem says Hello") 
        return True
    return False
