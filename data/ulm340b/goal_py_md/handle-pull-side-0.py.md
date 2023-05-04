

Here are some more useful commands to know:

* `robot.gripper_pos()` returns the position of the robot's gripper in the
  form `[x, y, z]`, measured relative to the floor and the front wall.
* `robot.gripper_angle()` returns the angle of the robot's gripper in degrees.
  (0 degrees is horizontal, parallel to the table, and the gripper opens away
  from the robot.)
* `robot.is_closed()` returns a Boolean indicating whether the gripper is
  closed.
* `robot.close_gripper()` moves the gripper towards the robot to close it.
  You can use this to close the gripper slightly.

You should put your commands after the text `handle_pull_side(robot):` and before the text `if check(...):`

When you have finished your program, please click the 'Submit' button.
"""


def handle_pull_side(robot):
    if check("the robot's gripper is not vertically aligned with the handle and the robot's gripper is open and the handle is above the robot's gripper"):
        robot.move_gripper("above the handle", close_gripper=True)
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is open and the handle is above the robot's gripper"):
        robot.move_gripper("forward aligned with the handle", close_gripper=True)
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is open and the handle is above the robot's gripper"):
        robot.move_gripper("vertically aligned with the handle", close_gripper=True)
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is open and the handle is above the robot's gripper"):
        robot.move_gripper("around the handle", close_gripper=True)
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is open and the handle is above the robot's gripper"):
        robot.move_gripper("around the handle", close_gripper=True)
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is open and the handle is above the robot's gripper"):
        robot.move_gripper("forward aligned with the handle")


# ================================
# Start of code