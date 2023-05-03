

Then, write your code:

```
# plate-slide-back-side: slide the plate back sideways into the target location
def plate_slide_back_side(robot):
    if check("the robot's gripper is not above the plate"):
        robot.place("gripper above plate")
    if check("the robot's gripper is not laying nearly flat beneath the plate"):
        robot.reach("flatly beneath plate")
    if check("the robot's gripper is laying flat beneath the plate and the robot's gripper is not around plate"):
        robot.drop("gripper around plate")
    if check("the robot's gripper is around plate and the plate is not sideways aligned with the goal"):
        robot.align("plate to goal sideways")
    if check("the plate is sideways aligned with the goal"):
        robot.slide("plate back to goal")
```