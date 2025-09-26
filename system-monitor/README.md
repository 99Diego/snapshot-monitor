# Snapshot Utility
A simple system monitoring tool that captures CPU, memory, and process snapshots.

---

## Installation 
Clone the repository and install the package:
```bash
pip install -U .
```

---

## Usage
Run the snapshot toot with:
```bash
snapshot -i 2 -n 5 -f snapshot.json
```
- i → interval in seconds between snapshots

- n → number of snapshots to capture

- f → output file name

Snapshots will be printed to the console and appended line-by-line to the output file.

---

## Example
snapshot -i 2 -n 3 -f snapshot.json

cat snapshot.json

### ***Sample Output***
```json
{"Tasks": {"total": 254, "running": 1, "sleeping": 253, "stopped": 0, "zombie": 0}, "%CPU": {"user": 0.0, "system": 1.0, "idle": 12.0}, "KiB Mem": {"total": 24326504, "free": 18159672, "used": 6166832}, "KiB Swap": {"total": 8388604, "free": 8388604, "used": 0}, "Timestamp": 1758900665}
