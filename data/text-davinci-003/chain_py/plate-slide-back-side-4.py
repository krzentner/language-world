
    # Steps:
    #  1. Put gripper above backwards edge of plate
    #  2. Grab onto backwards edge of plate
    #  3. Slide plate sideways backwards
    #  4. Slide plate sidewards back to goal
    # If the robot's gripper isn't near the back edge of the plate, we have to move
    # the gripper to the back edge of the plate while keeping it pointed up.
    # We don't need to be careful about the direction, since the plate is large
    # and we're just sliding it.
    if check("the robot's gripper is not near the back of the plate and the robot's gripper is pointing up"):
        robot.move("the gripper to the back edge of the plate")
    # When the gripper is near the back edge of the plate, move it over the plate
    # so that we can slide it.
    if check("the robot's gripper is near the back edge of the plate and the robot's gripper is pointing up"):
        robot.grab("the back edge of the plate")
    # If the robot's gripper is now holding onto the back edge of the plate, we
    # can slide it sideways back.
    # Keep doing this until the plate is above the goal.
    if check("the robot's gripper is holding onto the back edge of the plate and the plate is not horizontally aligned with the goal"):
        robot.slide("the plate backwards")
    # Push the plate sideways back until it's at the goal. 
    if check("the plate is horizontally aligned with the goal"):
        robot.place("the plate at the goal")