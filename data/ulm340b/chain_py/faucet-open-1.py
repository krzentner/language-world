
    # Steps:
    #  1. Put gripper around faucet handle
    #  2. Rotate faucet handle left
    # If the gripper is not lined up vertically with the faucet handle, try to
    # align it from the side
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.align("gripper with faucet handle")
    # If the faucet handle is not forward aligned with the gripper, maybe we
    # haven't grabbed it properly yet.
    if check("the robot's gripper is vertically aligned with faucet handle and the faucet handle is not forward aligned with the robot's gripper"):
        robot.put("gripper around faucet handle")
    # As long as the faucet handle is near the gripper, we can try turning it
    # left.
    if check("the faucet handle is forward aligned with the robot's gripper"):
        robot.rotate("the faucet handle left")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper roughly around the door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    # We don't need to be careful about the direction, since the door is large
    # and we're just pushing it (unlike when opening the door).
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    # If the door is aligned with the gripper as seen from in front, we can push
    # the door closed.
    if check("the robot's gripper is forward aligned with door handle"):
        robot.push("door closed")

# faucet-close: turn the faucet right
def faucet_close(robot):
    # Steps:
    #  1. Put gripper around faucet handle
    #  2. Rotate faucet handle right
    # If the gripper is not lined up vertically with the faucet handle, try to
    # align it from the side
    if check("the robot's gripper is not vertically aligned with faucet handle"):
        robot.align("gripper with faucet handle")
    # If the faucet handle is not forward aligned with the gripper, maybe we
   