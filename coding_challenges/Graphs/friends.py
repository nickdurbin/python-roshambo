def csFriendCircles(friendships):
    # friendships: is an array of arrays 
    # we just want the number of friend circles
    num_circles = 0    
    visited = set()
    # go through all students
    for student in range(len(friendships)):  # student = 0, 1, 2, 3, ... N-1 
        # if we've already visited the cur_student in a friend circle: 
        if student in visited: 
        #   skip them
            continue
        # otherwise: 
        else: 
        #   count their friend circle
        #   add 1 to num_circle
            num_circles += 1
        #   track all friends in that friend circle so we don't visited them later
            # 1) get the friends in the friend_circle
            friend_circle = get_friend_circle_for_student(friendships, student)
            # 2) add the friends to visited so we can skip them later
            visited.update(friend_circle)
    return num_circles
# how do we get the cur_student's direct friends from an adjacency matrix? 
# find the value at each index and see if it equals 0 or 1
def get_friends_for_student(friendships, cur_student):
    cur_students_edges = friendships[cur_student] # cur_student = 0. cur_students_edges = [1, 0, 1]
    cur_student_friends = []
    for idx, val in enumerate(cur_students_edges): 
        if val == 1: 
            # 0 and idx are direct friends
            cur_student_friends.append(idx)
    return cur_student_friends
def get_friend_circle_for_student(friendships, cur_student):
    visited = set()
    friends = get_friends_for_student(friendships, cur_student) # these are 0's direct friends
    # friends = [2]
    # how do we find their indirect friends? are the friends of their friends
    while len(friends) != 0:  # there are still friends we need to visit
        cur_friend = friends.pop(0)
        # don't add students we've already "visited"
        indirect_friends = get_friends_for_student(friendships, cur_friend)
        # if we haven't visited an indirect_friend, add it to the queue (friends)
            # and add it to visited
        for indirect_friend in indirect_friends: 
            if indirect_friend not in visited: 
                friends.append(indirect_friend)
                visited.add(indirect_friend)
    return visited
    # friends.extend(get_friends_for_student(cur_friend))
# indirect_friends = [1, 3, 6, 7]
# matrix: an array of arrays
# matrix[0] is an array [1, 0, 1]
# matrix[1] is [0, 1, 0]
# [1,0,1],
# [0,1,0],
# [1,0,1]