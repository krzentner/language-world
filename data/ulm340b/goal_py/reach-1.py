
    # Steps:
    #  1. Put gripper near the target location
    # Just move the gripper to the target location.
    if check("the robot's gripper is not near the target location"):
        robot.move_gripper("near the target location")

# lever-pull: reach to the target location
def lever_pull(robot):
    # Steps:
    #  1. Line up the gripper above the left side of the lever
    #  2. Push down the left side of the lever
    # Line up the robot's gripper from above to push down on the lever.
    # Line up the gripper from above.
    # Because the lever is a long object, we should check if the gripper is lined
    # up with the front of the lever.
    # We're looking at the lever's left side.
    if check("the robot's gripper is not vertically aligned with lever and lever is not forward aligned with the robot's gripper"):
        robot.move_gripper("vertically aligned with the lever")
    # If the lever is mostly lined up, we can just close the gripper to push
    # down on it.
    if check("lever is left of the robot's gripper and the robot's gripper is forward aligned with lever"):
        robot.move_gripper("near lever", close_gripper=True)

# knob-pull: reach to the target location
def knob_pull(robot):
    # Steps:
    #  1. Line up the gripper above the doorknob
    #  2. Push down on the doorknob
    # Line up the robot's gripper from above to push down on the doorknob.
    # Line up the gripper from above.
    # Because the doorknob is a long object, we should check if the gripper is
    # lined up with the front of the doorknob.
    if check("the robot's gripper is not vertically aligned with doorknob and doorknob is not forward aligned with the robot's gripper"):
        robot.move_gripper("vertically aligned with the doorknob")
    # If the doorknob is lined up, we can just close the gripper to push down on
    # it.
    if check("doorknob is left of the robot's gripper and the robot's gripper is forward