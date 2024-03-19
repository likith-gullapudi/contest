from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        index = 0
        q = deque()
        for i in students:
            q.appendleft(i)
        while q:

            taken = False
            for i in range(len(q)):
                temp = q.pop()

                if temp == sandwiches[index]:
                    taken = True
                    index += 1
                    break
                else:
                    q.appendleft(temp)
            if not taken:
                return len(q)
        return 0

