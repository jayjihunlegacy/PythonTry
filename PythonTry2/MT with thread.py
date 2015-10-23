import _thread
from time import sleep, ctime
import sys

#they do not show any race condition : they don't multithread!!



loops = [5,2];



x=0
def loop(nloop,nsec,lock):
    global x
    print("Start loop",nloop,"at:",ctime());
    for i in range(100):
        x+=1
        print("Loop {}, x is {}".format(nloop,x));
        sys.stdout.flush()
    
    #sleep(nsec)
    print("Loop",nloop,"done at:",ctime());
    lock.release();

def main():
    print("===Starting at :",ctime());
    locks = []
    nloops = range(len(loops))
    global x
    
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        _thread.start_new_thread(loop,(i,loops[i],locks[i]));

    for i in nloops:
        while locks[i].locked():
            pass
    print("Total x is :",x);
    print("===ALL Done at :",ctime());

if __name__ == "__main__":
    main();