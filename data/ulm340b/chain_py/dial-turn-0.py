
    # Steps:
    #  1. Put gripper above the dial
    #  2. Put the gripper around the dial
    #  3. Turn the dial
    # First, put the gripper above the dial.
    if check("the robot's gripper is not above the dial"):
        robot.put("gripper above dial")
    # If the gripper is above the dial but not around it, go around the dial.
    if check("the robot's gripper is above the dial and the robot's gripper is not around the dial"):
        robot.put("gripper around dial")
    # If the gripper is around the dial, turn it.
    if check("the robot's gripper is around the dial"):
        robot.turn("the dial")

# hook-hang: hang an object on the hook
def hook_hang(robot):
    # Steps:
    #  1. Put gripper above the hook
    #  2. Put gripper around the hook
    #  3. Drop object onto the hook
    # First, put the gripper above the hook.
    if check("the robot's gripper is not above the hook"):
        robot.put("gripper above the hook")
    # If the gripper is not above the hook, try going above the hook again.
    if check("the robot's gripper is not above the hook"):
        robot.put("gripper above the hook")
    # If the gripper is not above the hook, give up.
    if check("the robot's gripper is not above the hook"):
        robot.give("up")
    # If the gripper is above the hook, put the gripper around the hook.
    if check("the robot's gripper is above the hook"):
        robot.put("gripper around hook")
    # If the gripper is not around the hook, try putting the gripper around the
    # hook again.
    if check("the robot's gripper is not around the hook"):
        robot.put("gripper around hook")
    # If the gripper is not around the hook, give up.
    if check("the robot's gripper is not around the hook"):
        robot.give("up")
    # If the gripper is around the hook, release the