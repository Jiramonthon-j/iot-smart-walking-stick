#  IoT Smart Walking Stick

![MicroPython](https://img.shields.io/badge/Language-MicroPython-3776AB?style=flat-square&logo=python&logoColor=white)
![ESP32](https://img.shields.io/badge/Hardware-ESP32-E7352C?style=flat-square&logo=espressif&logoColor=white)
![Telegram](https://img.shields.io/badge/Integration-Telegram%20Bot%20API-26A5E4?style=flat-square&logo=telegram&logoColor=white)
![Focus](https://img.shields.io/badge/Domain-IoT%20%26%20Assistive%20Tech-00C853?style=flat-square)

An IoT-enabled assistive smart walking stick designed for the visually impaired and elderly, powered by MicroPython and ESP32.

---

## 📌 Key Features

- **Obstacle Detection:** Utilizes HC-SR04 Ultrasonic Sensor to detect objects within 30cm and triggers an audible buzzer alarm.
- **Fall Detection:** Uses MPU6050 6-axis Gyroscope & Accelerometer to detect sudden trips or falls.
- **Emergency Telegram Alert:** Automatically connects to Wi-Fi and sends an instant fall alert to family via the Telegram Bot API when a fall is detected.

---

## 🛠️ Hardware & Tech Stack

| Component Type | Hardware / Library | Purpose & Role |
| :--- | :--- | :--- |
| **Microcontroller** | ESP32 | Core processing unit running MicroPython firmware |
| **Sensors** | HC-SR04 Ultrasonic | Real-time distance measuring for obstacle avoidance |
| **Sensors** | MPU6050 Gyro/Accelerometer | 6-axis motion tracking for sudden fall detection |
| **Actuator** | Passive Buzzer | Instant audio alert notification for the user |
| **Integrations** | Telegram Bot API (`urequests`) | Emergency Wi-Fi alert system for caregivers |

---

## ⚙️ Setup

1. Flash MicroPython to the ESP32 and upload the `sonic` (HC-SR04) and `MPU6050` driver libraries.
2. Copy `config.example.py` to `config.py` and fill in your WiFi networks and Telegram bot token / chat ID.
   `config.py` is git-ignored, so credentials never end up in the repository.
3. Upload `config.py` and `main.py` to the board. `main.py` runs automatically on boot.

---

### Pins and thresholds (as set in `main.py`)

| Item | Value |
| :--- | :--- |
| HC-SR04 trigger / echo | GPIO 5 / GPIO 18 |
| Buzzer | GPIO 2 |
| Obstacle distance | alarm at 30 cm or closer |
| Fall detection | gyro on any axis > 60 **and** acceleration on any axis > 7 |

---

## 📸 Prototype Overview

<p align="center">
  <img width="400" height="533" alt="ไม้เท้าอัจฉริยะ" src="https://github.com/user-attachments/assets/d9d07ac7-2a84-4dcc-bb4c-c09ef29a93b0" />
  <br/>
  <sub><i>Fully Assembled IoT Smart Walking Stick Prototype</i></sub>
</p>
