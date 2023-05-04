

You're welcome to make up the names of the steps, but you should use the ones
from the earlier programs when they make sense.
If you run into trouble, you can type "help" and I will try to assist you.



<br>





> You can find all the code for the robot in
> ```
> # reach: reach to the target location
> def reach(robot):
>     # Steps:
>     #  1. Reach towards the target
>     # We don't have any objects to manipulate, so we can just move the robot's
>     # gripper directly to the target location
>     if check("the robot's gripper is not near reach target"):
>         robot.reach("to goal")
>
> # door-open: pull the door open
> def door_open(robot):
>     # Steps:
>     #  1. Put gripper above door handle
>     #  2. Drop gripper around door handle
>     #  3. Pull open the door
>     # First, put the gripper mostly above the door handle.
>     if check("the robot's gripper is not almost vertically aligned with door handle"):
>         robot.put("gripper above door handle")
>     # As long as the gripper is almost lined up, closing it should line it up
>     # all the way.
>     if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
>         robot.put("gripper around door handle")
>     # As long as the gripper is still vertically aligned with the door handle,
>     # it's being opened, so keep pulling.
>     if check("the robot's gripper is vertically aligned with the door handle"):
>         robot.pull("door open")
>
> # drawer-close: push the drawer close
> def drawer_close(robot):
>     # Steps:
>     #  1. Put gripper roughly around the drawer handle
>     #  2. Push the drawer closed
>     # If the gripper is not near the drawer handle, move it to the drawer
>     # handle.
>     # We don't need to be careful about the direction, since the drawer is large
>     # and we're just pushing it (unlike when opening the drawer).
>     if check("the robot's gripper is not near the drawer handle"):
>         robot.grab("drawer handle")
>     # If the drawer is aligned with the gripper as seen from