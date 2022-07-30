from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dict = defaultdict(list)

        for prerequisite in prerequisites:
            next_course, prev_course = prerequisite
            course_dict[prev_course].append(next_course)

        visited = [0 for _ in range(numCourses)]

        res = []
        for course in range(numCourses):
            res = self.dfs([], course, visited, course_dict)
            if not res:
                return []

        return res != None

    def dfs(self, res, course, visited, course_dict):
        if visited[course] == -1:  # Cycle detected
            return False

        if visited[course] == 1:
            return True

        visited[course] = -1

        for child in course_dict[course]:
            if not self.dfs(res, child, visited, course_dict):
                return False

        visited[course] = 1
        res.append(course)
        return res
