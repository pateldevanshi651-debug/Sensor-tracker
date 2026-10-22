# log_sensor.py
import datetime

def log_sensor_reading():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Sensor Reading: {current_time}")

if __name__ == "__main__":
    log_sensor_reading()
