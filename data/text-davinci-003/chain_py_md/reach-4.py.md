

The robot should be able to extend its arm to the target location.

```
# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Extend arm to the target location
    #  2. Hold arm in place

    # First, extend the robot arm so it is positioned at the target location
    if check("the robot's arm is not at the target location"):
        robot.extend("arm to the target location")
    # Once the arm is in position, keep it in place
    if check("the robot's arm is at the target location"):
        robot.hold("arm in place")
```