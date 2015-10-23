import threading
from time import sleep,ctime
import sys

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

def fib(x):
    if x<2:
        return 1
    return (fib(x-2)+fib(x-1))

def fac(x):
    if x<2:
        return 1
    return (x*fac(x-1))

def sum(x):
    if x<2:
        return 1
    return (x+sum(x-1))

funcs = (fib,fac,sum)

n=36

def main():
    nfuncs = range(len(funcs))

    print("=====Single threading=====")
    for i in nfuncs:
        print("Starting : {}, at : {}".format(funcs[i].__name__,ctime()))
        sys.stdout.flush()
        funcs[i](n)
        print("Finished : {}, at : {}".format(funcs[i].__name__,ctime()))
        sys.stdout.flush()

    print("=====Multi threading======")
    threads = []
    for i in nfuncs:
        thread = MyThread(funcs[i],(n,),funcs[i].__name__)
        threads.append(thread)

    print("Starting ALL, at : {}".format(ctime()))
    sys.stdout.flush()
    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print("{} joined!".format(i))

    print("Finished ALL, at : {}".format(ctime()))
    sys.stdout.flush()
    #for i in nfuncs:
    #    print(threads[i].getResult())

if __name__ == "__main__":
    main()