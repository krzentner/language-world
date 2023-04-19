```
# faucet-close: turn the faucet right
# def faucet_close(robot):
    # Steps:
    #  1. Put gripper around faucet knob
    #  2. Turn the knob right to close the faucet
    # First, put the gripper around the faucet knob.
    if check("the robot's gripper is not around faucet knob"):
        robot.move_gripper("around the faucet knob")
    # Turn the knob by moving the gripper to the right.
    if check("the robot's gripper is around the faucet knob and the faucet is not fully right"):
        robot.move_gripper("right of the faucet knob")
```