'''

There is a survey that consists of n questions where each question's answer is either 0 (no) or 1 (yes).

The survey was given to m students numbered from 0 to m - 1 and m mentors numbered from 0 to m - 1. The answers of the students are represented by a 2D integer array students where students[i] is an integer array that contains the answers of the ith student (0-indexed). The answers of the mentors are represented by a 2D integer array mentors where mentors[j] is an integer array that contains the answers of the jth mentor (0-indexed).

Each student will be assigned to one mentor, and each mentor will have one student assigned to them. The compatibility score of a student-mentor pair is the number of answers that are the same for both the student and the mentor.

For example, if the student's answers were [1, 0, 1] and the mentor's answers were [0, 0, 1], then their compatibility score is 2 because only the second and the third answers are the same.
You are tasked with finding the optimal student-mentor pairings to maximize the sum of the compatibility scores.

Given students and mentors, return the maximum compatibility score sum that can be achieved.



'''
test_case = [[[[1,1,0],[1,0,1],[0,0,1]],[[1,0,0],[0,0,1],[1,1,0]]],[[[0,0],[0,0],[0,0]],[[1,1],[1,1],[1,1]]]]




def maxCompatibilitySum(student,mentors):
    row,col = len(student), len(student[0])
    score_array = [0]*row
    def bk(i,j):
        if i >= row or j >= col:
            return
        count = 0
        for idx in range(col):
            if student[i][idx] == mentors[j][idx]:
                count+=1
        score_array[i] = max(score_array[i],count)
        bk(i+1,j)
        bk(i,j+1)
    bk(0,0)
    return sum(score_array)



for s,m in test_case:
    print(maxCompatibilitySum(s,m))
