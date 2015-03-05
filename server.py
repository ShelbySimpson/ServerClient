#!/usr/local/bin/charm
import socket

try:

    #create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind to an ip address / port tuple
    s.bind( ('127.0.0.1', 50000) )

    #listen for incoming connection(backlog of 5)
    s.listen(5)

    #accept incoming connection
    conn, addr = s.accept()
    print "connected to: ", addr

    #receive 100 bytes
    while True:
        data = conn.recv(100)

        #check for EOF (client closed socket)
        if not data:
            break

    #strip newline and carriage return characters
    data = data.strip('\n').strip('\r')

    #tokenize the string
    words = data.split(' ')

    #go through all words
    for w in words:
        print w

    # close the sockets
    conn.close()
    s.close()

except Exception as err:
        print err
        exit(1)
