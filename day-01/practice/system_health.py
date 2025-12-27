import psutil
#Takes threshold values (CPU, disk, memory) from user input

def check_cpu_health():
    cpu_threshold = int(input("Enter cpu threshold: "))
    current_cpu = psutil.cpu_percent(interval=1)
    if current_cpu > cpu_threshold:
        print(f"current cpu utilization is {current_cpu}%, which is too high. Alert email sent...")
    else:
        print(f"Current cpu is {current_cpu} which is within the threshold. No alert sent")

    
def check_disk_health():
    disk_threshold = int(input("Enter disk threshold: "))
    current_disk = psutil.disk_usage("/")

    current_disk_percent = current_disk.percent
    if current_disk_percent > disk_threshold:
        print(f"Current disk utilization is {current_disk}, which is too high. Alert email sent")
    else:
        print(f"Current disk utilization is {current_disk}, which is within the threshold")

def check_memory():
    memory_threshold = int(input("Enter memory threshold: "))
    current_memory = psutil.virtual_memory().percent

    if current_memory > memory_threshold:
        print(f"Current memory utilization is {current_memory}, which is too high. Alert email sent.")
    else:
        print(f"Current memory utilization is {current_memory}, which is within the threshold.")

check_cpu_health()
check_disk_health()
check_memory()