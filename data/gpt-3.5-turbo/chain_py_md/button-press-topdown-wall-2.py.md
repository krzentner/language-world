# button-press-topdown-wall: push the button down from above with a short wall in the way
def button_press_topdown_wall(robot):
    # Steps:
    #  1. Move the robot to the side of the wall
    #  2. Pivot the gripper over the wall
    #  3. Line up the gripper as viewed from above
    #  4. Push down on the button from the top
    # First, move the robot to the side of the wall.
    if check("the robot is not next to the wall"):
        robot.move("to the side of the wall")
    # Once the robot is beside the wall, pivot the gripper over it.
    if check("the robot is beside the wall and the gripper is not over the wall"):
        robot.pivot("the gripper over the wall")
    # Line up the robot's gripper from above since we're using the "topdown"
    # approach.
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.put("the gripper above button")
    # Push down on the button with the gripper.
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")