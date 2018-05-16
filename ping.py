
import os

# 
ip_list = ["192.168.0.1", "192.168.0.108", "8.8.8.8"]


# goal is to buils quick check tool to check status lan/wan 
# devices up/down
# earl



def check_ping(hostname):
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        status = "Device Online"
    else:
        status = "Device Error"

    return status


for hostname in ip_list:
    check_ping(hostname)

