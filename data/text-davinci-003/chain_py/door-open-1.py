
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # Because the door handle is a long object, lined up with the door, we can't
    # just move the gripper near it. We have to be more precise about it.
    # Put the gripper above the door handle.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # Now that the gripper is above the door handle, we can move it around the
    # door handle.
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    # Once the gripper is around the door handle, we can just pull the door open.
    if check("the robot's gripper is around door handle"):
        robot.pull("away from door")

# grab-hook: grab the hook from the side
def grab_hook(robot):
    # Steps:
    #  1. Put gripper above hook
    #  2. Hook gripper under the hook
    # Put the gripper above the hook.
    if check("the robot's gripper is not vertically aligned with hook"):
        robot.put("gripper above hook")
    # We want to hook the gripper under the hook so we can control it.
    # For that, we need to move the gripper to the side.
    if check("the robot's gripper is vertically aligned with hook and the robot's gripper is missing hook"):
        robot.hook("gripper under hook")
    # Now the gripper should be hooked under the hook!
    if check("the robot's gripper is hooked under hook"):
        robot.grab("hook")