
    # Steps:
    #  1. Move the gripper near the wall
    #  2. Move the gripper along the wall, over it
    #  3. Reach over the wall to the target location
    # First, move the robot's gripper near the wall.
    if check("the robot's gripper is not near the wall"):
        robot.move_gripper("near the wall")
    # Once we've found the wall, move the gripper along the wall until we're past
    # it.
    if check("the robot's gripper is near the wall"):
        robot.move_gripper("past the wall")
    # If we're past the wall, we've reached the target location.
    if check("the robot's gripper is past the wall"):
        robot.move_gripper("near reach target")

# push-back: slide the puck backwards a little so the robot has room to move
def push_back(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck backwards
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.move_gripper("vertically aligned with the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.move_gripper("above the puck", close_gripper=True)
    # If the gripper is near the puck, we've probably trapped the puck and can
    # slide it to the target location.
    # Close the gripper to make sure we keep control of the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.move_gripper("to