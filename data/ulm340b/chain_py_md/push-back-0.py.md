

Then, use the `check` function to check when to execute each step of the
task.

```
def push_back(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into back of puck
    #  3. Slide puck to goal
    # Because the task is "push-back", we need to put the gripper above the
    # puck with the back of the puck facing the gripper.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the back of the puck"):
        robot.place("the gripper above the back of the puck")
    # Once the gripper is aligned with the back of the puck, move the gripper
    # down.
    if check("the robot's gripper is vertically aligned with the back of the puck and the robot's gripper is not near the puck"):
        robot.push("the gripper into the back of the puck")
    # Once the gripper is near the puck, slide the puck to the goal while
    # keeping the gripper against the puck.
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")
```

Now write programs to perform the rest of the tasks in the table below:

```
# button-press: push the button down from the side
def button_press(robot):

# door-close: push the door closed
def door_close(robot):

# peg-insert: grab the peg and insert it into the hole from above
def peg_insert(robot):

# window-open: slide the window open to the side
def window_open(robot):

# pick: pick up the puck
def pick(robot):

# pick-place-with-camera-shake: pick up the puck, but with camera noise
def pick_place_with_camera_shake(robot):

# push-side: slide the puck sideways to the target location
def push_side(robot):

# push-side-back: slide the puck sideways backwards to the target location
def push_side_back(robot):

# hook: slide the hook to the target location
def hook(robot):

# hook-back: slide the hook to the target location backwards
def hook_back(robot):

# reach-back: reach the target location from behind
def