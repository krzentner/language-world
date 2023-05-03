
    # Steps:
    #  1. Put gripper above puck
    #  2. Grab puck
    #  3. Move puck to target location
    #  4. Place puck
    # First, put the gripper near the puck so we can grab it.
    if check("the robot's gripper is not near the puck and the robot's gripper is not above the puck"):
        robot.put("gripper above puck")
    # Now that the gripper is near the puck, grab it.
    if check("the robot's gripper is near the puck and the robot's gripper is open"):
        robot.grab("puck")
    # Now that the puck is in the gripper, move it to the target location.
    if check("the puck is in the robot's gripper and the puck is not at the target location"):
        robot.move("puck to goal")
    # Now that the puck is at the target location, we can place it.
    if check("the puck is at the target location"):
        robot.place("puck")