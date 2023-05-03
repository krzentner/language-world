

# hammer: hit the nail with the hammer
def hammer(robot):
    # Steps:
        #  1. Put gripper above the hammer
        #  2. Grab the hammer
        #  3. Line up the hammer with the nail
        #  4. Hit the nail with the hammer
    
    # First, put the gripper above the hammer.
    if check("the robot's gripper is not above the hammer"):
        robot.put("gripper above hammer")
    # As long as the grip is not around the hammer, close it to grab the hammer.
    if check("the robot's gripper is not around hammer and the robot's gripper is open"):
        robot.close("gripper around hammer")
    # As long as the hammer is not horizontally aligned with the nail,
    # adjust the orientation of the gripper to line it up with the nail.
    if check("the hammer is not horizontally aligned with the nail"):
        robot.align("hammer to nail")
    # When the hammer is aligned with the nail, use the gripper to hit the nail.
    if check("the hammer is horizontally aligned with the nail"):
        robot.hit("nail with hammer")