# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    # Steps:
    #  1. Put gripper above the button
    #  2. Move the gripper to the side of the wall
    #  3. Move the gripper towards the button
    #  4. Push down on the button
    # First, put the gripper roughly above the button.
    if check("the robot's gripper is not above the button"):
        robot.put("gripper above button")
    # If there is a wall in the way, move to the side of the wall before
    # moving the gripper towards the button.
    if check("there is a wall in the way of the robot's path to the button"):
        robot.move("gripper to side of wall")
    # Once the robot is beside the wall, move the gripper forward towards
    # the button.
    if check("the robot's gripper is not near the button"):
        robot.move("gripper towards button")
    # Finally, push down on the button.
    if check("the robot's gripper is near the button"):
        robot.push("down on button")