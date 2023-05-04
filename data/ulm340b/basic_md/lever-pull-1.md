
    - When the robot's gripper is not vertically aligned with the lever handle and the robot's gripper is below lever handle, the robot should place gripper above lever handle.
    - When the robot's gripper is above lever handle and the robot's gripper is not around lever handle, the robot should put gripper around lever handle.
    - When the robot's gripper is vertically aligned with the lever handle and the robot's gripper is around lever handle, the robot should pull lever up.

The task `peg-unplug-side` requires the robot to grab the peg and pull it out of the hole from the side.
To grab the peg and pull it out of the hole from the side reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with peg, the robot should move gripper above peg.
    - When peg is forward aligned with the robot's gripper, the robot should put gripper around peg.
    - When the robot's gripper is above the peg, the robot should pull out peg from hole.

The task `door-close` requires the robot to push the door close.
To push the door close reliably, the robot should perform the following steps:
    - When the robot's gripper is not vertically aligned with door handle, the robot should put gripper above door handle.
    - When the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle, the robot should put gripper around door handle.
    - When the robot's gripper is vertically aligned with door handle and the robot's gripper is open, the robot should close gripper around door handle.
    - When the robot's gripper is around door handle, the robot should push door closed.

The task `pick-place-with-camera` requires the robot to pick up the puck and hold it at the target location while watching the puck through the camera.
To pick up the puck and hold it at the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the puck, the robot should move gripper above puck.
    - When the robot's gripper is vertically aligned with the puck, the robot should close gripper around puck.
    - When the robot's gripper is above the puck, the robot should place puck at goal.
    - When the robot's gripper is vertically aligned with the puck, the robot should grab puck.

The task `peg-insert-top` requires the robot to grab the peg and insert it into the hole from above.
To grab the peg and insert it into the hole from above reliably,