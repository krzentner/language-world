
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Grasp the handle
    #  4. Turn faucet left
    # If the gripper is not above the faucet handle, we should put the gripper
    # directly above the handle.
    if check("the robot's gripper is not above the faucet handle"):
        robot.put("gripper above faucet handle")
    # If the gripper is above the faucet handle and not around it, we can
    # grab the faucet handle.
    # We need to grab the faucet handle so that the robot can turn it.
    if check("the robot's gripper is above the faucet handle and the robot's gripper is not around the faucet handle"):
        robot.drop("gripper around faucet handle")
    # Once the gripper is around the faucet handle and the faucet handle is
    # grasped by the robot, the robot can turn the faucet left.
    if check("the robot's gripper is around the faucet handle and the faucet handle is grasped by the robot"):
        robot.turn("faucet left")

# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper above faucet handle
    #  2. Drop gripper around faucet handle
    #  3. Grasp the handle
    #  4. Turn faucet right
    # If the gripper is not above the faucet handle, we should put the gripper
    # directly above the handle.
    if check("the robot's gripper is not above the faucet handle"):
        robot.put("gripper above faucet handle")
    # If the gripper is above the faucet handle and not around it, we can
    # grab the faucet handle.
    # We need to grab the faucet handle so that the robot can turn it.
    if check("the robot's gripper is above the faucet handle and the robot's gripper is not around the faucet handle"):
        robot.drop("gripper around faucet handle")
    # Once the gripper is around the faucet handle and the faucet handle is
    # grasped by the robot, the robot can turn the faucet right.
    if check("the robot's gripper is around the faucet handle and