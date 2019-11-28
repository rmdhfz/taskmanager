import psutil

print("\nTask Manager:")

for process in psutil.process_iter():
	processID = process.pid
	processName	= process.name()

	print("Process ID : ",processID," Process Name : ",processName)