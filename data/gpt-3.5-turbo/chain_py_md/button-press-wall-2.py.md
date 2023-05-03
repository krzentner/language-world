# button-press-wall: push the button from the front with a short wall in the way
def button_press_wall(robot):
    # Steps:
    #   1. Move the gripper to the left of the wall, facing the button
    #   2. Move the gripper forward until it reaches the wall
    #   3. Move the gripper slightly up to be above the button
    #   4. Close the gripper around the button, pushing it at the wall
    #   5. Move the gripper slightly down to release the button
    
    # Move the gripper left of the wall, facing the button
    if check("the robot's gripper is not left of the wall"):
        robot.move("gripper to left of wall")
    
    # Move the gripper forward until it reaches the wall
    if check("the robot's gripper is not touching the wall"):
        robot.slide("gripper towards the wall")
    
    # Move the gripper slightly up to be above the button
    if check("the robot's gripper is not above the button"):
        robot.move("gripper slightly up")
    
    # Close the gripper around the button, pushing it at the wall
    if check("the robot's gripper is not holding the button"):
        robot.close("gripper around button")
        robot.push("button at the wall")
    
    # Move the gripper slightly down to release the button
    if check("the robot's gripper is holding the button"):
        robot.move("gripper slightly down")
        robot.open("gripper")