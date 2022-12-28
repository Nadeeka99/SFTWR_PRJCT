import platform

# Windows
if platform.system() == "Windows":
  import wmi
  
  # Get a list of wifi connections
  wifi_connections = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True, MACAddress='00:00:00:00:00:00')
  
  # Iterate through the list of connections and print out the names
  for connection in wifi_connections:
    print(connection.Description)

# macOS
elif platform.system() == "Darwin":
  import subprocess
  import re
  
  # Get a list of wifi connections
  output = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-s"])
  output = output.decode("utf-8")
  
  # Extract the names of the connections from the output
  connections = re.findall(r"(.+?)\s+([\dA-F:]+)", output)
  
  # Iterate through the list of connections and print out the names
  for connection in connections:
    print(connection[0])

# Other platforms
else:
  print("This platform is not supported")
