import threading
from time import sleep,ctime

loops=[4,2]

def loop(nloop,nsec):
    print("Start loop {} at : {}".format(nloop,ctime()));
    sleep(nsec)
    print("Loop {} done at : {}".format(nloop,ctime()));

def main():
    print("Starting at : {}".format(ctime()));
    threads=[]
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print("All done at : {}".format(ctime()));

if __name__ == "__main__":
    main()