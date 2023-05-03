

then add the instructions to complete the task.

```
# dial-turn: turn the dial
def dial_turn(robot):
    if check("the robot's gripper is not above the dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is not around the dial and the robot's gripper is open"):
        robot.grab("dial")
    if check("the robot's gripper is around the dial"):
        robot.turn("dial to the desired position")