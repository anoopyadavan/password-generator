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
def making_list(data, num):
	yield data[0:num]
	
try:
    banner()
    minNum=int(input("Enter min length(default 2): ") or 2)
    maxNum=int(input("Enter max length(default 7): ") or 7)
    data=list(input("Enter character(default abc1234): ") or 'abc1234')
    for i in range(minNum,maxNum+1):
    	temp=list(making_list(data, i))
    	varl=perm1(temp[0])
    	for i in  varl:
    		print(''.join(i))
except KeyboardInterrupt as e:
    print('Quiting...')
    sleep(0.5)
