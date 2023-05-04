
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull up handle
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # If the gripper is aligned above the handle, drop it down around the
    # handle.
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.put("gripper around handle")
    # As long as the handle is still lined up vertically, we can pull it up by
    # moving the robot's gripper up.
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.lift("the handle")

# lever-pull: pull the lever up
def lever_pull(robot):
    # Steps:
    #  1. Put gripper above lever
    #  2. Drop gripper around lever
    #  3. Pull up the lever
    # First, put the gripper above the lever.
    if check("the robot's gripper is not vertically aligned with lever"):
        robot.put("gripper above lever")
    # If the gripper is aligned above the lever, drop it down around the lever.
    if check("the robot's gripper is vertically aligned with lever"):
        robot.put("gripper around lever")
    # As long as the lever is still lined up vertically, we can pull it up by
    # moving the robot's gripper up.
    if check("the robot's gripper is vertically aligned with lever"):
        robot.lift("the lever")

# light-switch-right: flip the light switch to the right
def light_switch_right(robot):
    # Steps:
    #  1. Put gripper to left of the light switch
    #  2. Push light switch to the right
    # First, put the gripper to left of the light switch.
    if check("the robot's gripper is not left of the light switch"):
        robot.put("gripper to left of the light switch")
    # If the robot's gripper is left of the light switch, we can probably flip it
  