from flask import Flask, render_template
app = Flask(__name__)
import os, socket


ip_list = {"Athenry HQ DC1":"001DC1", "Athenry HQ FP1":"001FP1", "Eachreidh DC1":"159DC1", "Eachreidh FP1":"159FP1", "Clairn DC":"015DC2", "Clairn FP":"015FP1",
            "St Brigids DC":"007DC1", "St Brigids FP":"007FP1", "AL Loughrea DC":"069DC1", "AL Loughrea FP":"069FP1", "AL Portumna DC":"146DC1", "AL Portumna FP":"146FP1",
            "YR Portumna DC":"203DC1", "YR Portumna FP":"203FP1", "St Killians DC": "009DC1", "St Killians FP":"009FP1", "AL Cliften DC":"149DC1", "AL Cliften FP": "149FP1"}


status_collection = []


class MyStatusObject:
    def __init__(self, server_location, server_name, server_status, server_ip):
        self.server_location = server_location
        self.server_name = server_name
        self.server_status = server_status
        self.server_ip = server_ip

    def __repr__(self):
        return  "\nLN: " + self.server_location + "\nNM: " + self.server_name + "\nST: " + self.server_status + "\nIP: " + self.server_ip 


def check_ping(k,v):
    ip = socket.gethostbyname(v)
    response = os.system("ping -n 2 " + v)
    if response == 0: 
        status = "Device Online" 
        my_new_object = MyStatusObject(k, v, status, ip )
        status_collection.append(my_new_object)
    else:
        status = "Device Error"
        my_new_object = MyStatusObject(k, v, status, ip )
        status_collection.append(my_new_object)
    return status

def pass_iplist(ip_list):
    for k,v in ip_list.items():
        check_ping(k,v)
        
def print_status_collection(col):
    for obj in col:
        print obj


def rerun():
    status_collection[:] = []
    pass_iplist(ip_list)



# pass_iplist(ip_list)
# print_status_collection(status_collection)


@app.route("/api/servers")
def hello():
    pass_iplist(ip_list)
    print_status_collection(status_collection)



    
    return render_template('index.html', status_collection= status_collection)


@app.route('/api/servers/rerun')
def rerun():
    status_collection[:] = []
    pass_iplist(ip_list)

    return render_template('index.html', status_collection= status_collection)

if __name__ == '__main__':
    app.run()