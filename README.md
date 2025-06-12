# Hands-off-Nose
This is my Code in Place 2025 project — a real-time Python system that detects when a hand comes close to the nose using MediaPipe Face Mesh and Hands, triggering an audio alert. I built it after my own septorhinoplasty to help prevent accidental nose touching during recovery. Useful for facial surgery patients or habit-tracking tools.

# 👃 Nose Touch Detection using MediaPipe & OpenCV

This project is my submission for **Code in Place 2025**, developed as a personal solution and a prototype for healthcare-focused AI applications.

## 🩺 Motivation

After undergoing **septorhinoplasty**, I experienced a strong urge to touch or scratch my nose — an action strongly discouraged during recovery. I even hit my nose once while asleep. This inspired me to build a system that **detects hand-to-nose proximity** and triggers an **audio alert**, helping patients avoid unconscious or accidental nose contact.

### 🎯 Broader Goal

This project is a starting point in my long-term vision to **use AI for healthcare**, especially in **patient recovery, behavior tracking, and safety reinforcement**. It represents a meaningful intersection of **Computer Vision and medical needs**, areas I aim to explore deeper through formal study.

I plan to continue evolving this into a more advanced model, integrating it with edge devices (e.g., Arduino + camera) for real-world use.

---

## 🧠 How It Works

This system uses:

- **MediaPipe FaceMesh** – to track the tip of the nose.
- **MediaPipe Hands** – to detect hand landmarks.
- **OpenCV** – for real-time video processing.
- **Pygame** – to play an alarm sound when a hand approaches the nose.

If any point of the hand comes within a set threshold distance from the nose tip, the system triggers a continuous **beep sound** until the hand moves away.

---

## 🎥 Demo

[![Watch the demo]([https://youtu.be/YOUR_VIDEO_ID_HERE](https://youtu.be/-RIvnhOtZEs))


---

## 💻 Requirements

- Python 3.8+
- `opencv-python`
- `mediapipe`
- `pygame`
- A working webcam

Install dependencies:

```bash
pip install opencv-python mediapipe pygame
```

---

## ▶️ How to Run

1. Place an alert sound file at `audio/beep-06.wav` (or change the path in the script).
2. Run the Python file:

   ```bash
   python nose_touch_detector.py
   ```

3. Press `q` to quit.

---

## 🧪 Use Cases & Future Plans

- Facial surgery recovery aid  
- Behavioral correction (e.g., nose picking, face touching)  
- Habit tracking via AI  
- Integration with microcontrollers like **Arduino** for portable alerts  
- Potential to train a model with MediaPipe's landmarks data and use it for gesture-based control or pose classification

---

## 🙏 Acknowledgments

Thanks to:

- **Chris Piech**, **Mehran Sahami**, and the entire **Code in Place 2025** community for the opportunity and support  
- **MediaPipe** and **OpenCV** for powerful open-source tools

---

## 🎓 Admissions Context

I built this to demonstrate my passion for **AI and healthcare**, an area I intend to pursue at institutions like **MBZUAI** and **Aga Khan University (AKU)**. It reflects:

- Creativity in real-world problem solving  
- Technical foundation in Python and CV libraries  
- A practical understanding of how AI can impact **medical recovery** and **patient safety**

This is just the beginning of my applied AI journey.
