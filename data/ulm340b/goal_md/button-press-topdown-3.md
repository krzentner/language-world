
    Steps:  1. Put gripper above button  2. Drop gripper until hitting button  3. Push button down
    - When the robot's gripper is not vertically aligned with button, move the robot's gripper until the robot's gripper is vertically aligned with button
    - When the robot's gripper is vertically aligned with button and the robot's gripper is above the button, move the robot's gripper until the robot's gripper is touching the button
    - When the robot's gripper is touching the button, move the robot's gripper until the robot's gripper is vertically aligned with button and the robot's gripper is around the button

The task `pick-place-with-peg` requires the robot to pick up the peg, then the puck, and then move the puck to the target location while holding onto the peg.
To pick up the puck, then the puck, and then move the puck to the target location while holding onto the peg reliably, what steps the robot should perform?
    Steps:  1. Put gripper above the peg  2. Drop gripper around the peg  3. Grab the peg with the gripper  4. Move gripper above puck  5. Drop gripper around the puck  6. Close gripper around puck  7. Move puck to goal  8. Put peg down
    - When the robot's gripper is not almost vertically aligned with the peg, move the robot's gripper until the robot's gripper is almost vertically aligned with the peg
    - When the robot's gripper is not around the peg, move the robot's gripper until the robot's gripper is around the peg
    - When the robot's gripper is vertically aligned with the peg and the robot's gripper is around the peg, move the robot's gripper until the robot's gripper is above the puck
    - When the robot's gripper is above the puck, move the robot's gripper until the robot's gripper is around the puck
    - When the robot's gripper is above the puck and the robot's gripper is around the puck and the robot's gripper is open, move the robot's gripper until the robot's gripper is almost vertically aligned with the puck
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is around the puck, move the robot's gripper until the robot's gripper is touching the puck
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is touching the puck, move the robot's gripper until