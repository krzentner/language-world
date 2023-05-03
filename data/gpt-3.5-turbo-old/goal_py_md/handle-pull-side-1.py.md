Here's the program to perform the `handle-pull-side` task:

```
# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle with the gripper
    #  3. Lift the handle up
    # First, put the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")
    # If the handle is not in the gripper, grab it.
    if check("the robot's gripper is not around handle and the robot's gripper is open"):
        robot.move_gripper("near the handle", close_gripper=True)
    # Once the gripper is around the handle, lift it up.
    if check("the robot's gripper is around the handle"):
        robot.move_gripper("above the handle")
```

This program will put the gripper above the handle, grab the handle with the gripper, and then lift the handle up. It uses the same structure as the other programs, with if statements to check if each step has been completed and to move the robot's gripper as needed.