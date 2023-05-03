
    # Steps:
    #  1. Put gripper above plate
    #  2. Push the plate in the direction of the goal
    #  3. Slide the plate in the direction of the goal
    # If the robot's gripper is not above the plate, move it above the plate.
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above the plate")
    # If the robot's gripper is above the plate, start pushing the plate in the
    # direction of the goal.
    if check("the robot's gripper is above the plate"):
        robot.push("plate to the goal")
    # If the plate is starting to move, give it more force in the direction of
    # the goal.
    if check("the plate is moving towards the goal"):
        robot.slide("plate to the goal")