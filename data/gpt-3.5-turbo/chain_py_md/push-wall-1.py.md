# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    #  4. If wall is encountered: lift gripper, reach target location, put gripper down, slide puck to goal
    
    # First, put the gripper roughly above the puck so that we don't bump it while trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    
    # If the gripper is aligned with the puck but not near it, move the gripper down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    
    # If the gripper is near the puck, we've probably trapped the puck and can slide it to the target location.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        try:
            robot.slide("the puck to the goal")
        except:
            # In case the wall is encountered, lift the gripper and reach the target location.
            if check("the wall is blocking the puck"):
                robot.lift("gripper")
                robot.reach("to goal")
                robot.place("gripper down")
                robot.slide("the puck to the goal")