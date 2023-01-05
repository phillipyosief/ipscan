import subprocess
import socket
import time
from dearpygui_pkg.dearpygui.dearpygui import *

filename = "ip.txt"

print('[-] IP ist schone belegt\n',
      '[+] IP ist frei\n')

def write(hostname):
   # Fügt IPs zur Datei hinzu (doppelte IPs werden nicht überprüft!)
   try:
      with open(filename, 'a') as f:
         f.writelines(f'{address} ({hostname})\n')
   except FileNotFoundError:
      open(filename, 'w')

      with open(filename, 'a') as f:
         f.writelines(f'{address} ({hostname})\n')


one_range_1 = 111
one_range_2 = 255

two_range_1 = 1
two_range_2 = 255

# 3. IP Feld
for one in range(111,255):
   # 4. IP Feld
    for two in range(1,255):
      address = "10.114." + str(one) + '.' + str(two)
      res = subprocess.call(['ping', '-n', '1', '-w', '1', address], # Windows Ping cmd -n = versuch, -w = timeout
      stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) # Um CMD Output zu vermeiden
      

      if res == 0:
         try:
            hostname = socket.gethostbyaddr(str(address))[0]
            print(f"[-] {address} ({hostname})")
            write(hostname)
         except:
            # falls die IP kein Hostnamen hat
            print(f'[-] {address} (N/A)')
            write('N/A')
      # IP gibt keine meldung
      elif res == 2:
          print("[+]", address)
      else:
          print("[+]", address)

