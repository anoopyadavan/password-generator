import os
from time import sleep
def banner():
    print("\t\t-----------------------------------------------------")
    print('\t\t|         P A S S W O R D    G E N E R A T O R       |')
    print("\t\t-----------------------------------------------------")

def perm1(lst):
    if len(lst)==0:
        yield []
    elif len(lst)==1:
        yield lst
    else:
        for i in range(len(lst)):
            x=lst[i]
            xs=lst[:i]+lst[i+1:]
            for p in perm1(xs):
                yield [x]+p

try:
    banner()
    minNum=int(input("Enter min length: "))
    maxNum=int(input("Enter max length: "))
    data=list('abc1234567890')
    varl=perm1(data)
    for i in  varl:
        print(''.join(i))
except KeyboardInterrupt as e:
    print('Quiting...')
    sleep(0.5)
