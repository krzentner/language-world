Here's the code for the `peg-insert-side` task:

```
# peg-insert-side: insert the peg into the hole from the side
# def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.move_gripper("vertically aligned with the peg")
    if check("the robot's gripper is not around the peg and the robot's gripper is open"):
        robot.move_gripper("near the peg", close_gripper=True)
    if check("the robot's gripper is around the peg and the peg is not horizontally aligned with the hole"):
        robot.move_gripper("horizontally aligned with the hole")
    if check("the robot's gripper is forward aligned with the peg and the peg is horizontally aligned with the hole"):
        robot.move_gripper("around the hole")
```