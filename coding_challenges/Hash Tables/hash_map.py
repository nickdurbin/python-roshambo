"""
hashMap
You've created a new programming language, and now you've decided to add hashmap support to it. Actually you are quite
disappointed that in common programming languages it's impossible to add a number to all hashmap keys, or all its
values. So you've decided to take matters into your own hands and implement your own hashmap in your new language that
has the following operations:
​
insert x y - insert an object with key x and value y.
get x - return the value of an object with key x.
addToKey x - add x to all keys in map.
addToValue y - add y to all values in map.
​
To test out your new hashmap, you have a list of queries in the form of two arrays:
queryTypes contains the names of the methods to be called (eg: insert, get, etc), and
queries contains the arguments for those methods (the x and y values).
​
Your task is to implement this hashmap, apply the given queries, and to find the sum of all the results for get operations.
​
Example
​
For queryType = ["insert", "insert", "addToValue", "addToKey", "get"] and
    query =     [[1, 2], [2, 3], [2], [1], [3]],
the output should be hashMap(queryType, query) = 5.
​
The hashmap looks like this after each query:
1 query: {1: 2}         insert 1, 2
2 query: {1: 2, 2: 3}   insert 2, 3
3 query: {1: 4, 2: 5}   addToValue 2
4 query: {2: 4, 3: 5}   addToKey 1
5 query: answer is 5    get 3
The result of the last get query for 3 is 5 in the resulting hashmap.
​
​
For
queryType = ["insert", "addToValue", "get", "insert", "addToKey", "addToValue", "get"] and
query = [[1, 2], [2], [1], [2, 3], [1], [-1], [3]], the output should be hashMap(queryType, query) = 6.
The hashmap looks like this after each query:
1 query: {1: 2}         insert 1, 2
2 query: {1: 4}         addToValue 2
3 query: answer is 4    get 1
4 query: {1: 4, 2: 3}   insert 2, 3
5 query: {2: 4, 3: 3}   addToKey 1
6 query: {2: 3, 3: 2}   addToValue -1
7 query: answer is 2    get 3
The sum of the results for all the get queries is equal to 4 + 2 = 6.
"""
​
​
def hashMap(queryType, query):
    # we want to build on top of pythons built in {}
    # we need our hashmap {}
    hash_map = {}
    # make helper functions for the different queries (get, insert, addToValue, addToKey)
    sum_of_gets = 0
    # iterate through queryType and query and call the corresponding helper functions
    for i in range(len(queryType)):
        method_name = queryType[i]
        parameters = query[i]
        # print(method_name, parameters)
        if method_name == "insert":
            hash_map = handle_insert(hash_map, parameters)
        elif method_name == "get":
            value = handle_get(hash_map, parameters)
            sum_of_gets += value
        elif method_name == "addToKey":
            hash_map = handle_add_to_key(hash_map, parameters)
        elif method_name == "addToValue":
            hash_map = handle_add_to_value(hash_map, parameters)
​
    return sum_of_gets
    # keep track of the sum of get queries
​
​
def handle_insert(hash_map, parameters):
    key = parameters[0]
    value = parameters[1]
    hash_map[key] = value
    return hash_map
​
​
def handle_get(hash_map, parameters):
    key = parameters[0]
    return hash_map[key]
​
​
def handle_add_to_key(hash_map, parameters):
    offset = parameters[0]
    # add `offset` to every key in hash_map
    # safer to create a new dictionary
    new_hash_map = {}
    # iterate through the keys and values in the old dictionary
    for key, value in hash_map.items():
        # add `offset` to the key and put it into the new dictionary
        new_key = key + offset
        new_hash_map[new_key] = value
    return new_hash_map
​
​
def handle_add_to_value(hash_map, parameters):
    offset = parameters[0]
    # we want to add offset to every value in hash_map
    for key, value in hash_map.items():
        new_value = value + offset
        hash_map[key] = new_value
    return hash_map
​
​
test_cases = [
    {"queryType": ["insert", "insert", "addToValue", "addToKey", "get"],
     "query": [[1, 2], [2, 3], [2], [1], [3]],
     "expected_output": 5},
    {"queryType": ["insert", "addToValue", "get", "insert", "addToKey", "addToValue", "get"],
     "query": [[1, 2], [2], [1], [2, 3], [1], [-1], [3]],
     "expected_output": 6},
    {"queryType": ["addToKey", "addToKey", "insert", "addToValue", "addToValue", "get", "addToKey", "insert",
                   "addToKey", "addToValue"],
     "query": [[-3], [-1], [0, -3], [3], [-1], [0], [-1], [-4, -5], [-1], [-4]],
     "expected_output": -1},
    {"queryType": ["insert", "insert", "addToKey", "addToKey", "addToKey", "insert", "addToValue", "addToKey",
                   "addToKey", "get"],
     "query": [[-5, -2], [2, 4], [-1], [-3], [1], [3, -2], [-4], [-2], [2], [-8]],
     "expected_output": -6},
    {"queryType": ["insert", "get", "insert", "addToValue", "addToValue", "addToValue", "insert", "addToKey", "get",
                   "insert"],
     "query": [[2, 1], [2], [1, 3], [-1], [0], [3], [4, -5], [3], [4], [1, 1]],
     "expected_output": 6},
    {"queryType": ["addToValue", "addToValue", "insert", "get", "addToKey", "insert", "insert", "insert", "addToValue",
          "addToKey"],
     "query": [[-5], [3], [3, -3], [3], [0], [-4, 2], [0, -3], [-2, 4], [2], [2]],
     "expected_output": -3},
    {"queryType": ["addToKey", "addToKey", "insert", "addToKey", "addToValue", "addToKey", "addToValue", "insert", "get",
          "insert"],
     "query": [[-1], [-3], [4, 3], [2], [2], [-2], [0], [-5, 3], [-5], [3, -4]],
     "expected_output": 3},
    {"queryType": ["insert", "insert", "insert", "get", "insert", "insert", "insert", "addToKey", "insert", "insert"],
     "query": [[3, -4], [-4, 3], [4, -3], [4], [-5, 0], [-2, -5], [2, 2], [1], [-5, -2], [1, 3]],
     "expected_output": -3},
    {"queryType": ["addToValue", "addToKey", "addToKey", "insert", "addToValue", "addToValue", "insert", "get", "get", "insert"],
     "query": [[-2], [-3], [0], [-3, 1], [-2], [-4], [2, -4], [2], [2], [3, -1]],
     "expected_output": -8}
]
​
​
for test_case in test_cases:
    query_type = test_case['queryType']
    query = test_case['query']
    print(f"Input:\nqueryType: {query_type}\nquery: {query}\nexpected_output: {test_case['expected_output']}")
    actual_output = hashMap(query_type, query)
    print(f"Actual output: {actual_output}")
    print("-----")