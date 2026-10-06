"""IoT Smart Walking Stick (MicroPython, ESP32)

- HC-SR04 ultrasonic sensor: buzzer alarm when an obstacle is within 30 cm
- MPU6050 gyro + accelerometer: detects a fall and sends a Telegram alert

Upload this file to the board as main.py so it runs on boot.
"""

# Libraries
from sonic import HCSR04
from MPU6050 import MPU6050
from machine import Pin
from time import sleep
import time
import network
import urequests

# Secrets live in config.py (not committed). Copy config.example.py -> config.py and fill in your values.
from config import WIFI_NETWORKS, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

# Initialize Ultrasensor
sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)
threshold_ultrasonic = 30

# Initialize Gyro (MPU6050)
mpu = MPU6050()
threshold_gyro_acc = 7
threshold_gyro_axis = 60

# Initialize Buzzer
buzzer = Pin(2, Pin.OUT)

# Return distance in cm
def read_ultrasonic():
    distance = sensor.distance_cm()
    return distance

# Function to read gyro axis
def read_axis():
    readgyro = mpu.read_gyro_data()
    read_x = readgyro["x"]
    read_y = readgyro["y"]
    read_z = readgyro["z"]
    return abs(read_x), abs(read_y), abs(read_z)

# Function to read gyro acc
def read_acc():
    readacc = mpu.read_accel_data()
    readacc_x = readacc["x"]
    readacc_y = readacc["y"]
    readacc_z = readacc["z"]
    return abs(readacc_x), abs(readacc_y), abs(readacc_z)

# Connect Wifi (tries each network in config.WIFI_NETWORKS in order)
def connect_wifi(timeout_s=10):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    for ssid, password in WIFI_NETWORKS:
        print('Connecting to WiFi:', ssid)
        wlan.connect(ssid, password)
        for _ in range(timeout_s):
            if wlan.isconnected():
                print('Connected to WiFi:', wlan.ifconfig())
                return wlan
            time.sleep(1)
        wlan.disconnect()
    raise RuntimeError('Could not connect to any configured WiFi network')

# send the message to telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        response = urequests.post(url, json=data)
        print("Message sent:", response.text)
        response.close()
        sleep(5)
    except Exception as e:
        print("Failed to send message:", e)
     
# Buzzer sound on
def buzz():
    buzzer.on()
    sleep(1)
    buzzer.off()
        
if __name__ == "__main__":
    # Connect to Wi-Fi
    try:
        connect_wifi()
    except Exception as e:
        print("WiFi connection failed:", e)

    # Main loop
    while True:
        distance = read_ultrasonic()
        x_axis, y_axis, z_axis = read_axis()
        x_acc, y_acc, z_acc = read_acc()

        # Ultrasonic condition
        if distance <= threshold_ultrasonic:
            buzz()

        # Gyro and acceleration conditions
        if (
            (x_axis > threshold_gyro_axis or y_axis > threshold_gyro_axis or z_axis > threshold_gyro_axis) and
            (x_acc > threshold_gyro_acc or y_acc > threshold_gyro_acc or z_acc > threshold_gyro_acc)
        ):
            send_telegram_message("Fall detected! The user may need help.")
            buzz()