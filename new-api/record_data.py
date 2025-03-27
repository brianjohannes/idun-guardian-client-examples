from idun_guardian_sdk import GuardianClient, GuardianBLE
from datetime import datetime, timezone, timedelta
import time

my_device_id = "E5-1E-FD-F5-15-26"
my_api_key = "idun_GAtJDPZJ1bbs47Mf4KEBA3-v35iudqE3NSGSLD3OE8zE8KN2CHcN809-"

ble = GuardianBLE()
api = GuardianClient(my_device_id, my_api_key)

recording_id = api.start_recording(None, filtered_stream=False, raw_stream=False)

ble.start_recording(api.callback)

start_time = datetime.now(timezone.utc)
while datetime.now(timezone.utc) - start_time < timedelta(minutes=30):
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break

ble.stop_recording()
api.stop_recording()