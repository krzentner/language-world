

The steps will be:
1. Put gripper above the puck
2. Push gripper into top of the puck
3. Move the puck until the wall is lined up with the robot's gripper 
4. Push against the wall while pushing the puck forward with the robot's gripper
5. Slide the puck to the target location

# push-wall: slide the puck to the target location with a small wall in the way
def push_wall(robot):
    # Steps:
    #  1. Put gripper above the puck
    #  2. Push gripper into top of the puck
    #  3. Move the puck until the wall is lined up with the robot's gripper 
    #  4. Push against the wall while pushing the puck forward with the robot's gripper
    #  5. Slide the puck to the target location
    # First, put the gripper above the puck, to avoid bumping it while trying to
    # push it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is aligned with the puck, move it until the wall is lined up
    # with the gripper from the front.
    if check("the robot's gripper is vertically aligned with the puck and the wall is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the wall")
    # Now that the wall is lined up with the gripper, slowly push against it to
    # move the puck away from the wall.
    if check("the wall is forward aligned with the robot's gripper"):
        robot.move_gripper("above the target location")
    # Once the puck has cleared the wall, move it to the target location.
    if check("the robot's gripper is near the target location"):
        robot.move_gripper("above the puck")