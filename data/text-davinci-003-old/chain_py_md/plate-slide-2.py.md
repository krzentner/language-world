

Steps: 
 1. Put gripper below plate
 2. Push the plate onto the goal

# plate-slide: slide the plate into the target location
# def plate_slide(robot):
    # Steps:
    #  1. Put gripper below plate
    #  2. Push the plate onto the goal
    # First, put the gripper below the plate
    if check("the robot's gripper is not below plate"):
        robot.put("gripper below plate")
    # If the gripper is near the plate, we can start pushing it onto the goal.
    if check("the robot's gripper is near plate"):
        robot.push("plate onto goal")