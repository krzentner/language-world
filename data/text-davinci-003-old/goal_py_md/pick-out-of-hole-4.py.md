

Steps:
1. Put gripper directly above the peg 
2. Drop gripper around the peg 
3. Close gripper around peg 
4. Move peg out of the hole 
5. Move peg to target location 

```
# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
# def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper directly above the peg
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("directly above the peg")
    #  2. Drop gripper around the peg
    if check("the robot's gripper is above the peg and the robot's gripper is not around peg"):
        robot.move_gripper("around the peg", close_gripper=True)
    #  3. Close gripper around peg
    if check("the robot's gripper is around the peg and the robot's gripper is open"):
        robot.move_gripper("near the peg", close_gripper=True)
    #  4. Move peg out of the hole
    # To move the peg out of the hole, the robot can move the peg sideways.
    # Because the peg is in a hole, look at it from the front.
    if check("the robot's gripper is not forward aligned with the peg"):
        robot.move_gripper("forward aligned with the peg")
    # Move the peg out of the hole by moving the gripper to the left.
    if check("the robot's gripper is forward aligned with the peg"):
        robot.move_gripper("left of the peg")
    #  5. Move peg to target location
    if check("the peg is left of the robot's gripper"):
        robot.move_gripper("above target location")