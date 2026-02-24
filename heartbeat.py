import psutil
import platform

print("--- Aliado Heartbeat ---")
print(f"System: {platform.system()}")
print(f"Node Name: {platform.node()}")
print(f"CPU Usage: {psutil.cpu_percent()}%")
print(f"Memory Usage: {psutil.virtual_memory().percent}%")
print("------------------------")
