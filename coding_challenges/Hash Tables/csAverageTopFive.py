'''
Given a list of different students' scores, write a function that returns the average of each student's top five scores. You should return the averages in ascending order of the students' id numbers.

Each entry (scores[i]) has the student's id number (scores[i][0]) and the student's score (scores[i][1]). The averages should be calculated using integer division.

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The average student `1` is `87`.
The average of student `2` is `88.6`, but with integer division is `88`.
'''

# Approach 1
# def csAverageOfTopFive(scores):
#     # we count the number of students and we'll use it as a condition in our while loop
#     num_students = len(set([pair[0] for pair in scores]))
#     # will contain the final results
#     result = list()
#     # assuming student id starts at 1
#     i = 1
#     while i < num_students + 1:
#         # all these data structures will reset every iteration of this while loop
#         # will contain the id and average score of student
#         # this is what gets appended to result
#         final_list = []
#         # will contain the scores of each student
#         scores_arr = []
#         # we loop through the scores array
#         for j in range(len(scores)):
#             # self explanatory
#             student = scores[j][0]
#             score = scores[j][1]
#             # if student is i (which is the current student we're evaluating)
#             if student == i:
#                 # we append the score of that student to our array
#                 scores_arr.append(score)
#         scores_arr.sort(reverse=True)
#         # we check if the scores is at least 5
#         if len(scores_arr) >= 5:
#             sum_it = sum(scores_arr[0:5]) // 5
#         # if it's not, the average will be the sum of scores divided by the number of scores available
#         else:
#             sum_it = sum(scores_arr) // len(scores_arr)
#         final_list = [i, sum_it]
#         result.append(final_list)
#         i += 1
#     return result

# Approach 2
# def csAverageOfTopFive(scores):
    # Initial thoughts:
    # Create a list of scores for each key(student)
    # sort the list starting with highest value to lowest
    # cutting off at 5
    # add all 5 scores together and divide by 5 for average
    # Create a second list to store the arrays

    # scores_arr = []
    # student_set = set()
    # student_list = []
    # average_score = []
    # final_list = []
    # for i in range(len(scores) - 1):
    #     student = scores[i][0]
    #     score = scores[i][1]
    #     student_set.add(student)
    #     student_list = list(student_set)
    #     if student == student_list[0]:
    #         scores_arr.append(score)
    # scores_arr.sort(reverse=True)
    # print(scores_arr)
    # sum_it = sum(scores_arr[0:5]) // 5
    # average_score.append(sum_it)
    # print(student_list, average_score)
    # final_list = list(zip(student_list, average_score))
    # print(final_list)

# Approach 3 with hash tables/dictionaries
