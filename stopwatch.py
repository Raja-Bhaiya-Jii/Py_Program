"""Stopwatch Application
A simple stopwatch with start, stop, and lap functionality."""
import time


class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.elapsed = 0
        self.running = False
        self.laps = []

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed
            self.running = True
            print("Stopwatch started.")
        else:
            print("Already running.")

    def stop(self):
        if self.running:
            self.elapsed = time.time() - self.start_time
            self.running = False
            print("Stopwatch stopped.")
        else:
            print("Not running.")

    def lap(self):
        if self.running:
            current = time.time() - self.start_time
            self.laps.append(current)
            print(f"Lap {len(self.laps)}: {self._format(current)}")
        else:
            print("Not running.")

    def reset(self):
        self.start_time = None
        self.elapsed = 0
        self.running = False
        self.laps = []
        print("Stopwatch reset.")

    def display(self):
        if self.running:
            t = time.time() - self.start_time
        else:
            t = self.elapsed
        print(f"Time: {self._format(t)}")

    def _format(self, seconds):
        m = int(seconds // 60)
        s = int(seconds % 60)
        ms = int((seconds * 100) % 100)
        return f"{m:02d}:{s:02d}.{ms:02d}"


def main():
    print("=" * 40)
    print("       STOPWATCH")
    print("=" * 40)
    sw = Stopwatch()
    while True:
        print("\n1.Start  2.Stop  3.Lap  4.Reset  5.Time  6.Exit")
        choice = input("Choice: ").strip()
        if choice == '1': sw.start()
        elif choice == '2': sw.stop()
        elif choice == '3': sw.lap()
        elif choice == '4': sw.reset()
        elif choice == '5': sw.display()
        elif choice == '6': break
        else: print("Invalid choice.")


if __name__ == "__main__":
    main()