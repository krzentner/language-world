
    # Steps:
    #  1. Move gripper to goal
    #  2. Stop and hold the gripper still at the target location
    # All we have to do is move the gripper to the goal.
    if check("the robot's gripper is not near the goal"):
        robot.move("gripper to goal")
    # Once we're near the goal, keep the gripper still.
    if check("the robot's gripper is near the goal"):
        robot.stop("gripper near goal")

# push-lever-button: push the lever to push the button
def push_lever_button(robot):
    # Steps:
    #  1. Put gripper above the lever
    #  2. Push the lever
    #  3. Push the lever harder
    # Because the lever is a large object, all we really need to do is put the
    # gripper above it, then push the lever.
    if check("the robot's gripper is not above the lever"):
        robot.put("gripper above the lever")
    # If the gripper is forward aligned with the lever, we can push it.
    if check("the robot's gripper is above the lever"):
        robot.push("the lever")
    # If the gripper is starting to be in front of the lever, push harder.
    if check("the robot's gripper is in front of the lever"):
        robot.push("the lever harder")

# switch-door-open: switch the door open to the other side
def switch_door_open(robot):
    # Steps:
    #  1. Put gripper near the door handle
    #  2. Grab the door handle
    #  3. Pull open the door
    #  4. Move the door away from the door frame
    # Put the gripper near the door handle.
    if check("the robot's gripper is not near the door handle"):
        robot.move("gripper to near the door handle")
    # If the gripper is near the door handle, try grabbing it.
    if check("the robot's gripper is near the door handle and the robot's gripper is open"):
        robot.grab("the door handle")
    # If the gripper is aligned with the door handle as