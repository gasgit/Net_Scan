#!/usr/bin/python



# list locations and hostnames | ip addresses
ip_list = {"ATH HQ DC1":"001DC1", "ATH HQ FP1":"001FP1", "EH DC1":"159DC1", "EH FP1":"159FP1", "CLN DC":"015DC2", "CLN FP":"015FP1",
            "BRD DC":"007DC1", "BRD FP":"007FP1", "AL LA DC":"069DC1", "AL LA FP":"069FP1", "AL PA DC":"146DC1", "AL PA FP":"146FP1",
            "YR PA DC":"203DC1", "YR PA FP":"203FP1", "SK NI DC": "009DC1", "SK NI FP":"009FP1", "AL CTN DC":"149DC1", "AL CTN FP": "149FP1",
             "VT GY FP":"247FP1", "VT GY DC":"247DC1", "MY AL DC":"047DC1", "MY AL FP":"047FP1","OD DC":"106DC1", "OD FP":"106FP1",
             "VT BS DC":"068DC1","VT BS FP":"068FP1", "YR BS DC":"044DC1","YR BS FP":"044FP1" }

# ip_list = {"CF1":"1.1.1.1","CF2":"1.0.0.1","GE1":"8.8.8.8","GE2":"8.8.4.4","Virgin":"virginmedia.ie", "Google":"google.ie", "Bing":"bing.ie",
# "Python":"python.org"}

def return_list():
    return ip_list