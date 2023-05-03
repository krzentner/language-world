

The idea is to approach the wall from the side, with the robot's gripper lined up with the button. Then, the robot should move close to the wall, such that it can use the wall to keep the gripper in place while it pushes. 

# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    # Steps:
    #  1. Line up the gripper as viewed from the side
    #  2. Move close to the wall
    #  3. Push against the wall to press the button
    # First, the gripper needs to be lined up with the button, as viewed from the side.
    if check("the robot's gripper is not laterally aligned with button"):
        robot.put("gripper alongside button")
    # If the gripper is now lined up with the button, move close to the short wall.
    if check("the robot's gripper is laterally aligned with button and the robot's gripper is not near the wall"):
        robot.move("gripper near wall")
    # Once the robot's gripper is near the wall and lined up with the button, the robot should push against the wall to press the button
    if check("the robot's gripper is near the wall and the robot's gripper is laterally aligned with button"):
        robot.push("against wall, pressing button")