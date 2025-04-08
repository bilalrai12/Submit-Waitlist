# 🚀 CodeX-Waitlist Script

**CodeX-Waitlist** automation script!  
This script automatically registers a list of emails to the [CodeX waitlist](https://www.codex.xyz) using proxies and multi-threading.  

---

## 🌟 Features

- 🧵 **Multi-threaded** processing for fast execution
- 🛡️ **Rotating proxies** to avoid IP bans
- 🎲 **Random names** for each submission
- 🕵️‍♂️ Tracks IP addresses for transparency
- 🔁 Automatic retry logic up to 5 times per account

---

## 📦 Clone the Repository

```bash
git clone https://github.com/bilalrai12/Submit-Waitlist.git
cd Submit-Waitlist
```

---

## ⚙️ Prerequisites

Make sure you have **Python 3.8+** installed.  
Install required dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Setup Guide

### 📂 Required Files

- `accounts.txt`: Your email list in the format: `email|password`
- `proxies.txt`: Proxy list in the format: `http://user:pass@ip:port`
- `main.py`: Main automation script
- `requirements.txt`: Python packages needed

---

### ⚙️ Adjust Number of Threads

Inside `main.py`, locate line **14**:

```python
threads = 10  # Config threads
```

You can increase or decrease this number depending on your system capability and proxy quality. 

📌 **Tip:** Too many threads with poor proxies can cause failures. Start with 10–20 and scale from there.

---

## 💻 How to Run the Script

### 🐧 Linux / 🍎 macOS

```bash
python3 main.py
```

✔ Output will include timestamps, IP info, and status for each submission.

---

### 🪟 Windows

```bash
python main.py
```

📌 Make sure you're in the same directory as `main.py` and all config files.

---

## 🧪 Example `accounts.txt`

```
email1@example.com|password123
email2@example.com|securepass456
```

## 🌐 Example `proxies.txt`

```
http://user:pass@123.45.67.89:8080
http://user:pass@98.76.54.32:3128
```

---

## 📢 Notes

- Avoid using public proxies for better success rate.
- Set `threads` value inside `main.py` to control concurrency (default is 10).
- Keep your files clean and properly formatted to avoid errors.

---

## 🙋‍♂️ Community & Support

Join the team or get help here:

- 💬 [Telegram](https://t.me/Bilalstudio2)  

> Made with ❤️ by Bilal Studio 

