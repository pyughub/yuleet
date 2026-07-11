# input
integer array temperatures, daily temperatures in order

# output
array answer, where answer[i] is the number of days after day i until a warmer temperature; use 0 if none

# steps
1. use a stack to store indices of days still waiting for a warmer day
2. iterate through temperatures; when the current day is warmer than the day at the stack top, pop and set answer[popped] = current index - popped index
3. push the current index onto the stack
4. days left on the stack have no warmer day ahead, so their answer stays 0

# requirements
1. write a python function, test it yourself, and put the code into daily_temperatures.py
2. start with: def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
