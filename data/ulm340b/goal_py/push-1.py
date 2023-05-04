
    # Steps:
    #  1. Put gripper in front of puck
    #  2. Slide puck to the target location
    # In order to push the puck, put the gripper in front of it.
    if check("the robot's gripper is not right of the puck"):
        robot.move_gripper("near the puck", close_gripper=True)
    # Once we're in front of the puck, slide it toward the target location.
    if check("the puck is right of the robot's gripper"):
        robot.move_gripper("above the puck")

# slide-back: slide the target object left, back to its starting position
def slide_back(robot):
    # Steps:
    #  1. Put gripper behind target
    #  2. Slide the target object to the left
    # As long as the target object is still in front of the robot's gripper, put
    # the gripper behind the object.
    if check("the robot's gripper is right of target"):
        robot.move_gripper("around target")
    # Now that the gripper is behind the object, move it to the left to push the
    # target object.
    if check("the robot's gripper is left of target"):
        robot.move_gripper("forward aligned with target")

# slide: slide the target object right
def slide(robot):
    # Steps:
    #  1. Put gripper behind target
    #  2. Slide the target object to the right
    # As long as the target object is still in front of the robot's gripper, put
    # the gripper behind the object.
    if check("the robot's gripper is right of target"):
        robot.move_gripper("around target")
    # Now that the gripper is behind the object, move it to the right to push the
    # target object.
    if check("the robot's gripper is left of target"):
        robot.move_gripper("forward aligned with target")

# slide-back-side: slide the target object left, back to its starting position
def slide_back_side(robot):
    # Steps:
    #  1. Put gripper left of the target object
    #  2. Grab the target object