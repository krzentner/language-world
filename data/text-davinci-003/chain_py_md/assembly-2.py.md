

The steps for assembly might look like this:

1. Put gripper over wrench 
2. Grab wrench with gripper 
3. Move wrench to the left side of the peg 
4. Rotate the wrench around the peg 

```
# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    # Steps:
    #  1. Put gripper over wrench
    #  2. Grab wrench with gripper
    #  3. Move wrench to the left side of the peg
    #  4. Rotate the wrench around the peg
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.put("gripper above wrench")
    # If the wrench is still above the robot's gripper, grab it.
    if check("the robot's gripper is vertically aligned with the wrench and the robot's gripper is open"):
        robot.grab("wrench with gripper")
    # Once the grip is on the wrench, move it to the left side of the peg.
    if check("the robot's gripper is near the wrench"):
        robot.move("wrench to the left side of the peg")
    # When the wrench is on the left side of the peg, wrap the wrench around the
    # peg by rotating it.
    if check("the robot's gripper is near the wrench and the wrench is on the left side of the peg"):
        robot.rotate("wrench around the peg")
```