

The program should look like this: 

```
# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    # Steps:
    #  1. Line up the gripper with the peg as if it were above
    #  2. Push the gripper downwards and catch the peg 
    #  3. Close the gripper around the peg
    #  4. Move the peg to the goal location
    # First, line up the gripper with the peg as if it were above.
    if check("the robot's gripper is not vertically aligned above the peg"):
        robot.put("gripper above peg")
    # Now that the gripper is lined up, push downwards to the hole to catch the
    # peg.
    if check("the robot's gripper is vertically aligned above the peg"):
        robot.push("downwards to catch peg")
    # Once the gripper is around the peg, close the gripper to make sure we
    # keep control of the peg.
    if check("the robot's gripper is around the peg and the robot's gripper is open"):
        robot.close("gripper around peg")
    # We closed the gripper and the peg is still near the gripper, so maybe we
    # grabbed it.
    # Try to move the peg to the goal.
    # If we didn't grab it, just go back to the earlier step.
    if check("the robot's gripper is around peg and the peg is below the robot's gripper"):
        robot.place("peg at goal")
```