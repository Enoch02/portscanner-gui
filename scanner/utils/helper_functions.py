from socket import *
import time

def validate_input(hostname: str, start: str, end: str):
    ...

# TODO: validate input befor scanning
def scan_host(target: str):
    start_time = time.time()
    t_IP = gethostbyname(target)
    print ('Starting scan on host: ', t_IP)
   
    for i in range(50, 65535): # max value = 65535
        print("Scanning port", i)
        s = socket(AF_INET, SOCK_STREAM)
      
        conn = s.connect_ex((t_IP, i))
        if(conn == 0) :
            print ('Port %d: OPEN' % (i,))
        s.close()

    print('Time taken:', time.time() - start_time)
