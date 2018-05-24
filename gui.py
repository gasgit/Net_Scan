try:
    from Tkinter import *
    from ttk import *
except ImportError:  # Python 3
    from tkinter import *
    from tkinter.ttk import *

import ckpm 
import os, time
import socket, datetime, platform, subprocess
import json
import pprint

##ckpm.ckeck_platform()

# list locations and hostnames | ip addresses
# #ip_list = {"ATH HQ DC1":"001DC1", "ATH HQ FP1":"001FP1", "EH DC1":"159DC1", "EH FP1":"159FP1", "CLN DC":"015DC2", "CLN FP":"015FP1",
#             "BRD DC":"007DC1", "BRD FP":"007FP1", "AL LA DC":"069DC1", "AL LA FP":"069FP1", "AL PA DC":"146DC1", "AL PA FP":"146FP1",
#             "YR PA DC":"203DC1", "YR PA FP":"203FP1", "KN DC": "009DC1", "KN FP":"009FP1", "AL CTN DC":"149DC1", "AL CTN FP": "149FP1",
#              "VT GY FP":"247FP1", "VT GY DC":"247DC1"}

ip_list = {"CF1":"1.1.1.1","CF2":"1.0.0.1","GE1":"8.8.8.8","GE2":"8.8.4.4","Virgin":"virginmedia.ie", "Google":"google.ie", "Bing":"bing.ie",
"Python":"python.org"}

# list to store MyStatusObjects
status_collection = []


# create objects
class MyStatusObject:
    def __init__(self, server_location, server_name, server_status, server_ip, server_platform, test_time):
        self.server_location = server_location
        self.server_name = server_name
        self.server_status = server_status
        self.server_ip = server_ip
        self.server_platform = server_platform
        self.test_time = test_time
        
    def __repr__(self):
        return  "\nLN: " + self.server_location + "\nNM: " + self.server_name + "\nST: " + self.server_status + "\nIP: " + self.server_ip + "\nPL: " + self.server_platform + "\nTT: " + str(self.test_time)

# get current platform
p = platform.system()

# check platform, ping, response, time, ip & create object
def check_ping(k,v):
    ip = socket.gethostbyname(v)
    ttime = datetime.datetime.now()
   
      
    if p == 'Linux':
        response = os.system("ping -c 1 " + v)
        
    elif p == 'Windows':
        response = os.system("ping -n 1 " + v)
        
    date_time = datetime.datetime.now()
    if response == 0: 
        status = "Device Online" 
        my_new_object = MyStatusObject(k, v, status, ip, p, ttime)
        status_collection.append(my_new_object)
   
    else:
        status = "Device Error"
        my_new_object = MyStatusObject(k, v, status, ip, p, ttime)
        status_collection.append(my_new_object)
     
    return status

def pass_iplist(ip_list):
    for k,v in ip_list.items():
        check_ping(k,v)
        
def print_status_collection(col):
    for obj in col:
        print(obj)

def writelogs(col):
    json_string = json.dumps([ob.__dict__ for ob in col], indent=4,sort_keys=True, default=str)
    if os.path.getsize('my_logs.json') == 0:
        with open('my_logs.json', 'w') as f:
            f.write(json_string)
    else:
        read_logs()

current_logs = []

def read_logs():
     with open('my_logs.json') as f:
        data = json.load(f)
        print data
        for i in data:
            print i
       
       

pass_iplist(ip_list)
#print_status_collection(status_collection)
writelogs(status_collection)





time.sleep(1)

class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)
        

    def CreateUI(self):
        tv = Treeview(self)
        
        tv['columns'] = ('servername','location', 'ip', 'status')
        

        tv.heading("#0", text='DATE TIME', anchor='w')
        tv.column("#0", anchor="w", width=250)


        tv.heading('servername', text='SERVERNAME', anchor='w')
        tv.column('servername', anchor='w', width=100)

        tv.heading('location', text='LOCATION', anchor='w')
        tv.column('location', anchor='w', width=100)

        tv.heading('ip', text='IP', anchor='w')
        tv.column('ip', anchor='w', width=100)

        tv.heading('status', text='STATUS', anchor='w')
        tv.column('status', anchor='w', width=100)
  
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    
    
    def LoadTable(self):

        
        for i in status_collection:
            self.treeview.insert('', 'end',text=i.test_time, values=(i.server_name,i.server_location, i.server_ip, i.server_status))
           
       
   


def main():
    root = Tk()
    root.title("Ping Results")
    root.geometry('800x600')
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()