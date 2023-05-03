

Solution:

```
# dial-turn: turn the dial
def dial_turn(robot):
    # Steps:
    #  1. Put gripper in front of the dial
    #  2. Push the dial around
    # First, put the gripper in front of the dial.
    if check("the robot's gripper is not partially aligned with the dial"):
        robot.move_gripper("partially aligned with the dial", close_gripper=True)
    # If the gripper is lined up with the dial and not touching it, push the 
    # dial around.
    if check("the gripper is forward aligned with the dial"):
        robot.move_gripper("near the dial")