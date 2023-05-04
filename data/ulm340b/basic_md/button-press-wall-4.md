
    - When the robot's gripper is not horizontally aligned with the button and the robot's gripper is not vertically aligned with the button, the robot should put the gripper above the button.
    - When the robot's gripper is vertically aligned with the button and the robot's gripper is not below the button, the robot should push the gripper into the button.
    - When the robot's gripper is below the button, the robot should push the gripper around the wall to the button.
    - When the robot's gripper is horizontally aligned with the button, the robot should push the button forward.

The task `switch-drawer` requires the robot to slide the switch open and close the drawer.
To slide the switch open and close the drawer reliably, what steps the robot should perform?
    - When the robot's gripper is not vertically aligned with switch, the robot should put gripper above switch.
    - When the robot's gripper is vertically aligned with switch and the robot's gripper is open, the robot should push gripper around switch.
    - When the robot's gripper is forward aligned with switch, the robot should turn switch right.
    - When the robot's gripper is right of switch and the robot's gripper is open, the robot should move gripper near drawer handle.
    - When the robot's gripper is near drawer handle, the robot should push drawer closed.
    - When the robot's gripper is below the drawer handle, the robot should push gripper around the drawer handle.
    - When the robot's gripper is above the drawer handle, the robot should pull away from drawer.
    - When the drawer is open, the robot should turn switch left.
    - When the robot's gripper is left of switch, the robot should turn switch left.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the door handle, the robot should put gripper above door handle.
    - When the robot's gripper is vertically aligned with the door handle and the robot's gripper is not near door handle, the robot should put gripper around door handle.
    - When the robot's gripper is around door handle, the robot should push door closed.

The task `peg-insert-front` requires the robot to grab the peg and insert it into the hole from the front.
To grab the peg and insert it into the hole from the front reliably, the robot should perform the following steps:
    - When the robot's gripper is not almost vertically aligned with peg