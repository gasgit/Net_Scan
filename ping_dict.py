
import os


#ip_list = {"HQ DC":"001DC1", "HQ FP":"001FP1", "EH DC":"159DC1", "EH FP": "159FP1", "CN DC":"015DC2", "CN FP":"015FP1"}

ip_list = {"CF1":"1.1.1.1","CF2":"1.0.0.1","GE1":"8.8.8.8","GE2":"8.8.4.4"}
# build quick check tool to check status lan/wan 
# devices up/down
# early days


online = {}
offline = {}


def check_ping(k,v):
    response = os.system("ping -c 1 " + v)
    if response == 0:
        status = ": Device Online" 
        online[k,v] = status
    else:
        status = ": Device Error"
        print status
        offline[k,v] = status
    return status

def pass_iplist(ip_list):
    for k,v in ip_list.items():
        check_ping(k,v)


def print_online(on):
    for k,v in on.items():
        print k, v


def print_offline(off):
    for k,v in off.items():
        print k, v

pass_iplist(ip_list)
print_online(online)
print_offline(offline)