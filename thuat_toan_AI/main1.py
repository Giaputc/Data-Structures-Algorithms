import heapq

class Node:
    def __init__(self, name, h):
        self.name = name
        self.h = h
        self.g = 9999
        self.f = 999
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

def reconstruct_path(end_node):
    path = []
    current = end_node
    while current is not None:
        path.append(current.name)
        current = current.parent
    return path[::-1]

def a_star_search(graph_data, heuristics, start_name, goal_name):
   
    nodes = {}
    for name, h in heuristics.items():
        new_node = Node(name, h)
        nodes[name] = new_node
    
    start_node = nodes[start_name]
    start_node.g = 0
    start_node.f = start_node.h + start_node.g
    
    open_list = [start_node]
    heapq.heapify(open_list)  # Khởi tạo heap
    closed_set = set()
    
    # In tiêu đề bảng
    print(f"{'Bước':<6} | {'U':<6} | {'Kê (U)':<12} | {'g(v) = g(u) + k(u,v)':<25} | {'f(v) = g(v) + h(v)':<22} | {'Open':<20}")
    print("-" * 110)
    step = 0
    
    while len(open_list) > 0:
        
        u = heapq.heappop(open_list)  # Lấy phần tử nhỏ nhất theo f
        
        if u.name == goal_name:
            print(f"{step:<6} | {u.name}^{u.f:<4} | {'':<12} | {'':<25} | {'':<22} | {'GOAL!':<20}")
            return reconstruct_path(u), u.g
        
        closed_set.add(u.name)
        
        neighbors = graph_data.get(u.name, [])
        neighbor_names = " ".join([v_name for v_name, _ in neighbors])
        
        g_lines = []
        f_lines = []
        
        for v_name, cost in neighbors:
            if v_name in closed_set:
                continue
            
            v_node = nodes[v_name]
            new_g = u.g + cost
            new_f = new_g + v_node.h
            
            if new_f < v_node.f:
                v_node.g = new_g
                v_node.f = new_f
                v_node.parent = u
                heapq.heappush(open_list, v_node)  # Thêm vào heap
            
            g_lines.append(f"g({v_name})={u.g}+{cost}={new_g}")
            f_lines.append(f"f({v_name})={new_g}+{v_node.h}={new_f}")
        
        # Tạo open_display từ heap (copy ra để không ảnh hưởng heap gốc)
        temp_list = open_list.copy()
        temp_list.sort()  
        result_elements = []
        for n in temp_list:
            item = f"{n.name}^{n.f}"
            result_elements.append(item)

        open_display = " ".join(result_elements)
        
        # In dòng đầu tiên
        if g_lines:
            print(f"{step:<6} | {u.name}^{u.f:<4} | {neighbor_names:<12} | {g_lines[0]:<25} | {f_lines[0]:<22} | {open_display:<20}")
            for i in range(1, len(g_lines)):
                print(f"{'':<6} | {'':<6} | {'':<12} | {g_lines[i]:<25} | {f_lines[i]:<22} | {'':<20}")
        else:
            print(f"{step:<6} | {u.name}^{u.f:<4} | {neighbor_names:<12} | {'':<25} | {'':<22} | {open_display:<20}")
        
        step += 1
    
    return None, 9999

# --- Dữ liệu đồ thị ---
heuristics = {'A': 14, 'C': 15, 'D': 6, 'F': 7, 'H': 10, 'E': 8, 'I': 4, 'G': 12, 'K': 2, 'B': 0}
graph = {
    'A': [('C', 9), ('D', 7), ('E', 13), ('F', 20)],
    'C': [('H', 6)],
    'D': [('H', 8), ('E', 4)],
    'F': [('G', 4), ('I', 6)],
    'H': [('K', 5)],
    'E': [('K', 4), ('I', 3)],
    'I': [('K', 9), ('B', 5)],
    'K': [('B', 6)],
    'B': []
}

# --- Thực thi ---
path, total_cost = a_star_search(graph, heuristics, 'A', 'B')

print("-" * 110)
print(f"Đường đi tối ưu: {' -> '.join(path)}")
print(f"Tổng chi phí thực tế: {total_cost}")