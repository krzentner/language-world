

Then the code goes like this:

```
# plate-slide: slide the plate into the target location
def plate_slide(robot):
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    if check("the robot's gripper is vertically aligned with plate and the robot's gripper is open"):
        robot.grab("plate")
    if check("plate is not aligned with the target destination"):
        robot.align("plate to destination")
    if check("plate is aligned with the target destination and the robot's gripper is forward aligned with plate"):
        robot.slide("plate to destination")

```