from idun_guardian_sdk import GuardianBLE

ble = GuardianBLE()

print(f"Battery: {ble.get_battery()}%")