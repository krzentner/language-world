
    # Steps:
    #  1. Line up the gripper from above
    #  2. Rotate the gripper
    # First, line up the gripper as seen from above.
    if check("the robot's gripper is not vertically aligned with door dial"):
        robot.move_gripper("vertically aligned with the door dial", close_gripper=True)
    # Once the gripper is lined up with the door handle, we should be able to
    # rotate it.
    if check("the robot's gripper is vertically aligned with door dial"):
        robot.move_gripper("around the door dial", close_gripper=True)

# button-press-side: push the button from the left or right
def button_press_side(robot):
    # Steps:
    #  1. Line up the gripper from the side
    #  2. Push the button
    # Because this is "side", we just need to line up the gripper from the side.
    # Line up the robot's gripper from the side.
    if check("the robot's gripper is not horizontally aligned with button"):
        robot.move_gripper("horizontally aligned with the button", close_gripper=True)
    # Once the gripper is lined up from the side, we should be able to push the
    # button
    if check("the robot's gripper is horizontally aligned with button"):
        robot.move_gripper("near the button")

def get_task_list(task_name):
    if task_name == "window-close":
        return [window_close]
    if task_name == "door-close":
        return [door_close]
    if task_name == "drawer-close":
        return [drawer_close]
    if task_name == "push":
        return [push]
    if task_name == "reach":
        return [reach]
    if task_name == "pick-place":
        return [pick_place]
    if task_name == "drawer-open":
        return [drawer_open]
    if task_name == "door-open":
        return [door_open]
    if task_name == "door-lock":
        return [door_lock]
    if task_name == "peg-insert-side