from typing import Dict,Tuple,List,Union
from math import inf,isclose
from collections import deque

EdgeData = Tuple[float,int] # 边数据，[准时概率,代价]

class Node:
    def __init__(self,index:int) -> None:
        self.index = index
        self.tos:Dict[Node,EdgeData] = {}
        return
    
    def link(self,other:"Node",poss:float,cost:int) -> None:
        self.tos[other] = (poss,cost) # poss -> possibility
        return
    
    def __repr__(self) -> str:
        return "<Node[{}] tos={}>".format(self.index,
            {i.index:j for i,j in self.tos.items()})

# 1 读入图
V,U,E,C = map(int, input().split())
graph = [Node(i) for i in range(V)]

spy_centers:List[Tuple[Node,int]] = []
for i in range(1,U+1):
    spy_centers.append((graph[i],int(input())))

for i in range(E):
    s,e,p,c = input().split()
    s = graph[int(s)]
    e = graph[int(e)]
    p = 1 - float(p)
    c = int(c)
    s.link(e,p,c)


# 2 搜索

# [城市编号,总开销,准时概率,出行路线]
Answer = Tuple[int,int,float,List[int]]
Path = List[int]
# [总开销,准时概率,出行路线]
PathInfo = Tuple[int,float,Path]

def best_path_of_spy_centers_iter() -> Answer:
    """依次yield每个领事馆的最优路径
    """
    def search_best_path(fr:Node,to:Node) -> PathInfo:
        best_poss = 0
        best_cost = inf
        best_path = [to]

        queue = deque()
        queue.appendleft(fr)

        for i in graph:
            i.poss = 0
            i.cost = inf

        fr.poss = 1
        fr.cost = 0
        fr.path = [fr]
        setattr(fr,"level",0)

        while queue:
            node:Node = queue.popleft()
            if node is to:
                if node.poss > best_poss or (
                    isclose(node.poss,best_poss)
                        and node.cost < best_cost):
                    best_poss = node.poss
                    best_cost = node.cost
                    best_path = node.path
                continue
            for n,(poss,cost) in node.tos.items():
                if hasattr(n,"level"):
                    if n.level < node.level:
                        continue
                else:
                    setattr(n,"level",node.level+1)
                    queue.append(n)

                temp_poss = node.poss * poss
                temp_cost = node.cost + cost
                if temp_poss > n.poss or (
                    isclose(temp_poss,n.poss) 
                        and temp_cost < n.cost):
                    n.poss = temp_poss
                    n.cost = temp_cost
                    n.path = node.path + [n]

        for i in graph:
            if hasattr(i,"level"):
                delattr(i,"level")
        return best_cost, best_poss, best_path


    v0 = graph[0]
    for i,j in spy_centers:
        goto_cost, goto_poss, goto_path = search_best_path(v0,i)
        back_cost, back_poss, back_path = search_best_path(i,v0)

        full_cost = goto_cost+back_cost+j
        if full_cost > C:
            continue

        goto_path.pop()
        full_path = goto_path + back_path

        yield i.index, full_cost , goto_poss*back_poss, full_path

    return

all_paths = list(best_path_of_spy_centers_iter())

a,b,c,d = max(all_paths, key=lambda x: (int(x[2]*100000),-x[1]))

print(a)
print(b)
print("{:.6f}".format(1-c))
print(" ".join([str(i.index) for i in d]))
