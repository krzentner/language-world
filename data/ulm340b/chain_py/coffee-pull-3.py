
    # Steps:
    #  1. Put gripper above the mug's handle
    #  2. Drop gripper around the mug's handle
    #  3. Pull the mug to the target location
    # First, put the gripper above the mug's handle.
    if check("the robot's gripper is not above the mug's handle"):
        robot.put("gripper above mug's handle")
    # If the mug's handle is not in the gripper's fingers, drop the gripper
    # around the mug's handle.
    if check("the robot's gripper is not around the mug's handle"):
        robot.grab("mug's handle")
    # If the gripper is around the mug's handle, pull the mug to the target
    # location.
    if check("the robot's gripper is around the mug's handle"):
        robot.pull("to goal")

# coffee-push: push the mug to the target location
def coffee_push(robot):
    # Steps:
    #  1. Put gripper above the mug's handle
    #  2. Push the mug's handle towards the target location
    # First, put the gripper above the mug's handle.
    if check("the robot's gripper is not above the mug's handle"):
        robot.put("gripper above mug's handle")
    # If the robot's gripper is above the mug's handle, push the mug's handle to
    # the target location.
    if check("the robot's gripper is above the mug's handle"):
        robot.push("to goal")

# lever-pull-side: pull the lever sideways to the side
def lever_pull_side(robot):
    # Steps:
    #  1. Put gripper above the lever
    #  2. Drop gripper around the lever
    #  3. Move the lever sideways
    # First, put the gripper above the lever.
    if check("the robot's gripper is not above the lever"):
        robot.put("gripper above lever")
    # If the lever is not in the gripper, move the gripper around the lever.
    if check("the robot's gripper is not around lever"):
       