# IoT Smart Walking Stick 

An IoT-enabled assistive smart walking stick designed for the visually impaired and elderly, powered by MicroPython and ESP32.

## Key Features
- **Obstacle Detection:** Utilizes HC-SR04 Ultrasonic Sensor to detect objects within 30cm and triggers an audible buzzer alarm.
- **Fall Detection:** Uses MPU6050 6-axis Gyroscope & Accelerometer to detect sudden trips or falls.
- **Emergency Telegram Alert:** Automatically connects to Wi-Fi and sends instant SOS location/alerts to family via Telegram Bot API when a fall is detected.

## Hardware & Tech Stack
- **Microcontroller:** ESP32 / ESP8266 (MicroPython)
- **Sensors:** HC-SR04 Ultrasonic, MPU6050 Gyro/Accelerometer
- **Actuator:** Passive Buzzer
- **Integrations:** Telegram Bot API (`urequests`), Wi-Fi Auto-connect
