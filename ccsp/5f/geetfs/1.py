from typing import List, Dict
from collections import UserDict

class GeetFile:
    def __init__(self,name:str) -> None:
        self.name = name
        self.data:List[str] = []
        return
    
    def read(self,offset:int,size:int) -> str:
        wtf = offset + size
        temp = self.data[offset:wtf]
        wtf -= len(self.data)
        if wtf > 0:
            temp.extend("." * wtf)
        return "".join(temp)

    def write(self,offset:int,data:str) -> None:
        wtf = offset + len(data) - len(self.data)
        if wtf > 0:
            self.data.extend(["."] * wtf)
        for i in data:
            self.data[offset] = i
            offset += 1
        return


class GeetFileSystem(UserDict):
    def w(self,name:str) -> GeetFile:
        return self.data.setdefault(name,GeetFile(name))

    def r(self,name:str) -> GeetFile:
        return self.data.get(name,None)
    
    def delete(self,name:str) -> None:
        self.data.pop(name,None)
        return
    
    def listall(self) -> List[str]:
        return list(self.data)

fs = GeetFileSystem()


def parse_and_exec_cmd():
    cmd, *args = input().split()
    if cmd == "write":
        name, offset, size = args
        data = input().strip()
        fs.w(name).write(int(offset),data)
    elif cmd == "read":
        name, offset, size = args
        f = fs.r(name)
        if f is None:
            print("." * int(size),end="\n")
        else:
            print(f.read(int(offset),int(size)),end="\n")
    elif cmd == "unlink":
        name, = args
        fs.delete(name)
    elif cmd == "ls":
        omg = fs.listall()
        omg.sort()
        if omg:
            print(len(omg), omg[0], omg[-1],end="\n")
        else:
            print(0,end="\n")
    return


N = int(input())
for i in range(N):
    parse_and_exec_cmd()
