from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph: dict[int, list[int]] = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # 0 = unvisited, 1 = visiting (on current path), 2 = finished
        state = [0] * numCourses

        def dfs(course: int) -> bool:
            state[course] = 1
            for next_course in graph[course]:
                if state[next_course] == 1:
                    return False
                if state[next_course] == 0 and not dfs(next_course):
                    return False
            state[course] = 2
            return True

        for course in range(numCourses):
            if state[course] == 0 and not dfs(course):
                return False

        return True

    def canFinish_kahn(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        taken = 0

        while queue:
            course = queue.popleft()
            taken += 1
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return taken == numCourses


def load_testcase(path: str) -> tuple[int, list[list[int]], bool]:
    import ast

    lines = open(path, encoding="utf-8").read().strip().splitlines()
    num_courses_str, prerequisites_str = lines[0].split("input:", 1)[1].strip().split(";", 1)
    expected = lines[1].split("output:", 1)[1].strip().lower() == "true"
    return int(num_courses_str), ast.literal_eval(prerequisites_str), expected


if __name__ == "__main__":
    solution = Solution()

    tests = [
        {"numCourses": 2, "prerequisites": [[1, 0]], "expected": True},
        {"numCourses": 2, "prerequisites": [[1, 0], [0, 1]], "expected": False},
        {"numCourses": 3, "prerequisites": [[1, 0], [2, 1]], "expected": True},
        {"numCourses": 4, "prerequisites": [[1, 0], [2, 1], [3, 2]], "expected": True},
        {"numCourses": 4, "prerequisites": [[1, 0], [2, 0], [3, 1], [3, 2]], "expected": True},
        {"numCourses": 1, "prerequisites": [], "expected": True},
        {"numCourses": 3, "prerequisites": [[0, 1], [1, 2], [2, 0]], "expected": False},
    ]

    num_courses, prerequisites, expected = load_testcase("course_schedule_testcase.txt")
    tests.append(
        {
            "numCourses": num_courses,
            "prerequisites": prerequisites,
            "expected": expected,
            "label": "course_schedule_testcase.txt",
        }
    )

    passed = 0
    for idx, test in enumerate(tests, 1):
        actual_dfs = solution.canFinish(test["numCourses"], test["prerequisites"])
        actual_kahn = solution.canFinish_kahn(test["numCourses"], test["prerequisites"])
        expected = test["expected"]
        ok = actual_dfs == expected and actual_kahn == expected
        passed += ok
        status = "OK" if ok else "FAIL"
        label = test.get("label", "")
        suffix = f"  ({label})" if label else ""
        print(
            f"[{idx}] {status}  numCourses={test['numCourses']}  "
            f"prerequisites={test['prerequisites']}  dfs={actual_dfs}  "
            f"kahn={actual_kahn}  expected={expected}{suffix}"
        )

    print(f"\n{passed}/{len(tests)} passed")
