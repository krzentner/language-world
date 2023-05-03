# Steps:
    #  1. Put gripper above puck on the far side of the wall
    #  2. Grab the puck with the gripper
    #  3. Lift the gripper and puck over the wall
    #  4. Move the gripper to the target location
    #  5. Lower the gripper and release the puck
    # First, put the gripper above the puck on the far side of the short wall.
    if check("the robot's gripper is not above the puck and is not beyond the wall"):
        robot.place("gripper above puck beyond wall")
    # If the gripper is above the puck and not holding it, grab the puck.
    if check("the robot's gripper is above the puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is holding the puck, lift it over the wall to the target
    # location.
    if check("the robot's gripper is holding the puck and the puck is not at the target location"):
        robot.lift("gripper and puck over the wall and move to target location")
    # If the gripper and puck are at the target location, lower the gripper and
    # release the puck.
    if check("the robot's gripper and the puck are at the target location and the robot's gripper is holding the puck"):
        robot.place("puck at target location beyond wall")