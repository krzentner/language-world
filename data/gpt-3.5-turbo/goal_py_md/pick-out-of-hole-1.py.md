```
# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
# def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above the hole
    #  2. Grab the peg with the gripper
    #  3. Move the gripper up and out of the hole
    #  4. Line up the gripper with the target location
    #  5. Move the gripper to the target location
   
    # First, put the gripper above the hole.
    if check("the robot's gripper is not vertically aligned with the hole"):
        robot.move_gripper("vertically aligned with the hole")
    # Once the gripper is above the hole, put it around the peg.
    if check("the robot's gripper is above the hole and the robot's gripper is not around the peg"):
        robot.move_gripper("into the hole", close_gripper=True)
    # Now that the gripper holds the peg, move it up and out of the hole.
    if check("the robot's gripper is around the peg and not outside of the hole"):
        robot.move_gripper("above the hole")
    # Line up the gripper with the target location.
    if check("the robot's gripper is not above the target location"):
        robot.move_gripper("above the target location")
    # Finally, move the gripper to the target location.
    if check("the robot's gripper is above the target location and the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location", close_gripper=True)
```