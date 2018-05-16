from flask import Flask, render_template
import os, socket, datetime
app = Flask(__name__)



ip_list = {"ATH HQ DC1":"001DC1", "ATH HQ FP1":"001FP1", "EH DC1":"159DC1", "EH FP1":"159FP1", "CLN DC":"015DC2", "CLN FP":"015FP1",
            "BRD DC":"007DC1", "BRD FP":"007FP1", "AL LA DC":"069DC1", "AL LA FP":"069FP1", "AL PA DC":"146DC1", "AL PA FP":"146FP1",
            "YR PA DC":"203DC1", "YR PA FP":"203FP1", "KN DC": "009DC1", "KN FP":"009FP1", "AL CTN DC":"149DC1", "AL CTN FP": "149FP1",
             "VT GY FP":"247FP1", "VT GY DC":"247DC1"}


status_collection = []



# TODO
# 404
# fix landing
# get more attributes from ping


class MyStatusObject:
    def __init__(self, server_location, server_name, server_status, server_ip, status_time):
        self.server_location = server_location
        self.server_name = server_name
        self.server_status = server_status
        self.server_ip = server_ip
        self.status_time = status_time

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
        status_collection.append(my_new_object)
    return status

def pass_iplist(ip_list):
    for k,v in ip_list.items():
        check_ping(k,v)
        
def print_status_collection(col):
    for obj in col:
        print obj



@app.route('/api/servers/')
def index():
    return render_template('index.html')


@app.route("/api/servers/display")
def display_servers():
    pass_iplist(ip_list)
    print_status_collection(status_collection)
    return render_template('display_servers.html', status_collection= status_collection)


@app.route('/api/servers/rerun')
def rerun():
    status_collection[:] = []
    pass_iplist(ip_list)
    return render_template('display_servers.html', status_collection= status_collection)

if __name__ == '__main__':
    app.run()