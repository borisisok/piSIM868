from at import AT
import conn
import logging

logging.basicConfig(level=logging.DEBUG)

def has_pwr():
    cmd = b'AT'
    if 'OK' in conn.send(AT.GET_OK):
        logging.debug("Modem says Hello") 
        return True
    return False
