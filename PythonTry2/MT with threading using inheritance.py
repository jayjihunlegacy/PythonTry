import threading
from time import sleep,ctime

loops=[4,2]

class MyThread(threading.Thread):
    def __init__(self,func,args,name="",verb=False):
        threading.Thread.__init__(self,name=name);
        self.func = func
        self.args = args
        self.verb = verb

    def getResult(self):
        return self.res

    def run(self):
        if self.verb:
            print("Starting {}, at:{}".format(self.name,ctime()))
        self.res = self.func(*self.args)
        if self.verb:
            print("{} finished at:".format(self.name,ctime()))



def loop(nloop,nsec):
    print("Start loop {} at : {}".format(nloop,ctime()));
    sleep(nsec)
    print("Loop {} done at : {}".format(nloop,ctime()));

def main():
    print("Starting at : {}".format(ctime()));
    threads=[]
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print("All done at : {}".format(ctime()));

if __name__ == "__main__":
    main()