#!/usr/bin/python
import webbrowser as wb
import os

def open_browser():
    url = 'http://127.0.0.1:5000/api/servers'
    wb.open_new_tab(url)
    #execfile("web.py")
def run_brow():
    os.system("start cmd")
    execfile('web.py')