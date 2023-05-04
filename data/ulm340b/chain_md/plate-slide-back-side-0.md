"""

instructions_no_plan = """


The task `drawer-open` requires the robot to pull the drawer open.
To pull the drawer open reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above drawer handle  2. Drop gripper around drawer handle  3. Pull open the drawer
    We need to put the gripper above the drawer handle before we can grab it, because of the angle of the robot's gripper.
    Once the gripper is lined up above the drawer handle, we should be able to grab the drawer handle by moving the gripper down around it.
    Once the gripper is around the drawer handle, we can just pull the drawer open.

The task `button-press-topdown` requires the robot to push the button down from above.
To push the button down from above reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
    Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
    Now that the gripper is lined up, just push down on the button.

The task `drawer-close` requires the robot to push the drawer close.
To push the drawer close reliably, the robot should perform the following steps:
    Steps:  1. Put gripper roughly around the drawer handle  2. Push the drawer closed
    If the gripper is not near the drawer handle, move it to the drawer handle. We don't need to be careful about the direction, since the drawer is large and we're just pushing it (unlike when opening the drawer).
    If the drawer is aligned with the gripper as seen from in front, we can push the drawer closed.

The task `door-open` requires the robot to pull the door open.
To pull the door open reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Pull open the door
    First, put the gripper mostly above the door handle.
    As long as the gripper is almost lined up, closing it should line it up all the way.
    As long as the gripper is still vertically aligned with the door handle, it's being opened, so keep pulling.

The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
To grab the peg and insert it into