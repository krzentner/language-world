

Write your program using the following vocabulary:

    * left: left of (the lever)
    * right: right of (the lever)
    * in front: in front of (the lever)
    * above: above (the lever)
    * below: below (the lever)

    * forward: forward
    * backward: backward
    * left: left
    * right: right
    * up: up
    * down: down

    * gripper: gripper
    * lever: lever
    * table: table

Here's some helpful comments:

    * Steps:
      *  1. Grab the gripper from the side
      *  2. Pull the gripper up

To help you out, I've written the first few steps.

```
# lever-pull: rotate the lever up
def lever_pull(robot):
    # Steps:
    #  1. Grab the gripper from the side
    #  2. Pull the gripper up
    # We need to put the gripper on the right side of the lever.
    if check("the robot's gripper is not right of the lever and the robot's gripper is not left of the lever and the robot's gripper is not in front of the lever"):
        robot.move_gripper("right of the lever")
    # Once the gripper is right of the lever, we need to grab it from the side.
    if check("the robot's gripper is right of the lever and the robot's gripper is not above the lever and the robot's gripper is not below the lever"):
        robot.move_gripper("around the lever")
    # TODO: continue the program
```
'''

# %%
# lever-pull: rotate the lever up
def lever_pull(robot):
    # Steps:
    #  1. Grab the gripper from the side
    #  2. Pull the gripper up
    # We need to put the gripper on the right side of the lever.
    if check("the robot's gripper is not right of the lever and the robot's gripper is not left of the lever and the robot's gripper is not in front of the lever"):
        robot.move_gripper("right of the lever")
    # Once the gripper is right of the lever, we need to grab it from the side.
    if check("the robot's gripper is right of the lever and