
    - When the robot's gripper is not almost vertically aligned with drawer handle, the robot should put gripper above drawer handle.
    - When the robot's gripper is almost vertically aligned with the drawer handle and the robot's gripper is open, the robot should put gripper around drawer handle.
    - When the robot's gripper is vertically aligned with the drawer handle, the robot should pull drawer open.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, what steps the robot should perform?
    - When the robot's gripper is not near the door handle, the robot should grab door handle.
    - When the robot's gripper is forward aligned with door handle, the robot should push door closed.

The task `peg-unstack` requires the robot to lift the top peg off the stack of pegs.
To lift the top peg off the stack of pegs reliably, what steps the robot should perform?
    - When the robot's gripper is not above the stack of pegs, the robot should place the gripper above the stack of pegs.
    - When the robot's gripper is not around the peg and the robot's gripper is open, the robot should drop the gripper around the peg.
    - When the robot's gripper is near the peg and the robot's gripper is open, the robot should close the gripper around the peg.
    - When the robot's gripper is above the stack of pegs and the robot's gripper is closed, the robot should lift the peg off the stack of pegs.

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, what steps the robot should perform?
    - When the robot's gripper is not left of the button, the robot should grab button.
    - When the robot's gripper is forward aligned with the button, the robot should push the button.

The task `peg-insert-vertical` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably, the robot should perform the following steps:
    - When the robot's gripper is not almost vertically aligned with peg, the robot should put gripper above peg.
    - When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
    - When the robot's gripper is almost vertically aligned with the peg and the robot's gripper is forward aligned with the peg, the robot should align peg to hole.