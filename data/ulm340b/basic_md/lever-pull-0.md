
If the robot's gripper is not vertically aligned with the lever:
    The robot should move gripper above lever.
If the robot's gripper is below the lever:
    The robot should move gripper left of lever.
If the robot's gripper is left of the lever and the robot's gripper is not around lever:
    The robot should move gripper around lever.
If the robot's gripper is around the lever:
    The robot should pull lever.

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, what steps the robot should perform?
If the robot's gripper is not vertically aligned with the button:
    The robot should move gripper above button.
If the robot's gripper is below the button and the robot's gripper is open:
    The robot should move gripper around button.
If the robot's gripper is around the button:
    The robot should push button left.

The task `door-close` requires the robot to close the door.
To close the door reliably, what steps the robot should perform?
If the robot's gripper is below the door handle:
    The robot should move gripper above door handle.
If the robot's gripper is above the door handle and the robot's gripper is not around door handle:
    The robot should put gripper around door handle.
If the robot's gripper is around the door handle and the robot's gripper is not forward aligned with the door handle:
    The robot should push gripper into door handle.
If the robot's gripper is forward aligned with the door handle:
    The robot should push door closed.

The task `pick` requires the robot to pick up the puck.
To pick up the puck reliably, what steps the robot should perform?
If the robot's gripper is not above puck:
    The robot should move gripper above puck.
If the robot's gripper is above puck and the robot's gripper is open:
    The robot should move gripper near puck.
If the robot's gripper is near puck and the robot's gripper is not closed:
    The robot should close gripper.

The task `peg-unplug-side` requires the robot to grab the peg and unplug it from the hole from the side.
To grab the peg and unplug it from the hole from the side reliably, what steps the robot should perform?
If the robot's gripper is not above