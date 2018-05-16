from flask import Flask, render_template
<<<<<<< HEAD
import os, socket, datetime, platform, subprocess
app = Flask(__name__)


# list locations and hostnames | ip addresses
# ip_list = {"ATH HQ DC1":"001DC1", "ATH HQ FP1":"001FP1", "EH DC1":"159DC1", "EH FP1":"159FP1", "CLN DC":"015DC2", "CLN FP":"015FP1",
#             "BRD DC":"007DC1", "BRD FP":"007FP1", "AL LA DC":"069DC1", "AL LA FP":"069FP1", "AL PA DC":"146DC1", "AL PA FP":"146FP1",
#             "YR PA DC":"203DC1", "YR PA FP":"203FP1", "KN DC": "009DC1", "KN FP":"009FP1", "AL CTN DC":"149DC1", "AL CTN FP": "149FP1",
#              "VT GY FP":"247FP1", "VT GY DC":"247DC1"}

ip_list = {"CF1":"1.1.1.1","CF2":"1.0.0.1","GE1":"8.8.8.8","GE2":"8.8.4.4","Virgin":"virginmedia.ie", "Google":"google.ie", "Bing":"bing.ie",
"Python":"python.org"}




# list to store MyStatusObjects
=======
import os, socket, datetime
app = Flask(__name__)



ip_list = {"ATH HQ DC1":"001DC1", "ATH HQ FP1":"001FP1", "EH DC1":"159DC1", "EH FP1":"159FP1", "CLN DC":"015DC2", "CLN FP":"015FP1",
            "BRD DC":"007DC1", "BRD FP":"007FP1", "AL LA DC":"069DC1", "AL LA FP":"069FP1", "AL PA DC":"146DC1", "AL PA FP":"146FP1",
            "YR PA DC":"203DC1", "YR PA FP":"203FP1", "KN DC": "009DC1", "KN FP":"009FP1", "AL CTN DC":"149DC1", "AL CTN FP": "149FP1",
             "VT GY FP":"247FP1", "VT GY DC":"247DC1"}


>>>>>>> a72ac3731d046f19eadd4a831600fd4430343312
status_collection = []



# TODO
# 404
# fix landing
# get more attributes from ping


<<<<<<< HEAD
# create objects
class MyStatusObject:
    def __init__(self, server_location, server_name, server_status, server_ip, status_time, server_platform):
=======
class MyStatusObject:
    def __init__(self, server_location, server_name, server_status, server_ip, status_time):
>>>>>>> a72ac3731d046f19eadd4a831600fd4430343312
        self.server_location = server_location
        self.server_name = server_name
        self.server_status = server_status
        self.server_ip = server_ip
        self.status_time = status_time
<<<<<<< HEAD
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
=======

    def __repr__(self):
        return  "\nLN: " + self.server_location + "\nNM: " + self.server_name + "\nST: " + self.server_status + "\nIP: " + self.server_ip + "\nTE: " + self.status_time


def check_ping(k,v):
    ip = socket.gethostbyname(v)
    response = os.system("ping -n 1 " + v)
    stat_time = datetime.datetime.now()
    if response == 0: 
        status = "Device Online" 
        my_new_object = MyStatusObject(k, v, status, ip, stat_time )
        status_collection.append(my_new_object)
    else:
        status = "Device Error"
        my_new_object = MyStatusObject(k, v, status, ip, stat_time )
>>>>>>> a72ac3731d046f19eadd4a831600fd4430343312
        status_collection.append(my_new_object)
    return status

def pass_iplist(ip_list):
    for k,v in ip_list.items():
        check_ping(k,v)
        
def print_status_collection(col):
    for obj in col:
        print obj


<<<<<<< HEAD
# landing page 
=======

>>>>>>> a72ac3731d046f19eadd4a831600fd4430343312
@app.route('/api/servers/')
def index():
    return render_template('index.html')

<<<<<<< HEAD
# display results
@app.route("/api/servers/display")
def display_servers():
    pass_iplist(ip_list)
    return render_template('display_servers.html', status_collection= status_collection)

# retest route
=======

@app.route("/api/servers/display")
def display_servers():
    pass_iplist(ip_list)
    print_status_collection(status_collection)
    return render_template('display_servers.html', status_collection= status_collection)


>>>>>>> a72ac3731d046f19eadd4a831600fd4430343312
@app.route('/api/servers/rerun')
def rerun():
    status_collection[:] = []
    pass_iplist(ip_list)
    return render_template('display_servers.html', status_collection= status_collection)

if __name__ == '__main__':
    app.run()