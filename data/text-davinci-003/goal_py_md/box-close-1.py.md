

Here is the program:

```
# box-close: pick up the box lid and place it on the box
# def box_close(robot):
    # Steps:
    #  1. Put gripper above box lid
    #  2. Grab the box lid with the gripper
    #  3. Line the box lid up with the box
    #  4. Place the box lid down on the box
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.move_gripper("above the box lid")
    # If the box lid becomes left of the gripper, go back to putting the gripper
    # above the box lid.
    if check("the box lid is not left of the robot's gripper and box lid is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the box lid", close_gripper=True)
    # As long the gripper is still mostly around the box lid, line up the box
    # lid with the box.
    if check("box lid is horizontally aligned with box"):
        robot.move_gripper("above the box lid")
    # If the box lid is lined up with the box to the side, place it down on the
    # box.
    if check("the robot's gripper is forward aligned with the box lid and the box lid is not horizontally aligned with box"):
        robot.move_gripper("horizontally aligned with box", close_gripper=False)