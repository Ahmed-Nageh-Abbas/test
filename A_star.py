graph={
    'A':[('B',4),('C',3),('E',7)] ,
    'B':[('A',4),('C',6),('D',5)],
    'C':[('A',3),('B',6),('D',11),('E',8)],
    'D':[('B',5),('C',11),('E',2)],
    'E':[('A',7),('C',8),('D',2),('G',5)],
    'F':[('D',2),('G',3)],
    'G':[('E',5),('F',3)]
}
# fgds
H_Table={
    'A':1*2,
    'B':1*2,
    'C':2*2,
    'D':3*2,
    'E':3*2,
    'F':5*2,
    'G':0*2
}

def search(start,goal):
    visited = set()
    visited.add(start)
    fronter = [(0,start,[start],0)]
    while fronter:
        fronter.sort()
        f_cost,curr_city,curr_path,g_cost = fronter.pop(0)
        
        if curr_city == goal:
            return (curr_path,g_cost)
        
        for child_city, child_cost in graph[curr_city]:
                if child_city not in visited:
                    visited.add(child_city)
                    fronter.append((g_cost+child_cost+H_Table[child_city],child_city,curr_path+[child_city],g_cost+child_cost))

    return "No Solution found!"

def main():
     sol = search('A','G')
     print("path:", sol[0])
     print("total cost:",sol[1])

main()
