#!/usr/bin/python
from flask import Flask, render_template
import os
import socket, datetime, platform, subprocess
# get list ips
from ip_list import return_list
import ckpm 

app = Flask(__name__)

ckpm.ckeck_platform()

# list to store MyStatusObjects
status_collection = []

# TODO
# 404
# fix landing
# get more attributes from ping

# create objects
class MyStatusObject:
    def __init__(self, server_location, server_name, server_status, server_ip, status_time, server_platform):
        self.server_location = server_location
        self.server_name = server_name
        self.server_status = server_status
        self.server_ip = server_ip
        self.status_time = status_time
        self.server_platform = server_platform

    def __repr__(self):
        return  "\nLN: " + self.server_location + "\nNM: " + self.server_name + "\nST: " + self.server_status + "\nIP: " + self.server_ip + "\nTE: " + self.status_time + "\nPL: " + self.server_platform

# get current platform
p = platform.system()

# check platform, ping, response, time, ip & create object
def check_ping(k,v):
    ip = socket.gethostbyname(v)
      
    if p == 'Linux':
        response = os.system("ping -c 1 " + v)
        
    elif p == 'Windows':
        response = os.system("ping -n 1 " + v)
        
    stat_time = datetime.datetime.now()
    if response == 0: 
        status = "Device Online" 
        my_new_object = MyStatusObject(k, v, status, ip, stat_time, p)
        status_collection.append(my_new_object)
    else:
        status = "Device Error"
        my_new_object = MyStatusObject(k, v, status, ip, stat_time, p )
        status_collection.append(my_new_object)
    return status

def pass_iplist(ip_list):
    for k,v in ip_list.items():
        check_ping(k,v)
    return status_collection   
        
def print_status_collection(col):
    for obj in col:
        print obj


# landing page 
@app.route('/api/servers/')
def index():   
    return render_template('index.html')

# display results
@app.route("/api/servers/display")
def display_servers():
    pass_iplist(return_list())
 
    return render_template('display_servers.html', status_collection=status_collection)

# retest route
@app.route('/api/servers/rerun')
def rerun():
    status_collection[:] = []
    pass_iplist(return_list())
    return render_template('display_servers.html', status_collection= status_collection)


if __name__ == '__main__':
    app.run()