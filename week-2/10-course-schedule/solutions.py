from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dict = defaultdict(list)

        for prerequisite in prerequisites:
            next_course, prev_course = prerequisite
            course_dict[prev_course].append(next_course)

        path = [False] * numCourses
        checked = [False] * numCourses

        for course in range(numCourses):
            if self.check_cycle(course, course_dict, checked, path):
                return False

        return True

    def check_cycle(self, course, course_dict, checked, path):

        if checked[course]:
            return False

        if path[course]:
            return True

        path[course] = True

        res = False
        for child in course_dict[course]:
            res = self.check_cycle(child, course_dict, checked, path)
            if res:
                break

        path[course] = False
        checked[course] = True
        return res
