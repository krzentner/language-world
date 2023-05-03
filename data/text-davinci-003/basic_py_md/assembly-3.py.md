

Answer:
```
# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    if check("the robot's gripper is not above the wrench"):
        robot.put("gripper above wrench")
    if check("the robot's gripper is not around wrench"):
        robot.grab("wrench")
    if check("the robot's gripper is around wrench and the robot's gripper is not horizontally aligned with peg"):
        robot.align("gripper to peg")
    if check("the robot's gripper is horizontally aligned with peg"):
        robot.wrap("wrench around peg")
```