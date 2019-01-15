import sim868
import sim868.conn as conn
from sim868.at import AT

sim868.power_on()

print conn.send(AT.GET_COMPLETE_TA_CAPABILITIES_LIST)
print conn.send(AT.GET_MANUFACTURER_IDENTIFICATION)
print conn.send(AT.GET_TA_MODEL_IDENTIFICATION)
print conn.send(AT.GET_TA_REVISION_IDENTIFICATION_OF_SOFTWARE_RELEASE)
print conn.send(AT.GET_GLOBAL_OBJECT_IDENTIFICATION)
print conn.send(AT.GET_TA_SERIAL_NUMBER_IDENTIFICATION)

sim868.power_off()

