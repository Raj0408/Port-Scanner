import socket
import termcolor
def scan(target2 , port):
    for i in range(0,port):
        scan_port(target2,i)
def scan_port(target3,port):
    try:
        sock = socket.socket()
        sock.connect((target3,port))
        print("[+] Port Opened " + str(port))
        sock.close()

    except:
        pass

    
                                                                  
print(
"""        
 / ___| _ __  ___   __ _ | |_  | |/ / __ _  _ __    ___  _ __ (_) _   _   __ _ 
| |  _ |  __|/ _ \ / _` || __| |   / / _` ||  _ \  / _ \|  __|| || | | | / _` |
| |_| || |  |  __/| (_| || |_  | . \| (_| || | | ||  __/| |   | || |_| || (_| |
 \____||_|   \___| \__,_| \__| |_|\_\__,_| |_| |_| \___||_|   |_| \__, | \__,_|
                                                                  |___/
                                                                  
                                                                  """)
                                                                  
target = input("Enter the targets (split by ,) : ")
ports = int(input("Enter How many Ports : "))

x = target.split(',')

print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))

for i in x:
    scan(i,ports)
    
