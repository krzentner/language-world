

Steps: 
1. Move the gripper to the short wall that is near the button
2. Lower the gripper to the wall in line with the button
3. Push the button from the side of the short wall

Solution:
```
# button-press-wall: push the button from the front with a short wall in the way
# def button_press_wall(robot):
    # Steps:
    #  1. Move the gripper to the short wall that is near the button
    #  2. Lower the gripper to the wall in line with the button
    #  3. Push the button from the side of the short wall
    if check("the robot's gripper is not near the short wall"):
        robot.move_gripper("near the short wall")
    # If the gripper is near the short wall, lower it to the wall in line with
    # the button.
    if check("the robot's gripper is in line with the button"):
        robot.move_gripper("in line with the button", close_gripper=True)
    # If the gripper is in line with the button (as viewed from the side) we
    # can push the buton by moving the gripper left.
    if check("the robot's gripper is in line with the button and the robot's gripper is not near the button"):
        robot.move_gripper("left of the button")