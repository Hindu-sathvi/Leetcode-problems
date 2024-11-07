#https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/?envType=problem-list-v2&envId=queue
#Code:
class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        students_queue = deque(students)
        s_index = 0 
        attempts = 0 
        while students_queue and attempts < len(students_queue):
            if students_queue[0] == sandwiches[s_index]:
                students_queue.popleft() 
                s_index += 1 
                attempts = 0 
            else:
                students_queue.append(students_queue.popleft())
                attempts += 1  

        return len(students_queue)
