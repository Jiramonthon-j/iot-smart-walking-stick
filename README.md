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

<br>
<h3 align="center">Prototype</h3>
<br>
<p align="center">
<img width="400" height="533" alt="ไม้เท้าอัจฉริยะ" src="https://github.com/user-attachments/assets/d9d07ac7-2a84-4dcc-bb4c-c09ef29a93b0" />
<br>
  <sub><i>Fully Assembled IoT Smart Walking Stick Prototype</i></sub>
</p>
