# input
1. integer numCourses, the number of courses
2. array prerequisites (made of two-element arrays `[course, prereq]`, meaning `course` requires `prereq`)

# output
boolean value (whether able to finish all courses)

# steps
1. build a directed graph: for each `[course, prereq]`, add an edge `prereq -> course`
2. assign each course a state: `0` = unvisited, `1` = visiting (on current DFS path), `2` = finished
3. for each course from `0` to `numCourses - 1`, if it is unvisited, run DFS (`dfs`); if DFS returns `false`, return `false`
4. during DFS on a course:
   - mark it as visiting (`1`)
   - for each neighbor (courses that depend on it), if a neighbor is visiting, a cycle exists → return `false`
   - if a neighbor is unvisited, recurse into it; if that recursion returns `false`, return `false`
   - after exploring all neighbors, mark the course as finished (`2`) and return `true`
5. if every course completes DFS without finding a cycle, return `true`

# requirements
1. write a python function, test it yourself, and put the code into course_schedule.py
2. start with: def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
