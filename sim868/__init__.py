from at import AT
import sim868.pwr as pwd
import sim868.conn as conn
import sim868.util as util
import logging
import time	
	
logging.basicConfig(level=logging.DEBUG)

def power_on():
	conn.open()
	if not util.has_pwr():
		logging.info("Switching modem on now") 
		pwr.toggle()
		time.sleep(2)
		if util.has_pwr():
			logging.info("Modem is ready now") 
		else:
			logging.warning("Modem is still not ready. Aborting") 
	else:
		logging.info("Modem is on") 

def power_off():
	conn.open()
	if util.has_pwr():
		logging.info("Switching modem off") 
		pwr.toggle()
		time.sleep(2)
		if not util.has_pwr():
			logging.info("Modem is off now") 
		else:
			logging.warning("Modem is still active. Aborting") 

	else:
		logging.info("Modem is off") 


def hello():
	print "hello"


