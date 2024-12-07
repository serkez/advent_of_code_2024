rules = open("rules.txt").readlines()
#print(f"rules: {rules}")
input = open("input.txt").readlines()
sum_middle = 0
sum_middle_corrected = 0

def follows_rules(line)->bool:
    for rule in rules:
        a,b = rule.strip().split("|")
        if(a in line and b in line and line.index(a) > line.index(b)):
            return False
    return True     








def create_graph(rules):
    # Use a set to track unique nodes and ensure no duplicates
    adj = {}
    for rule in rules:
        a, b = rule.strip().split("|")
        # Ensure each node exists as a key
        if a not in adj:
            adj[a] = set()
        if b not in adj:
            adj[b] = set()
        # Add directed edge
        adj[a].add(b)
    return adj

def get_top_sort_order(adj):
    # Count in-degrees
    in_degrees = {node: 0 for node in adj}
    for node in adj:
        for neighbor in adj[node]:
            in_degrees[neighbor] = in_degrees.get(neighbor, 0) + 1
    
    # Queue starts with nodes having zero in-degree
    queue = [node for node, degree in in_degrees.items() if degree == 0]
    order = []

    while queue:
        current = queue.pop(0)
        order.append(current)

        # Process neighbors
        if current in adj:
            for neighbor in list(adj[current]):
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

    # If order doesn't include all nodes, there might be a cycle or disconnected components
    if len(order) != len(adj):
        print("Partial ordering or potential cycle detected")
        # Return a partial order instead of an empty list
        return order

    return order









# def create_graph(rules):
#     adj = {n:list() for rule in rules for n in rule.strip().split("|")}
#     #line = line.split(",")
#     for rule in rules:
#         a,b = rule.strip().split("|")
#         adj[a].append(b)
#         #print(f"Added edge {a} -> {b}, Updated Adjacency List: {adj}")
#     # for i in adj:
#     #     print(i)    
     
#     return adj
# def get_top_sort_order(adj):
#     #print(adj)
#     order = []
#     degrees = {}
#     for edges in adj:
#         degrees[edges]=0 
#     for edges in adj:    
#         for edge in adj[edges]:
#             if edge in degrees:
#                 degrees[edge]+=1
#             else:
#                 degrees[edge]=1    
    
#     # bfs
#     queue = list()
#     for k, v in degrees.items():
#         if v == 0:
#             queue.append(k)
#             for edge in adj[k]:
#                 degrees[edge] -= 1
#             degrees[k] -= 1    
#     while queue:
#         for k,v in degrees.items():
#             if v == 0:
#                 queue.append(k)
#                 for edge in adj[k]:
#                     degrees[edge] -= 1
#                 degrees[k] -= 1
#                 print("HIHIHI",order)
#         order.append(queue.pop(0))
#     #print(f"in get top sort, order: {order}")   
#     print(order)             
#     return order

def get_top_sort_order(adj):
    # Count in-degrees for each node
    in_degrees = {node: 0 for node in adj}
    for node in adj:
        for neighbor in adj[node]:
            in_degrees[neighbor] = in_degrees.get(neighbor, 0) + 1
    
    # Find nodes with zero in-degree to start
    queue = [node for node, degree in in_degrees.items() if degree == 0]
    order = []

    while queue:
        current = queue.pop(0)
        order.append(current)

        # Reduce in-degrees of neighbors
        for neighbor in adj.get(current, []):
            in_degrees[neighbor] -= 1
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)

    # Check if we have a complete topological sort
    if len(order) != len(adj):
        print("Warning: Graph contains a cycle")
        return []

    return order


def top_sort(order, line):
    order_map = {value: index for index, value in enumerate(order)}
    #print(order_map)

    def custom_sort_key(x):
        return order_map.get(x,float('inf'))

    # Sort the input list but keep elements not in the rules in their original order
    return sorted(line, key=lambda x: (custom_sort_key(x), line.index(x)))

    
    
def fix_order(line)->int:
    adj = create_graph(rules)
    #print(f"Adjacency List: {adj}")
    order = get_top_sort_order(adj)
    #print(order)
    sorted_line = top_sort(order,line.strip().split(","))
    return int(sorted_line[int(len(sorted_line)/2)])

for line in input:
    if follows_rules(line):
        #print(f"legal line: {line} ")
        sum_middle += int(line.split(",")[int(len(line.split(","))/2) ])
    else:
        sum_middle_corrected += fix_order(line)    


print(sum_middle)
print(sum_middle_corrected)