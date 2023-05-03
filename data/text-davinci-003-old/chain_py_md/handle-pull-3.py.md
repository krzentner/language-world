

The code should be:
```
# handle-pull: pull up the handle
# def handle_pull(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Drop the gripper around the handle
    #  3. Pull the handle up
    # First, move the gripper vertically above the handle so that it's possible to grab it.
    if check("the robot's gripper is not almost vertically aligned with handle"):
        robot.put("gripper above handle")
    # As long as the gripper is almost lined up, closing it should line it up all the way.
    if check("the robot's gripper is almost vertically aligned with the handle and the robot's gripper is open"):
        robot.put("gripper around handle")
    # As long as the gripper is still vertically aligned with the handle, pull it up.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.pull("handle up")
```