# basketball: put the ball into the hoop
# def basketball(robot):
    # Welcome to the most exciting task of the day! Here's how we can make the robot shoot some hoops:
    #  1. Put the gripper above the ball
    #  2. Grab the ball with the gripper
    #  3. Move the gripper towards the hoop
    #  4. Release the ball
    #  5. Celebrate the winning shot!

    # First, we need to position the gripper above the ball. If it is not there already, move it.
    if check("the robot's gripper is not above the ball"):
        robot.move_gripper("above the ball")
    
    # Then, we can grab the ball by closing the gripper around it.
    if check("the robot's gripper is not around the ball"):
        robot.move_gripper("near the ball", close_gripper=True)

    # Next, we need to move the gripper towards the hoop. We need to be careful so that the ball doesn't hit the hoop and bounce off.
    if check("the robot's gripper is not near the hoop"):
        robot.move_gripper("over the hoop")
        robot.move_gripper("above the hoop")
        robot.move_gripper("almost vertically aligned with the hoop")
        robot.move_gripper("horizontally aligned with the hoop")

    # Once we're close enough, we can release the ball by opening the gripper.
    if check("the robot's gripper is not open and above the hoop"):
        robot.move_gripper("above the hoop", close_gripper=False)

    # Finally, let's celebrate the winning shot! 🏀🎉
    print("Yay, we made it!")