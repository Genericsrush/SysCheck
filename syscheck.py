# Title: System checker
# Author: Macray Keeper
# Date: Feb 3, 2025
# Description: Fetches the system data and prints it to the console.

# Module imports
import psutil

# Converts bytes to megabytes
def mb_convert(num):
    return num/1000000

# Converts bytes to gagabytes
def gb_convert(num):
    return num/1000000000

# These variables fetch the computer statistics.
cpu_percentage = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory()
disk = psutil.disk_usage('/')
network = psutil.net_io_counters()

# Prints out details about the computer stats.
string = f"""The CPU is at: {"%.1f"%cpu_percentage}% usage
Memory usage: {"%.1f"%mb_convert(ram.used)}/{"%.0f"%mb_convert(ram.total)} MBs
Storage at: {"%.1f"%gb_convert(disk.used)}/{"%.1f"%gb_convert(disk.total)} GBs
Network usage at: {"%.1f"%mb_convert(network.packets_sent)} Mbps
Active processes:"""
print(string)
# Prints out the processes and their pids.
for proc in psutil.process_iter(['pid', 'name']):
    print("     ProcessID: {0} Process Name: {1}".format(proc.info["pid"],proc.info["name"]))