import heapq

class Node:
    def __init__(self, name, h):
        self.name = name
        self.h = h              # Heuristic (ước lượng đến đích)
        self.g = 9999   # Chi phí thực tế từ điểm bắt đầu
        self.f = 999   # f = g + h (Tổng chi phí dự tính)
        self.parent = None      # Để truy vết đường đi

    # Bắt buộc phải có để heapq biết so sánh nút nào nhỏ hơn dựa trên f
    def __lt__(self, other):
        return self.f < other.f

def reconstruct_path(end_node):
    """Đi ngược từ đích về đầu dựa vào parent"""
    path = []
    current = end_node
    while current is not None:
        path.append(current.name)
        current = current.parent
    return path[::-1] # Đảo ngược lại để có Start -> End

def a_star_search(graph_data, heuristics, start_name, goal_name):
   
    nodes = {}
    for name, h in heuristics.items():
        # Tạo đối tượng Node
        new_node = Node(name, h)
        # Lưu vào dictionary
        nodes[name] = new_node
    
    start_node = nodes[start_name]
    start_node.g = 0
    start_node.f = start_node.h +start_node.g
    
    # 2. Open List (Heap) và Closed Set
    open_list = [start_node]
    closed_set = set()

    print(f"{'Duyệt U':<8} | {'f(u)':<5} | {'Open List (name^f)'}")
    print("-" * 50)

    while len(open_list)>0:
        
        # Lấy nút có f nhỏ nhất (ưu tiên nhất)
        u = heapq.heappop(open_list)
         # In log giống như bảng trong ảnh của bạn

        # Nếu đã đến đích, gọi hàm truy vết rồi trả về kết quả
        if u.name == goal_name:
            print(f"{u.name:<8} | {u.f:<5} | {'GOAL!'}")
            return reconstruct_path(u), u.g

        # Đưa vào tập đã duyệt xong
        closed_set.add(u.name)

        # 3. Xét các nút kề v của u
        for v_name, cost in graph_data.get(u.name, []):
            if v_name in closed_set:
                continue
            
            v_node = nodes[v_name]
            
            # Tính toán f mới thông qua nút u
            new_g = u.g + cost
            new_f = new_g + v_node.h

            # SO SÁNH F: Nếu tổng chi phí mới này rẻ hơn chi phí cũ của v
            if new_f < v_node.f:
                v_node.g = new_g
                v_node.f = new_f
                v_node.parent = u
                heapq.heappush(open_list, v_node)
                open_display = " ".join([f"{n.name}^{n.f}" for n in sorted(open_list)])
        print(f"{u.name:<8} | {u.f:<5} | {open_display}")
    return None, float('inf')
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

# --- Thực thi ---
path, total_cost = a_star_search(graph, heuristics, 'A', 'B')

print("-" * 110)
print(f"Đường đi tối ưu: {' -> '.join(path)}")
print(f"Tổng chi phí thực tế: {total_cost}")

