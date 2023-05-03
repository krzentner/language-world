
    # Steps:
    #  1. Push the drawer towards the goal
    #  2. Release the drawer and let it close
    # We just need to push the drawer towards the goal.
    if check("the robot's gripper is not pushing the drawer away and the drawer is not at the goal"):
        robot.push("drawer away from robot")
    # Once the drawer is at the goal, we don't need to be pushing on it any
    # longer, so release the drawer and let it close.
    if check("the drawer is at the goal"):
        robot.release("drawer")