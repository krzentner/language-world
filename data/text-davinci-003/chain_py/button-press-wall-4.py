
    # Steps:
    #  1. Put gripper near the wall
    #  2. Line up gripper to the button as seen from the side
    #  3. Push the button from the wall 
    # If the the robot's gripper is not near the wall, we should move the gripper
    # near the wall to start pushing
    if check("the robot's gripper is not near wall"):
        robot.move("gripper to near wall")
    # Line up the gripper with the button as seen from the side. 
    if check("the robot's gripper is near the wall and the robot's gripper is not side aligned with the button"):
        robot.align("gripper to button side")
    # If the the robot's gripper is now lined up with the button as seen from
    # the side and the wall is still between them, push the button.
    if check("the robot's gripper is side aligned with the button and the wall is between robot's gripper and button"):
        robot.push("button from wall")