

and use the check statements in the task description to finish the program:

```
# plate-slide: slide the plate into the target location
# The robot's gripper is not forward aligned with the plate
# The robot's gripper is not near the plate
# The robot's gripper is near the plate
# The robot's gripper is around the plate
# The plate is in front of the target location
def plate_slide(robot):
    pass
```
    
# GPT-3

> Hello. Today I would like you to help me control a robot. The robot has a single gripper that it can use to grab small objects.

> Here's some code that demonstrates how the robot can do a variety of tasks:

> ```
> # button-press-topdown: push the button down from above
> def button_press_topdown(robot):
>     if check("the robot's gripper is not vertically aligned with button"):
>         robot.put("gripper above button")
>     if check("the robot's gripper is vertically aligned with button"):
>         robot.push("down on button")
>
> # drawer-open: pull the drawer open
> def drawer_open(robot):
>     if check("the robot's gripper is not vertically aligned with drawer handle"):
>         robot.put("gripper above drawer handle")
>     if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
>         robot.put("gripper around drawer handle")
>     if check("the robot's gripper is around drawer handle"):
>         robot.pull("away from drawer")
>
> # door-open: pull the door open
> def door_open(robot):
>     if check("the robot's gripper is not almost vertically aligned with door handle"):
>         robot.put("gripper above door handle")
>     if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
>         robot.put("gripper around door handle")
>     if check("the robot's gripper is vertically aligned with the door handle"):
>         robot.pull("door open")
>
> # drawer-close: push the drawer close
> def drawer_close(robot):
>     if check("the robot's gripper is not near the drawer handle"):
>         robot.grab("drawer handle")
>     if check("the robot's gripper is forward aligned with drawer handle"):
