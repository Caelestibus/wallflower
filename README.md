## 🌸 Wallflower - Python Reverse Shell C2

**Wallflower🌸🌸** is a lightweight Command & Control (C2) framework written in Python. It shows how attackers gain access to victims system in real time.

This project was built for educational purposes as part of my red team learning journey.

---

### 💡 What It Does

- ✅ Opens a reverse shell from a "victim" to an "attacker"
- ✅ Executes shell commands remotely (e.g. `whoami`, `ls`)
- ✅ Built using simple Python sockets
- ✅ Set up using Vagrant with two virtual machines

---

### 🧱 How It Works

- The **attacker** runs `server.py`, which waits for incoming connections.
- The **victim** runs `client.py`, which connects back to the attacker.
- The attacker sends commands, and the victim machine runs them and returns the results.

```
┌──────────────┐             ┌──────────────┐
│ Attacker VM  │ ←────────→ │  Victim VM   │
│ 192.168.56.10│             │192.168.56.20 │
│  server.py   │ :4444       │  client.py   │
└──────────────┘             └──────────────┘
```


---

### 🛠 Requirements

- Python 3
- Vagrant
- VirtualBox

---

### ⚙️ Setup Instructions

1. **Clone this repository**:
   ```bash
   git clone https://github.com/Caelestibus/wallflower.git
   cd wallflower

---

2. Start the virtual lab:

   ```bash
   vagrant up
   ```
   SSH into the VMs:

   ```bash
   vagrant ssh attacker
   vagrant ssh victim
   ```

---

3. Run the Python scripts:

   On the attacker VM:

   ```bash
   python3 server.py
   ```

   On the victim VM:

   ```bash
   python3 client.py
   ```

---


4. 🧪 Example Commands (run on attacker side)

   ```bash

   Shell> whoami
   Shell> uname -a
   Shell> ls
   Shell> exit
   ```

---

### ⚠️ Disclaimer

- This project is intended solely for educational and ethical purposes.

- All tools, scripts, and configurations provided here are designed for use in controlled lab environments and authorized penetration testing only.

- Unauthorized access, scanning, or exploitation of systems without explicit permission is illegal and strictly prohibited.

- The author assumes no responsibility for any misuse or damage caused by the use of this code or any techniques demonstrated herein.

- By using or replicating this project, you agree to comply with all applicable local, national, and international laws regarding cybersecurity and ethical hacking.

---

###### _🌸🌸🌸🌸 The Perks of being a Wallflower 🌸🌸🌸🌸_

---
