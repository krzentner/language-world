# door-unlock: turn the dial on the door
# def door_unlock(robot):

# Steps:
#  1. Move the gripper above the knob
#  2. Turn the knob to the right
#  3. Turn the knob to the left
#  4. Turn the knob to the right again to unlock the door


# Move the gripper above the knob
if check("the robot's gripper is not above the doorknob"):
    robot.move_gripper("above the doorknob")


# Turn the knob to the right
if check("the door is still locked"):
    robot.move_gripper("around the knob", close_gripper=True)
    robot.rotate_wrist("right", degrees=180)

# Turn the knob to the left
if check("the door is still locked"):
    robot.rotate_wrist("left", degrees=180)

# Turn the knob to the right again to unlock the door
if check("the door is still locked"):
    robot.rotate_wrist("right", degrees=180)