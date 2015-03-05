#!/usr/local/bin/charm
import socket

try:

    #create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(('127.0.0.1', 40000))

    s.send("By the power invested in me I command you to work!!!...Please")

    s.close()


except Exception as err:
        print err
        exit(1)

