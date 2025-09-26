import argparse
import json
import os
import time
import psutil

class SystemMonitor:
    def __init__(self, interval, output_file, snapshots_count):
        self.interval = interval
        self.output_file = output_file
        self.snapshots_count = snapshots_count

    def get_snapshot(self):
        # Procesos por estado
        process_states = {"running": 0, "sleeping": 0, "stopped": 0, "zombie": 0}
        for proc in psutil.process_iter(['status']):
            status = proc.info['status']
            if status == psutil.STATUS_RUNNING:
                process_states["running"] += 1
            elif status == psutil.STATUS_SLEEPING:
                process_states["sleeping"] += 1
            elif status == psutil.STATUS_STOPPED:
                process_states["stopped"] += 1
            elif status == psutil.STATUS_ZOMBIE:
                process_states["zombie"] += 1

        total_processes = sum(process_states.values())

        # CPU
        cpu_times = psutil.cpu_times_percent()
        cpu = {
            "user": cpu_times.user,
            "system": cpu_times.system,
            "idle": cpu_times.idle
        }

        # Memoria
        mem = psutil.virtual_memory()
        mem_info = {
            "total": mem.total // 1024,
            "free": mem.available // 1024,
            "used": mem.used // 1024
        }

        # Swap
        swap = psutil.swap_memory()
        swap_info = {
            "total": swap.total // 1024,
            "free": swap.free // 1024,
            "used": swap.used // 1024
        }

        # Timestamp
        timestamp = int(time.time())

        snapshot = {
            "Tasks": {"total": total_processes, **process_states},
            "%CPU": cpu,
            "KiB Mem": mem_info,
            "KiB Swap": swap_info,
            "Timestamp": timestamp
        }

        return snapshot

    def run(self):
        # Limpiar archivo al iniciar
        with open(self.output_file, "w") as f:
            f.write("")

        for _ in range(self.snapshots_count):
            snapshot = self.get_snapshot()

            # Imprimir en consola
            os.system('clear')
            print(json.dumps(snapshot, indent=4))

            # Guardar en archivo (una línea por snapshot)
            with open(self.output_file, "a") as f:
                f.write(json.dumps(snapshot) + "\n")

            time.sleep(self.interval)

    def main():
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", help="Interval between snapshots in seconds", type=int, default=30)
        parser.add_argument("-f", help="Output file name", default="snapshot.json")
        parser.add_argument("-n", help="Quantity of snapshots to output", type=int, default=20)

        args = parser.parse_args()

        monitor = SystemMonitor(args.i, args.f, args.n)
        monitor.run()


if __name__ == "__main__":
    main()
