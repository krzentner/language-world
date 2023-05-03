# push-wall: slide the puck to the target location with a small wall in the way
# def push_wall(robot):
    # Steps:
    #  1. Put gripper above the puck, to the side of the wall
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # First, check if the gripper is on the left side of the wall. If not, move it there.
    if check("the robot's gripper is not left of the wall"):
        robot.move_gripper("left of the wall")
    # If the gripper is not in position above the puck, move it there.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck but the robot's gripper is not near puck"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and the puck is below the robot's gripper, approach the wall.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move_gripper("against the wall")
    # If the gripper is against the wall, push the puck until it is past the wall.
    if check("the robot's gripper is against the wall and the puck is not past the wall"):
        robot.move_gripper("past the wall", close_gripper=True)
    # If the puck is past the wall, slide it to the target location.
    if check("the puck is past the wall"):
        robot.move_gripper("above the target location")