from at import AT
import pwr
import conn
import util
import logging
import time	
	
logging.basicConfig(level=logging.DEBUG)

def power_on():
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


# main
conn.open()
power_on()

print conn.send(AT.GET_COMPLETE_TA_CAPABILITIES_LIST)
print 
print conn.send(AT.GET_MANUFACTURER_IDENTIFICATION)
print 
print conn.send(AT.GET_TA_MODEL_IDENTIFICATION)
print 
print conn.send(AT.GET_TA_REVISION_IDENTIFICATION_OF_SOFTWARE_RELEASE)
print 
print conn.send(AT.GET_GLOBAL_OBJECT_IDENTIFICATION)
print 
print conn.send(AT.GET_TA_SERIAL_NUMBER_IDENTIFICATION)
print 

#power_on()
#time.sleep(15)
#power_off()
