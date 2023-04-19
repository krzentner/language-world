
    # Steps:
    #  1. Put gripper above dial
    #  2. Turn the dial counterclockwise
    #  3. Check if the door has unlocked
    # Put the gripper above the dial so that we can turn it.
    if check("the robot's gripper is not above the dial"):
        robot.put("gripper above dial")
    # Once we have the gripper lined up above the dial, turn the dial
    # counterclockwise.
    if check("the robot's gripper is above the dial"):
        robot.rotate("dial counterclockwise")
    # After turning the dial, try to open the door. 
    # If the door is unlocked, continue to the next task.
    if check("the door is unlocked"):
        return true