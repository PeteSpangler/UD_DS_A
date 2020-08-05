import math
from queue import PriorityQueue

def h(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))
#Euclidean heuristic implemented

def output_list(came_from, start, goal):
    current = goal
    route = [current]
    while current != start:
        current = came_from[current]
        route.append(current)
    route.reverse()
    return route



def shortest_path(M, start, goal):
    print("shortest path called")

    open_set = PriorityQueue()
    open_set.put(start, 0)
    
    came_from = {start: None}
    G_score = {start: 0}
    
    while not open_set.empty():
        current = open_set.get()
        
        if current == goal:
            output_list(came_from, start, goal)
        
        for node in M.roads[current]:
            temp_f_score = G_score[current] + h(M.intersections[current], M.intersections[node])
            
            if node not in G_score or temp_f_score < G_score[node]:
                G_score[node] = temp_f_score
                F_score = temp_f_score + h(M.intersections[current], M.intersections[node])
                open_set.put(node, F_score)
                came_from[node] = current
                
    return output_list(came_from, start, goal)  
                




# Source(s):
# https://brilliant.org/wiki/a-star-search/
# https://www.youtube.com/watch?v=JtiK0DOeI4A Tech with Tim visualization implementation