# Chandrayaan-3
TDD Assesment for Incubyte

Starting Position: (0, 0, 0)

Initial Direction: N

There are 9 test cases shown in this program in the file test_translator.py

Test Case 1:
Just checking the function default when we pass translator(0, 0, 0, "N")
the values are correctly initialized as x = 0, y = 0, z = 0, direction = "N"

Test Case 2:
if f(forward):
then (0, 1, 0)

Test Case 3:
if b(backward):
then (0, -1, 0)

Test Case 4:
if l(left):
  if direction is North : 
    Direction = West
  else if direction is South : 
    Direction = East
  else if direction is East : 
    Direction = North
  else if direction is West : 
    Direction = South

Test Case 5:
if r(right):
  if direction is North : 
    Direction = East
  else if direction is South : 
    Direction = West
  else if direction is East : 
    Direction = South
  else if direction is West : 
    Direction = North

Test Case 6:
if u(upwards):
  Direction = Upwards

Test Case 7:
if d(downwards):
  Direction = Downwards

Test Case 8:
Move multiple steps
1 f(Move 1 times forward)
2 b(Move 2 times backward)
initial = (0, 0, 0)
Step 1 - (0, 1, 0)
Step 2 - (0, 0, 0)
Step 3 - (0, -1, 0)
output = (0, -1, 0)

Test Case 9:
The given example as an array
[ "f", "r", "u", "b", "l" ]
“f” - (0, 1, 0) - N
“r” - (0, 1, 0) - E
“u” - (0, 1, 0) - U
“b” - (0, 1, -1) - U
“l” - (0, 1, -1) - N
Final Position: (0, 1, -1)
Final Direction: N

All 9 Test Cases passed succesfully
Extract and keep both the files translator.py and test_translator.py in same folder
Run the file test_translator.py by the command "python -u test_translator.py"

It will show
----------------------------------------------------------------------
Ran 9 tests in 0.001s
Happy Coding!!!😊
