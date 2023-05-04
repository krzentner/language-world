:
    Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
    Because this is "front", we need to line up the gripper by moving it around the button before pushing. Line up the robot's gripper from above and close it.
    - When the robot's gripper is not vertically aligned with button, move the robot's gripper until the robot's gripper is vertically aligned with the button and the robot's gripper is closed
    Now that the gripper is lined up, just push down on the button.
    - When the robot's gripper is vertically aligned with button, move the robot's gripper until the robot's gripper is near the button

The task `drawer-close` requires the robot to push the drawer close.
To push the drawer close reliably, what steps the robot should perform?:
    Steps:  1. Put gripper roughly around the drawer handle  2. Push the drawer closed
    If the gripper is not near the drawer handle, move it to the drawer handle. We don't need to be careful about the direction, since the drawer is large and we're just pushing it (unlike when opening the drawer).
    - When the robot's gripper is not near the drawer handle, move the robot's gripper until the robot's gripper is near the drawer handle
    If the drawer is aligned with the gripper as seen from in front, we can push the drawer closed.
    - When the robot's gripper is forward aligned with drawer handle, move the robot's gripper until the robot's gripper is around the drawer handle

The task `door-open` requires the robot to pull the door open.
To pull the door open reliably, what steps the robot should perform?:
    Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Pull open the door
    First, put the gripper mostly above the door handle.
    - When the robot's gripper is not almost vertically aligned with door handle, move the robot's gripper until the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is closed
    As long as the gripper is almost lined up, closing it should line it up all the way.
    - When the robot's gripper is vertically aligned with the door handle, move the robot's gripper until the robot's gripper is left of the door handle

The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from