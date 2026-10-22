# log_sensor.py
import datetime

def log_sensor_reading():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sensor_readings = [
        f"Reading 1: {current_time}",
        f"Reading 2: {current_time}",
        # Add more readings as needed
    ]
    for reading in sensor_readings:
        print(reading)

if __name__ == "__main__":
    log_sensor_reading()
