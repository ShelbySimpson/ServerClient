#!/usr/local/bin/charm
import threading
import sys

#global variable var needs global lock object
var = 0
mutex = threading.Lock()

#function for thread to run
def fx(arg):
    global var,mutex

    #use the argument
    print "running thread #", arg

    #100 iterations: acquire lock, var++, reelease lock
    for i in range(100):
        mutex.acquire()
        lvar = var
        lvar = lvar + 1
        var = lvar
        mutex.release()

try:
    #list to keep track of spawned threads
    threads = []

    #check cmd line args
    if len(sys.argv) != 2:
        print "usage: ./a.out.py num_threads"
        sys.exit();

    #convert cmd line arg to integer
    num = int(sys.argv[1]);

    #spawn off num threads
    for i in range(num):

        #creat thread to run fx with argument i
        t = threading.Thread(target=fx, args=(i,))

        #start thread
        t.start()

        #add thread object to list of threads
        threads.append(t)

    #join thread objects
    for t in threads:
            t.join()

    #print result (w/check)
    lvar = num * 100;
    print var, " should be ", lvar




except Exception as err:
        print err
        exit(1)

