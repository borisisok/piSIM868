import sim868
import sim868.conn as conn
from sim868.at import AT
import time

sim868.power_on()

print conn.send(AT.GET_COMPLETE_TA_CAPABILITIES_LIST)
time.sleep(2)
print conn.send(AT.GET_MANUFACTURER_IDENTIFICATION)
time.sleep(2)
print conn.send(AT.GET_TA_MODEL_IDENTIFICATION)
time.sleep(2)
print conn.send(AT.GET_TA_REVISION_IDENTIFICATION_OF_SOFTWARE_RELEASE)
time.sleep(2)
print conn.send(AT.GET_GLOBAL_OBJECT_IDENTIFICATION)
time.sleep(2)
print conn.send(AT.GET_TA_SERIAL_NUMBER_IDENTIFICATION)
time.sleep(2)

print conn.send(AT.GET_CURRENT_CALLS_OF_ME)
time.sleep(2)
print conn.send(AT.GET_CURRENT_CONFIGURATION)
time.sleep(2)
print conn.send(AT.GET_INTERNATIONAL_MOBILE_SUBSCRIBER_IDENTITY)
time.sleep(2)
print conn.send(AT.GET_LOCAL_TIME)
time.sleep(2)
print conn.send(AT.GET_MODEL_IDENTIFICATION)
time.sleep(2)
print conn.send(AT.GET_OPERATOR_SELECTION)
time.sleep(2)
print conn.send(AT.GET_JAMMING_DETECTION)
print conn.send(AT.GET_PHONE_ACIVIY_STATUS)
print conn.send('AT+CENG=4,1')
time.sleep(3)
print conn.send('AT+CENG?')
print conn.send('AT+CENG=0,0')
sim868.power_off()

