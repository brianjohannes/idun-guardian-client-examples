import asyncio
from idun_guardian_client import GuardianClient


IMPEDANCE_DURATION = 50  # duration of impedance measurement in seconds
MAINS_FREQUENCY_60Hz = (
    True  # mains frequency in Hz (50 or 60), for Europe 50Hz, for US 60Hz
)

# Get device address
bci = GuardianClient()
bci.address = asyncio.run(bci.search_device())

# start a recording session
asyncio.run(
    bci.start_recording(
        recording_timer=IMPEDANCE_DURATION,
        mains_freq_60hz=MAINS_FREQUENCY_60Hz,
        impedance_measurement=True,
    )
)