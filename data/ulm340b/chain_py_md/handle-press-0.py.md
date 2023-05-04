

In this task:

- The handle needs to be pressed downward (not to the side).
- The handle does not need to be grasped or grabbed by the gripper.
- The handle is large and easy to line up with as seen from the top.

Please write code to perform the task here:

# REPLACE THIS COMMENT WITH YOUR CODE
# handle-press: push down the handle
def handle_press(robot):
    if check("the robot's gripper is not above handle and the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    if check("the robot's gripper is vertically aligned with handle"):
        robot.push("down handle")
# REPLACE THIS COMMENT WITH YOUR CODE

### Task 3: Debugging

In each of the code examples below, something is wrong. Can you fix the code and then describe what was wrong? Please describe in English what the bug was and how it should have worked.

```
# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Reach towards the target
    # We don't have any objects to manipulate, so we can just move the robot's
    # gripper directly to the target location
    # TODO: fix the reach(robot) function to reach to the target location
    if check("the robot's gripper is not near reach target"):
        robot.move("gripper to right of reach target")
```


```
# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Drop gripper around puck
    #  3. Close gripper around puck
    #  4. Move puck to goal
    # First, put the gripper roughly above puck, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    # If the gripper isn't around the puck, put it around the puck.
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    # If the gripper is near the puck and open, maybe we can grab it by closing
  