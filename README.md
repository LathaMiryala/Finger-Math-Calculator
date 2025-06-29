# 🖐️ Finger Math Addition using Webcam

This Python project uses **OpenCV** and **MediaPipe** to detect fingers via a webcam and performs **real-time finger addition**. It captures hand landmarks, counts extended fingers on both hands, and displays their sum as a simple math addition on the screen.

## 🔧 Technologies Used

- **Python 3.x**
- **OpenCV**
- **MediaPipe**

## ✨ Features

- Real-time finger tracking from webcam
- Automatic hand detection (Left or Right)
- Thumb detection logic adapted for left/right hands
- Displays individual finger counts and their sum

## 🧠 How It Works

1. Uses **MediaPipe Hands** to detect 21 hand landmarks.
2. Detects whether the hand is left or right.
3. Counts the number of raised fingers based on relative landmark positions.
4. Displays finger count and their addition live on the screen.

