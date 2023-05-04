
    The robot should perform the following steps:
        Steps:  1. Put gripper roughly around the drawer handle  2. Pull the drawer open
        If the gripper is not near the drawer handle, move it to the drawer handle. We don't need to be careful about the direction, since the drawer is large and we're just pulling it (unlike when closing the drawer).
        If the drawer is aligned with the gripper as seen from in front, we can pull the drawer open.

The task `button-press-side` requires the robot to push the button down sideways.
To push the button down sideways reliably, what steps the robot should perform?
    The robot should perform the following steps:
        Steps:  1. Put gripper roughly in front of the button  2. Push the button sideways down
        If the gripper is not near the button, move it to the button.
        If the gripper is aligned with the button as seen from in front, we can push the button down sideways.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, what steps the robot should perform?
    The robot should perform the following steps:
        Steps:  1. Put gripper above door handle  2. Put gripper around door handle  3. Push door closed
        First, put the gripper mostly above the door handle.
        As long as the gripper is almost lined up, putting it around should line it up all the way.
        As long as the gripper is still vertically aligned with the door handle, it's being closed, so keep pushing.

The task `peg-insert-topdown` requires the robot to grab the peg and insert it into the hole from the top.
To grab the peg and insert it into the hole from the top reliably, what steps the robot should perform?
    The robot should perform the following steps:
        Steps:  1. Put gripper above the peg  2. Grab the peg with the gripper  3. Line the peg up with the hole  4. Insert the peg into the hole
        First, put the gripper above the peg.
        If the peg becomes left of the gripper, go back to putting the gripper above the peg.
        As long the gripper is still mostly around the peg and the peg isn't lined up with the hole, line up the peg with the hole.
        If the peg is lined up with the hole to the top, insert it.


Hello. We have provided you with strategies for how to perform a wide variety of tasks reliably. Now, I'd like you to tell me what you