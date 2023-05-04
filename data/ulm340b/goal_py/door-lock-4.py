
    # Steps:
    #  1. Put gripper above the door handle
    #  2. Move gripper over dial
    #  3. Turn the dial
    # First, put the gripper above the door handle.
    if check("the robot's gripper is not above the door handle"):
        robot.move_gripper("above the door handle")
    # Once the gripper is above the door handle, we should be able to move it
    # over the dial.
    if check("the robot's gripper is above the door handle"):
        robot.move_gripper("above the door handle", close_gripper=True)

# pick-place-wall: pick up the puck on the wall
def pick_place_wall(robot):
    # Steps:
    #  1. Put gripper above the puck
    #  2. Drop gripper around the puck
    #  3. Close gripper around the puck
    #  4. Move puck off wall
    #  5. Put puck at goal
    # First, put the gripper above the puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.move_gripper("above the puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around the puck and the robot's gripper is open"):
        robot.move_gripper("near the puck", close_gripper=True)
    # If the gripper is near the puck and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is near the puck and the robot's gripper is closed"):
        robot.move_gripper("above the puck")
    # If the gripper is above the puck and closed, we can probably move it to the
    # goal.
    if check("the robot's gripper is above the puck"):
        robot.move_gripper("almost vertically aligned with the puck")
    # If the gripper is aligned with the puck, we should move it off the wall.
    if check("the robot's gripper is forward aligned with the puck"):
        robot.