import time
import random
from datetime import datetime

log_levels = ["INFO", "WARNING", "ERROR", "CRITICAL", "DEBUG"]
messages = [
    "User login successful",
    "Firewall breached",
    "Suspicious activity detected",
    "System rebooted",
    "Unauthorized access attempt",
    "Malware signature detected",
    "Brute-force attack detected",
]

def generate_log():
    timestamp = datetime.utcnow().isoformat()
    level = random.choice(log_levels)
    message = random.choice(messages)
    return f"{timestamp} [{level}] - {message}\n"

if __name__ == "__main__":
    with open("elk-stack/test-logs/generated.log", "a") as log_file:
        while True:
            log = generate_log()
            log_file.write(log)
            log_file.flush()
            print(log.strip())  # Optional: See output in terminal
            time.sleep(random.uniform(1, 3))
