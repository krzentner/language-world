

Then add the code:

```
    # Steps:
    #  1. Put gripper below the wrench handle
    #  2. Drop gripper around the wrench handle
    #  3. Pull the wrench off the peg
    # We need to put the robot's gripper below the wrench handle before we can
    # grab it, because of the angle of the robot's gripper.
    if check("the robot's gripper is not below the wrench handle"):
        robot.put("gripper below wrench handle")
    # Once the gripper is lined up below the wrench handle, we should be able to
    # grab the wrench handle by moving the gripper up around it.
    if check("the robot's gripper is below wrench handle and the robot's gripper is not around wrench handle"):
        robot.drop("gripper around wrench handle")
    # Once the gripper is around the wrench handle, we can just pull the wrench
    # off the peg.
    if check("the robot's gripper is around wrench handle"):
        robot.pull("wrench off peg")
```