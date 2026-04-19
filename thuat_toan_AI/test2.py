import heapq
class Node:
    def __init__(self,name,h):
        self.name=name
        self.h=h
        self.g=999
        self.f=999
        self.parent=None
    def __lt__(self, other):
        return self.f<other.f
def tim_duong(node_end):
    curr=node_end
    path=[]
    while curr is not None:
        path.append(curr.name)
        curr=curr.parent
    return path[::-1]
def thuat_thuat_toan_a(graph,heuristics,node_dau,node_cuoi):
    nodes={}
    for node,cost in heuristics.items():
        nodes[node]=Node(node,cost)
    start=nodes[node_dau]
    start.g=0
    start.f=0+start.h
    open_list=[start]
    close_list=set()
    line_g=[]
    line_f=[]
    step=0
    print(f" {'Bước':4} | {'U':10} | {'g(v)=g(u) + k(u,v)':<20} | {'f(v) = g(v) + h(v) ':<20} | {'open':<20}")
    while len(open_list)>0:
        u=heapq.heappop(open_list)
        ds=graph.get(u.name,[])
        list_ds=[]
        for node,cost in ds:
            list_ds.append(node)
        neight_name=" ".join(list_ds)
        if u.name==node_cuoi:
             print(f" {step:4} | {u.name:10} | {u.f:<20} | {'':<20} | {'tìm thấy':<20}")
             return tim_duong(u),u.g
        close_list.add(u)
        for node_xet,cost in ds:
            if node_xet in close_list:
                continue
            v=nodes[node_xet]
            new_g=u.g+cost
            new_f=v.g+v.f
            if new_f<v.f:
                v.f=new_f
                v.g=new_g
                v.parent=u
                heapq.heappush(open_list,v)
            line_g.append(f"g({v.name})={u.g}+{cost}={new_g}")
            line_f.append(f"f({v.name})={new_g}+{v.h}={new_f}")
            open1=open_list.copy()
            open1.sort()
            resul=[]
            for i in open1:
                resul.append(i)
                                       
    return None,9999
# --- Dữ liệu đồ thị ---
heuristics = {'A': 14, 'C': 15, 'D': 6, 'F': 7, 'H': 10, 'E':8,'I':4,'G':12,'K':12,'B':0}
graph = {
    'A': [('C', 9), ('D', 7), ('E', 13), ('F', 20)],
    'C':[('H',6)],
    'D':[('H',8),('E',4)],
    'F':[('G',4),('I',6)],
    'H':[('K',5)],
    'E':[('K',4),('I',3)],
    'I':[('K',9),('B',5)],
    'K':[('B',6)],
    'B':[]
}


duong,gia=thuat_thuat_toan_a(graph,heuristics,'A','B')

print(f"duong di la {duong}")
print(f"gia tri  di la {gia}")