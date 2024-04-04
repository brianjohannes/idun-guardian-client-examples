from idun_guardian_sdk import GuardianAPI, GuardianBLE
from datetime import datetime, timezone, timedelta
import time
from pylsl import StreamInfo, StreamOutlet


my_device_id = "E5-1E-FD-F5-15-26"
my_api_key = "idun_GAtJDPZJ1bbs47Mf4KEBA3-v35iudqE3NSGSLD3OE8zE8KN2CHcN809-"

ble = GuardianBLE()
api = GuardianAPI(my_device_id, my_api_key)

info = StreamInfo('IDUN', 'EEG', 1, 250, 'float32', ble.device_id)
lsl_outlet = StreamOutlet(info, 20, 360)


# recording_id = api.start_recording(lambda data: lsl_outlet.push_chunk(data['raw_eeg']['ch1'], data['raw_eeg']['timestamp'][-1]), filtered_stream=False, raw_stream=True)
recording_id = api.start_recording(lambda data: lsl_outlet.push_chunk(data['raw_eeg']['ch1']), filtered_stream=False, raw_stream=True)
# recording_id = api.start_recording(lambda data: lsl_outlet.push_sample(data['raw_eeg']['ch1']), filtered_stream=False, raw_stream=True)


ble.start_recording(api.callback)

start_time = datetime.now()
while datetime.now() - start_time < timedelta(minutes=30):
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break

ble.stop_recording()
api.stop_recording()