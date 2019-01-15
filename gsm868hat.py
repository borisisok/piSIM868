import pwr
import conn
import logging
import time	
	
logging.basicConfig(level=logging.DEBUG)
	
def has_pwr():
	conn.open()

	if 'OK' in conn.response(conn.AT_HELLO):
		logging.debug("Modem says Hello") 
		return True
	return False


def power_on():
	if not has_pwr():
		logging.info("Switching modem on now") 
		pwr.toggle()
		time.sleep(2)
		if has_pwr():
			logging.info("Modem is ready now") 
		else:
			logging.warning("Modem is still not ready. Aborting") 
	else:
		logging.info("Modem is on") 

def power_off():
	if has_pwr():
		logging.info("Switching modem off") 
		pwr.toggle()
		time.sleep(2)
		if not has_pwr():
			logging.info("Modem is off now") 
		else:
			logging.warning("Modem is still active. Aborting") 

	else:
		logging.info("Modem is off") 


#power_on()
#time.sleep(15)
power_off()
