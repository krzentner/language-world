
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with coffee button"):
        robot.put("gripper above coffee button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with coffee button"):
        robot.push("down on button")

# push-left: push the large object to the left
def push_left(robot):
    # Steps:
    #  1. Put gripper right of the door handle
    #  2. Start pushing against the door handle to close the door
    #  3. Push the door closed harder
    # If the the door handle is left of the robot's gripper, we should move the
    # gripper near the door handle to start pushing
    if check("the door handle is left of the robot's gripper and the robot's gripper is not near the door handle"):
        robot.move("gripper to right of door handle")
    # If the robot's gripper is near the door handle we can probably slide the
    # door closed now by moving the gripper left.
    if check("the robot's gripper is near the door handle"):
        robot.slide("the door left")
    # If the robot's gripper is starting to be in front of the door handle,
    # push harder.
    if check("the robot's gripper is in front of the door handle"):
        robot.push("the door left harder")

# pick-place-simple: pick up the ball and hold it at the target location
def pick_place_simple(robot):
    # Steps:
    #  1. Put gripper above ball
    #  2. Grab ball with the gripper
    #  3. Move ball to goal
    # First, put the gripper roughly above ball, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the ball"):
        robot