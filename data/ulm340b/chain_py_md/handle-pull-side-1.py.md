

The `Steps:` and the first lines of code are included below for convenience:

```
# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper left of handle
    #  2. Grab handle
    #  3. Pull handle up
    # If the robot's gripper is to the right of the handle, we can't grab it, so
    # move the robot's gripper to the left of the handle.
    if check("the robot's gripper is not left of handle"):
        robot.put("gripper left of handle")
```

The robot has a single gripper that can be used to grab small objects.

""",
    # The program itself.
    program=[
        """# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Reach towards the target
    # We don't have any objects to manipulate, so we can just move the robot's
    # gripper directly to the target location
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")

""",
        """# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper above puck
    #  2. Push gripper into top of puck
    #  3. Slide puck to goal
    # The robot can slide the puck by trapping it by pushing down on it from
    # above and moving the gripper.
    # If the puck isn't below the gripper as seen from above, move the gripper
    # above the puck.
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    # If the gripper is aligned with the puck but not near it, move the gripper
    # down to the puck to slide it.
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    # If the gripper is near the puck, we've probably trapped the puck and can
