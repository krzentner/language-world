

Then, write some code to perform the steps for this task.

```
# Steps:
#  1. Put the gripper above the handle
#  2. Close the gripper on the handle from above
#  3. Pull up on the handle from above
#  4. Let the handle fall so that it's hanging from the gripper
#  5. Lift the handle to the goal location
# First, put the gripper roughly above the handle.
```

**Steps:**

* First, put the gripper roughly above the handle.
* Then, close the gripper on the handle from above.
* Then, pull the gripper up on the handle from above.
* Then, let the handle fall so that it's hanging from the gripper.
* Finally, lift the handle up above the goal location.

**Code:**

```
# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put the gripper above the handle
    #  2. Close the gripper on the handle from above
    #  3. Pull up on the handle from above
    #  4. Let the handle fall so that it's hanging from the gripper
    #  5. Lift the handle to the goal location
    # First, put the gripper roughly above the handle.
    if check("the robot's gripper is not above the handle"):
        robot.move_gripper("above the handle")

    # Then, close the gripper on the handle from above.
    if check("the robot's gripper is above the handle and the handle is not vertically aligned with the robot's gripper"):
        robot.move_gripper("above the handle", close_gripper=True)

    # Then, pull the gripper up on the handle from above.
    if check("the robot's gripper is vertically aligned with the handle"):
        robot.move_gripper("vertically aligned with the handle")

    # Then, let the handle fall so that it's hanging from the gripper.
    if check("the robot's gripper is above the handle"):
        robot.move_gripper("above the handle", open_gripper=True)

    # Finally, lift the handle up above the goal location.
    if check("the handle is not vertically aligned with the robot's gripper"):
        robot