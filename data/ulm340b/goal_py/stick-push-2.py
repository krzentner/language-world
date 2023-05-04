
    # Steps:
    #  1. Put gripper above stick
    #  2. Grab stick
    #  3. Move stick to align with front of thermos
    #  4. Push stick forward to push thermos
    # First, put the gripper roughly above the stick.
    # We can be more careful about this later.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the stick is above the robot's gripper, the robot's gripper is
    # probably above the stick.
    # If the stick is vertically aligned with the robot's gripper, and the
    # gripper is open, we should be able to grab it by moving the gripper down.
    # We can be more careful about this later.
    if check("the stick is above the robot's gripper"):
        robot.move_gripper("almost vertically aligned with the stick", close_gripper=True)
    # If the gripper is aligned with the stick and closed, the gripper has
    # probably grabbed the stick and we can move the stick.
    if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is open"):
        robot.move_gripper("near the thermos")

# stick-pick-place: grab the stick and use it to push the puck to the target location
def stick_pick_place(robot):
    # Steps:
    #  1. Put gripper above stick
    #  2. Grab stick
    #  3. Put stick above puck
    #  4. Put stick around puck
    #  5. Push stick to close gripper around puck
    #  6. Push stick to slide puck
    # First, put the gripper roughly above the stick.
    # We can be more careful about this later.
    if check("the robot's gripper is not above the stick"):
        robot.move_gripper("above the stick")
    # If the stick is above the robot's gripper, the robot's gripper is
    # probably above the stick.
    # If the stick is vertically aligned with the robot's gripper, and the
    # gripper is open, we should be able to