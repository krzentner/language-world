
    - When the robot's gripper is not vertically aligned with the box lid, the robot should put gripper above box lid.
    - When the box lid is not near the robot's gripper, the robot should pick up box lid.
    - When the box lid is near the robot's gripper and the robot's gripper is not near the box, the robot should put the box lid on top of the box.

The task `faucet-open` requires the robot to pull the faucet open.
To pull the faucet open reliably, the robot should perform the following steps:
    - When the robot's gripper is not almost vertically aligned with faucet handle, the robot should put gripper above faucet handle.
    - When the robot's gripper is almost vertically aligned with the faucet handle and the robot's gripper is open, the robot should put gripper around faucet handle.
    - When the robot's gripper is vertically aligned with the faucet handle, the robot should pull faucet open.

The task `box-open` requires the robot to pick up the box lid and place it above the box.
To pick up the box lid and place it above the box reliably, what steps the robot should perform?
    - When the robot's gripper is not vertically aligned with the box lid, the robot should put gripper above box lid.
    - When the box lid is not near the robot's gripper, the robot should pick up box lid.
    - When the box lid is near the robot's gripper and the robot's gripper is near the box, the robot should put the box lid above the box.

The task `button-press` requires the robot to push the button.
To push the button reliably, the robot should perform the following steps:
    - When the robot's gripper is not above button and the robot's gripper is not vertically aligned with the button, the robot should put gripper above button.
    - When the robot's gripper is vertically aligned with button, the robot should push button.

The task `plug-insert-side` requires the robot to pick up the plug and insert it into the socket from the side.
To pick up the plug and insert it into the socket from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with the plug, the robot should put gripper above plug.
    - When the robot's gripper is vertically aligned with the plug and the robot's gripper is open, the robot should close gripper around plug.
    - When the robot's gripper is closed around plug, the robot should insert plug into socket.

The task `button-press