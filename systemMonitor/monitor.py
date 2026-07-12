import psutil
import time
import logging
from datetime import datetime

# ----------------------------
# Logging Configuration
# ----------------------------

logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format="%(asctime)s | %(message)s"
)

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90


def get_system_info():
    cpu = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory().percent

    disk = psutil.disk_usage('/').percent

    return cpu, memory, disk


def display(cpu, memory, disk):

    print("\n" + "=" * 40)
    print("     SYSTEM RESOURCE MONITOR")
    print("=" * 40)

    print("Time :", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    print(f"\nCPU Usage    : {cpu}%")
    print(f"Memory Usage : {memory}%")
    print(f"Disk Usage   : {disk}%")

    print("\nStatus:")

    if cpu > CPU_THRESHOLD:
        print("WARNING : High CPU Usage")

    if memory > MEMORY_THRESHOLD:
        print("WARNING : High Memory Usage")

    if disk > DISK_THRESHOLD:
        print("WARNING : Low Disk Space")

    if (
        cpu <= CPU_THRESHOLD
        and memory <= MEMORY_THRESHOLD
        and disk <= DISK_THRESHOLD
    ):
        print("System Healthy")



def save_log(cpu, memory, disk):

    logging.info(
        f"CPU={cpu}% | Memory={memory}% | Disk={disk}%"
    )


print("\nStarting System Monitor...")
print("Press CTRL + C to stop.\n")

try:

    while True:

        cpu, memory, disk = get_system_info()

        display(cpu, memory, disk)

        save_log(cpu, memory, disk)

        time.sleep(5)

except KeyboardInterrupt:

    print("\nMonitoring Stopped.")