

The robot should:

1. Put the gripper above the peg 
2. Drop the gripper around the peg 
3. Close the gripper around the peg 
4. Move the peg directly up from the hole, without rotating or turning it 

```
# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location
def pick_out_of_hole(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Drop gripper around peg
    #  3. Close gripper around peg
    #  4. Move peg directly up from the hole
    # First, put the gripper roughly above the peg, so that we don't bump it 
    # while trying to grab it.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # If the gripper isn't around the peg, put it around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.move_gripper("near the peg", close_gripper=True)
    # If the gripper is near the peg and open, maybe we can grab it by closing 
    # the gripper.
    if check("the robot's gripper is around the peg and the robot's gripper is closed"):
        robot.move_gripper("above the hole") 
    # Finally, move the peg directly up from the hole, without rotating or turning
    # it. 
    if check("the robot's gripper is above the hole"):
        robot.move_gripper("above the target location")
```