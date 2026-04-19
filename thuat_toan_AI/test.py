import heapq

class Node:
    def __init__(self, name, h):
        self.name = name
        self.h = h
        self.g = float('inf')
        self.f = float('inf')
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

def tim_duong(node_end):
    path = []
    curr = node_end
    while curr is not None:
        path.append(curr.name)
        curr = curr.parent
    return "->".join(path[::-1])

def thuat_toan_a(graph, heuristics, node_dau, node_cuoi):
    nodes = {}
    for node, h in heuristics.items():
        nodes[node] = Node(node, h)

    start = nodes[node_dau]
    start.g = 0
    start.f = start.h + start.g

    open_list = []
    heapq.heappush(open_list, start)
    closed = set()
    out = open("output.txt", "w", encoding="utf-8")

    def write(line):
        print(line)
        out.write(line + "\n")

    write(f"{'Bước':<6} | {'U':<6} | {'Kề (U)':<10} | {'g(v)':<25} | {'f(v)':<20} | {'Open':<20}")
    write("-" * 110)
    write(f"{0:<6} | {'':<6} | {'':<10} | {'Khởi tạo':<25} | {'':<20} | {start.name}^{start.f:<20}")

    step = 1
    danh_sach_diem_ke = {}  

    while len(open_list) > 0:
        u = heapq.heappop(open_list)

        if u.f != u.g + u.h:
            continue

        if u.name in closed:
            continue

        if u.name == node_cuoi:
            write(f"{step:<6} | {u.name}^{u.f:<4} | {'':<10} | {'':<25} | {'':<20} | {'GOAL!':<20}")
            path = tim_duong(u)
            write(f"Đường đi là: {path}")
            write(f"Chi phí là: {u.g}")
            
            # Ghi danh sách các điểm kề đã xét
            write("\n" + "=" * 110)
            for diem, ke in danh_sach_diem_ke.items():
                write(f"Điểm {diem}: {len(ke)}")
            
            out.close()
            return path, u.g

        closed.add(u.name)

        neighbors = graph.get(u.name, [])
        
        # Lưu danh sách các điểm kề (chỉ lấy tên, không lấy trọng số)
        danh_sach_diem_ke[u.name] = [v_name for v_name, cost in neighbors]
        
        list_names = []
        for v_name, cost in neighbors:
            list_names.append(v_name)
        neighbor_names = " ".join(list_names)
        
        g_lines = []
        f_lines = []

        for v_name, cost in neighbors:
            v = nodes[v_name]
            new_g = u.g + cost
            new_f = new_g + v.h

            if v_name in closed and new_g >= v.g:
                continue

            if new_g < v.g:
                new_node = Node(v_name, v.h)
                new_node.g = new_g
                new_node.f = new_f
                new_node.parent = u

                nodes[v_name] = new_node
                heapq.heappush(open_list, new_node)

            g_lines.append(f"g({v_name})={u.g}+{cost}={new_g}")
            f_lines.append(f"f({v_name})={new_g}+{v.h}={new_f}")

        temp = open_list.copy()
        temp.sort()

        result = []
        for node in temp:
            text = node.name + "^" + str(node.f)
            result.append(text)

        open_display = " ".join(result)

        if g_lines:
            write(f"{step:<6} | {u.name}^{u.f:<4} | {neighbor_names:<10} | {g_lines[0]:<25} | {f_lines[0]:<20} | {open_display:<20}")
            for i in range(1, len(g_lines)):
                write(f"{'':<6} | {'':<6} | {'':<10} | {g_lines[i]:<25} | {f_lines[i]:<20} | {'':<20}")

        step += 1

    write("Không tìm thấy đường")
    out.close()
    return None, float('inf')

def doc_file_input(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    heuristics = {}
    graph = {}
    start = ""
    goal = ""
    
    idx = 0
    while idx < len(lines):
        if lines[idx] == "heuristics:":
            idx += 1
            while idx < len(lines) and lines[idx] != "graph:":
                if ':' in lines[idx]:
                    parts = lines[idx].split(':')
                    node = parts[0].strip()
                    h_val = int(parts[1].strip().strip(','))
                    heuristics[node] = h_val
                idx += 1
        elif lines[idx] == "graph:":
            idx += 1
            while idx < len(lines) and lines[idx] != "start:":
                if ':' in lines[idx] and lines[idx].count(':') == 1:
                    parts = lines[idx].split(':')
                    node = parts[0].strip()
                    if parts[1].strip() == "":
                        graph[node] = []
                    else:
                        neighbors = parts[1].split(',')
                        neighbor_list = []
                        for nb in neighbors:
                            nb = nb.strip()
                            if nb:
                                if '(' in nb and ')' in nb:
                                    nb_parts = nb.split('(')
                                    nb_name = nb_parts[0].strip()
                                    nb_cost = int(nb_parts[1].strip(')'))
                                    neighbor_list.append((nb_name, nb_cost))
                                else:
                                    # Trường hợp chỉ có tên không có trọng số (ít khi xảy ra)
                                    neighbor_list.append((nb, 1))
                        graph[node] = neighbor_list
                idx += 1
        elif lines[idx] == "start:":
            start = lines[idx + 1].strip()
            idx += 2
        elif lines[idx] == "goal:":
            goal = lines[idx + 1].strip()
            idx += 2
        else:
            idx += 1
    
    return heuristics, graph, start, goal

# Đọc dữ liệu từ file input.txt
heuristics, graph, start, goal = doc_file_input("input.txt")

# Chạy thuật toán
duong, gia = thuat_toan_a(graph, heuristics, start, goal)

print(f"\nĐường đi là: {duong}")
print(f"Chi phí là: {gia}")