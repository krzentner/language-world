

The first step of every task is to check whether it's done.
```
    # Steps:
    #  1. Put gripper around handle
    #  2. Pull mug toward target
    # If the robot's gripper is around the handle, we can stop.
    if check("the robot's gripper is not around handle"):
```

First, the robot's gripper must be moved close to the mug handle.
```
    # First, put the gripper roughly around the mug handle, so that we don't bump it while
    # trying to grab it.
    if check("the robot's gripper is not above the mug handle"):
```

As long as the gripper is roughly above the mug handle, we should just keep trying to drop the gripper around it.
```
    # As long as the gripper is roughly above the mug handle, we should just keep trying to drop the gripper around it.
    if check("the robot's gripper is above the mug handle and the robot's gripper is not around the mug handle"):
```

As long as the gripper is around the mug handle, and the robot's gripper is still open, we should just keep trying to drop the gripper around the mug handle.
```
    # As long as the gripper is around the mug handle, and the robot's gripper is still open, we should just keep trying to drop the gripper around the mug handle.
    if check("the robot's gripper is around the mug handle and the robot's gripper is open"):
```

If the robot's gripper is around the mug handle, the robot's gripper is closed, and the mug handle is in front of the robot, we can just pull the handle toward the target location.
```
    # If the robot's gripper is around the mug handle, the robot's gripper is closed, and the mug handle is in front of the robot, we can just pull the handle toward the target location.
    if check("the robot's gripper is around the mug handle and the robot's gripper is closed and the robot's gripper is forward aligned with mug handle"):
```

The command `robot.pull("mug handle toward target")` will pull the mug handle toward the target location.
```
    # The command `robot.pull("mug handle toward target")` will pull the mug handle toward the target location.
    if check("the robot's gripper is around the mug