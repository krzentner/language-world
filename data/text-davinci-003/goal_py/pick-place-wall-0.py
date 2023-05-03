
    # Steps:
    #  1. Put gripper slightly to the side of the puck
    #  2. Reach past wall to grab puck
    #  3. Lift puck above wall
    #  4. Move puck to target location
    # Because there is a wall in between the puck and the target location, we
    # need to first build up a bit of momentum with the gripper.
    # Put the gripper slightly to the side of the puck, so that when the gripper
    # reaches past the wall it can grab the puck.
    if check("the robot's gripper is not to the side of the puck"):
        robot.move_gripper("to the side of the puck")
    # Once the gripper is close to the puck, reach past the wall to grab it.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.move_gripper("around the puck", close_gripper=True)
    # Lift the puck a bit, so that it is above the wall.
    if check("the robot's gripper is closed around puck and the puck is below the robot's gripper"):
        robot.move_gripper("above the wall")
    # Once the puck is clear of the wall, move it to the target location.
    if check("the robot's gripper is above the wall"):
        robot.move_gripper("near the target location")