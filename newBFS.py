graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
queue=[]
def find_all_paths(graph, start, end, path=[]):
    
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        queue.append(node)

    for node in graph[start]:
            
        n=queue[0]
        queue.pop(0)
        paths += find_all_paths(graph, n, end, path)
    return paths

list=[]
list=find_all_paths(graph, 'A', 'C')
if len(list) == 0:
    print "my_list is empty"
else:

    print "all path"
    print (list)
    print "shortest path"
    print(min(list,key=len))
