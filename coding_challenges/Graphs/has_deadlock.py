def hasDeadlock(connections):
    # find out if the graph has a cycle
    # helper function to see if a nodes children are visited 
    def are_children_visited(vert):
        print(connections[vert])
        for i in range(len(connections[vert])):
            if connections[vert][i] in visited:
                return True
                print('yes in visited **********')
            else:
                return False
    # iterating the WHOLE array
    for i in range(len(connections)):
        # keep track of visited verts
        visited = []
        q = []
        # creating a new q every iteration with the current index 
        q.append(i)
        # while there is a vert in the q
        while q:
            cur = q.pop(0)
            print('current after pop', cur)
            # add the current vert to visited
            visited.append(cur)
            print('visited after append', visited)
            # iterate the current verts neighbors
            for i in range(len(connections[cur])):
                neighbor = connections[cur][i]
                print('neighbor just created', neighbor)
                # check if any neighbors OR their neighbors are already in 
                # visited
                # if they are in visited return True there IS a cycle
                if neighbor in visited:
                    if are_children_visited(neighbor):
                        return True
                    print('neighbor in visited', neighbor)
                    print('visited', visited)
                # else add the neigbor to the q if not already in the q
                else:
                    if neighbor not in q:
                        q.append(neighbor)
                        print('q appended neighbor', q)
    # return False if we find no cycle
    return False