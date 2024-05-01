import socket
import subprocess
import sys
from datetime import datetime

# blank your screen
subprocess.call('clear', shell=True)

# Ask for input
remoteServer= input("Enter a remote host to scan: ").strip()
remoteServerIP= socket.gethostbyname(remoteServer)


# Print a nice banner with information on which host we are about to scan
print("_" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("_" * 60)

# # Check the date and time the scan was started 
t1= datetime.now()
print(t1)

# # Using the range function specify ports
# #Also we will do error handling


try:
    for port in range(1, 5000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        sock.close()
        if result == 0:
            print("Port {}: Open ".format(port))

except KeyboardInterrupt:
    print("You pressed Ctrl + C")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()


# # Checking time again
t2= datetime.now()

# # calculate the difference in time to know how long the scan took
total= t2-t1

# # Printing the Information on the screen
print("Scanning Completed in: ", total )