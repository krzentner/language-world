
    We should not have to do anything! Just put the ball near the hoop.

The task `drawer-close-topdown` requires the robot to push the drawer closed from above.
To push the drawer closed from above reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above drawer handle  2. Push the drawer closed 
    If the gripper is not vertically aligned with the drawer handle, put the gripper above the drawer handle.
    - When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.
    If the robot's gripper is vertically aligned with the drawer handle, we can push the drawer closed
    - When the robot's gripper is vertically aligned with drawer handle, the robot should push drawer closed.

The task `button-press-side` requires the robot to push the button from the side.
To push the button from the side reliably, the robot should perform the following steps:
    Steps:  1. Put gripper in front of button  2. Push button from the side  
    If the robot's gripper is not in front of the button, put the gripper in front of button.
    - When the robot's gripper is not forward aligned with button, the robot should put gripper in front of button.
    If the robot's gripper is forward aligned with the button, we can push the button from the side
    - When the robot's gripper is forward aligned with button, the robot should push the button sideways.

The task `door-close` requires the robot to push the door closed.
To push the door closed reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above door handle  2. Drop gripper around door handle  3. Push the door closed
    Put the gripper above the door handle
    - When the robot's gripper is not vertically aligned with door handle, the robot should put gripper above door handle.
    Now that the gripper is above the door handle, we can move the gripper down around the door handle
    - When the robot's gripper is vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.
    As long as the gripper is still vertically aligned with the door handle, we can push the door closed
    - When the robot's gripper is vertically aligned with the door handle, the robot should push door closed.

The task `door-open-topdown` requires the robot to pull the door open from above