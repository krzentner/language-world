# pick-place: pick up the puck and hold it at the target location
# def pick_place(robot):
    # Steps:
    #  1. Put gripper roughly above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above the puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper is not around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing the gripper.
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    # We closed the gripper, and the puck is still near the gripper, so maybe we grabbed it.
    # Hold the puck in place and move it to the goal
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.slide("the puck to the goal")