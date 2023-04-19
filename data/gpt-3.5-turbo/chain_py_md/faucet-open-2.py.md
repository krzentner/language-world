# faucet-open: turn the faucet left
# def faucet_open(robot):

# Steps:
#  1. Put gripper around the faucet handle
#  2. Push the faucet handle and turn it left
#  3. Stop when the handle can't be turned anymore

# Move gripper around the faucet handle.
if check("the robot's gripper is not around the faucet handle"):
    robot.drop("gripper around faucet handle")
# Turn the faucet handle left by pushing it with the gripper.
if check("the faucet handle can still be turned left"):
    robot.push("faucet handle left")