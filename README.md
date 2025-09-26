# Snapshot Monitor- System Monitoring Utility
A lightweight Python utility that captures real-time system snapshots (CPU, memory, processes, swap) and saves them to JSON files while also printing them to the console.
Built with psutil, packaged with setuptools, and ready to run as a CLI tool (snapshot).

---

# Features
- Captures system metrics:

    ✅ CPU usage (user, system, idle)

    ✅ Memory (total, free, used)

    ✅ Swap memory

    ✅ Running process states

- Outputs results to console and JSON file

- Fully configurable:

    - i → interval between snapshots (default: 30s)

    - n → number of snapshots to capture (default: 20)

    -f → output file name (default: snapshot.json)

- Distributed as a Python package with a console entry point

- Developed using OOP principles (class SystemMonitor)

---

## Installation 
Clone the repository and install the package:
```
bash
git clone https://github.com/99Diego/snapshot-monitor.git
cd snapshot-monitor
pip install -U .
```
This will make the command snapshot available globally in your environment.

---

## Usage
Run the tool from the command line:
```
bash
snapshot -i 2 -n 5 -f snapshot.json
```
- Takes 3 snapshots every 2 seconds
- Saves them into snapshot.json
- Prints them to the console in real-time

---

### Example Output
```
json
{"Tasks": {"total": 254, "running": 1, "sleeping": 253, "stopped": 0, "zombie": 0},
 "%CPU": {"user": 2.0, "system": 1.1, "idle": 96.8},
 "KiB Mem": {"total": 24326504, "free": 18172116, "used": 6154388},
 "KiB Swap": {"total": 8388604, "free": 8388604, "used": 0},
 "Timestamp": 1758900670}
```

---

# Project Structure
```
bash
snapshot-monitor/
├── snapshot/             # Package code
│   ├── __init__.py
│   └── monitor.py        # SystemMonitor class + main()
├── setup.py              # Package configuration
├── README.md             # Documentation
└── tests/                # Unit tests (provided by EPAM)
```

---

# Tests
Run tests with:
```
bash
pytest tests/
```

---

# Future Improvements
- Add logging support

- Export snapshots to CSV or database

- Dockerize the tool for portability

- Integrate with monitoring stacks (Prometheus, Grafana)

