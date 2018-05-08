from flask import Flask, render_template
app = Flask(__name__)


import os


ip_list = {"Athenry HQ DC1":"001DC1", "Athenry HQ FP1":"001FP1", "Eachreidh DC1":"159DC1", "Eachreidh FP1": "159FP1", "Clairn DC":"015DC2", "Clairn FP":"015FP1",
            "St Brigids DC": "007DC1", "St Brigids FP": "007FP1", "AL Loughrea DC": "069DC1", "AL Loughrea FP": "069FP1", "AL Portumna DC": "146DC1", "AL Portumna FP":"146FP1",
            "YR Portumna DC": "203DC1", "YR Portumna FP": "203FP2"}

#ip_list = {"CF1":"1.1.1.1","GE1":"8.8.8.8","GE2":"8.8.4.4"}
# build quick check tool to check status lan/wan 
# devices up/down
# early days


online = {}
offline = {}


def check_ping(k,v):
    response = os.system("ping -n 1 " + v)
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



def return_online(on):
    return on



pass_iplist(ip_list)
print_online(online)
print_offline(offline)








@app.route("/api/servers")
def hello():

   return render_template('index.html', online= online, offline=offline)


if __name__ == '__main__':
    app.run()