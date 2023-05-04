

Then use the `check()` and `robot.move()` functions, as in the other programs. For example,

```
# shelf-place: pick up the block and place it at the target location
def shelf_place(robot):
    if check("the robot's gripper is not vertically aligned with the block"):
        robot.put("the gripper above the block")
    if check("the robot's gripper is vertically aligned with the block"):
        robot.put("the gripper above the block")
```

and so on. Please use proper spelling and punctuation, including all necessary quotes, parentheses, and other punctuation marks.

--

This completes the tutorial. Thank you for your help!
'''

# shelf-place: pick up the block and place it at the target location
def shelf_place(robot):
    if check("the robot's gripper is not near the goal"):
        robot.slide("block left")
    if check("the block is near the target"):
        robot.push("block at goal")

# push: slide the puck to the target location
def push(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")

# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# window-close: slide the window closed to the right
def window_close(robot):
    if check("