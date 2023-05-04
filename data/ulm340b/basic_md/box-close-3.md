
    - When the robot's gripper is not over box lid, the robot should put gripper over box lid.
    - When the robot's gripper is open and the robot's gripper is around box lid, the robot should grab box lid.
    - When the robot's gripper is over the box and the box lid is over the box, the robot should release gripper around the box lid.

The task `box-open` requires the robot to pick up the box lid and place it on the table.
To pick up the box lid and place it on the table reliably, what steps the robot should perform?
    - When the robot's gripper is not over box lid, the robot should put gripper over box lid.
    - When the robot's gripper is open and the robot's gripper is around box lid, the robot should grab box lid.
    - When the robot's gripper is over the table and the box lid is over the table, the robot should release gripper around the box lid.



%% filename: src/appendices/instructions-old.tex %%


The task `pick-place` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not near puck, the robot should put gripper over puck.
    - When the robot's gripper is over puck, the robot should grab puck.
    - When the robot's gripper is over puck and the robot's gripper is closed, the robot should put puck at goal.

The task `door-open` requires the robot to pull the door open.
To pull the door open reliably, the robot should perform the following steps:
    - When the robot's gripper is not almost vertically aligned with door handle, the robot should put gripper above door handle.
    - When the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open, the robot should put gripper around door handle.
    - When the robot's gripper is vertically aligned with the door handle, the robot should pull door open.

The task `reach` requires the robot to reach to the target location.
To reach to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not near reach target, the robot should put gripper at goal.

The task `window-close` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, the robot should perform the following steps:
    - When