# 🛠️ ShelBot Lite

**Your free, fully local, open-source ShelBot that runs on almost any computer.**

Built by **Ryan** from [Sheltech LLC](https://sheltechllc.com) — the lightweight and accessible version of ShelBotX.

![ShelBot Lite running](Shelbot-lite%20convo.png)

---

## ✨ What is ShelBot Lite?

ShelBot Lite is a **100% private local AI** you can run offline on your own PC. No subscriptions, no data leaving your machine.

It carries the same helpful, witty, engineering-focused personality as the full ShelBotX — just optimized to run on modest hardware.

---

## 🎯 Features

- **Completely Local** — Works offline after initial model download
- **Persistent Memory** — Remembers your conversation across the session
- **Simple & Reliable** — Console-based (no complicated UI)
- **One-click setup** on Windows
- **Easy to customize** (change model or personality)
- **Free forever** — Open source

---

## ⚙️ System Requirements

| Component     | Minimum              | Recommended         |
|---------------|----------------------|---------------------|
| RAM           | 8 GB                 | 16 GB+              |
| Storage       | ~5 GB (for model)    | 10 GB               |
| Processor     | Modern 4-core CPU    | Any recent CPU/GPU  |
| OS            | Windows (primary)    | Linux/macOS possible|

**Runs great on normal laptops and older desktops.**

---

## 🚀 Quick Start

1. **Install Ollama**  
   Download from [ollama.com](https://ollama.com)

2. **Download ShelBot Lite**  
   Click **Code → Download ZIP** on this page

3. **Setup**  
   Extract the zip → Double-click `setup.bat`

4. **Download the AI Model** (first time only)
   ```powershell
   ollama pull llama3.2:3b

Launch
Double-click run.bat and start chatting!


📋 What ShelBot Lite Can Do

Rockets, drones, 3D printing, PID tuning, electronics, Arduino, Python, etc.
Brainstorm experimental ideas and project planning
Troubleshoot technical problems
General knowledge with a fun, slightly sarcastic engineer vibe

Best for: Makers, students, hobbyists, and garage engineers.

❌ Limitations

Uses a small 3B model → Good but not as intelligent as the full 70B ShelBotX
Console interface only (keeps it lightweight)
No internet tools or web browsing
Memory is saved locally but resets if you delete memory.json
May hallucinate on very advanced topics

This is the free community edition — designed for accessibility.

⬆️ Upgrade Options
Want more power? Check out:

ShelBot_Quan — Quantized higher-performance version
Full ShelBotX — Maximum intelligence + advanced features
EdgeAuton Core — Specialized for drones & rockets

Available on Gumroad or message Ryan directly.

🛠️ Customization

Edit the Modelfile to change personality
Change the model in shelbot.py (try llama3:8b, qwen2.5:7b, etc.)


📁 Folder Structure
textShelBot-Lite/
├── setup.bat
├── run.bat
├── shelbot.py
├── Modelfile
├── requirements.txt
├── README.md
├── LICENSE
└── memory.json          ← Created automatically

🤝 Contributing & Feedback
Feel free to open issues or pull requests!
Suggestions for colors, Linux support, or personality tweaks are welcome.

📜 License
MIT License

❤️ Made by
Ryan Shelton — Sheltech LLC
From 3D printed rockets to local AI — because cool tools should be for everyone.
X: @Ryan_shelton91
