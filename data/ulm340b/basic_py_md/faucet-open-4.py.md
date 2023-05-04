

## Context
This task comes from the following [paper](https://arxiv.org/abs/1803.05313):

```
@inproceedings{shridhar2018interactive,
    title={Interactive Neural Task Programming for Robotic Manipulation Skills},
    author={Shridhar, Ankit and Latif, Yahya and Li, Andy and Paques, Alexandre and Abbeel, Pieter and Malik, Jitendra},
    booktitle={Conference on Robot Learning},
    year={2018}
}
```

and the accompanying code [here](https://github.com/ankit5/robo-imitation).

## Model Solution

```
# faucet-open: turn the faucet left
def faucet_open(robot):
    if check("the robot's gripper is below the faucet handle"):
        robot.put("gripper above faucet handle")
    if check("the robot's gripper is above the faucet handle"):
        robot.put("gripper around faucet handle")
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet left")
```
"""

# fmt: on


# fmt: off
def window_close(robot):
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")


def peg_insert_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")


def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper