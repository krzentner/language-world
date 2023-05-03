The robot should perform the following steps to pick up the puck and hold it at the target location:
    
    Steps:  1. Put gripper above the puck  2. Grab the puck with the gripper  3. Lift the puck  4. Move the gripper to the target location  5. Lower the puck at the target location
    First, put the gripper above the puck.
    - When the robot's gripper is not vertically aligned with the puck, move the robot's gripper until the robot's gripper is vertically aligned with the puck
    Once the gripper is aligned with the puck, we should grab it.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not around the puck, move the robot's gripper until the robot's gripper is closed around the puck
    We can now lift the puck and move it to the target location.
    - When the robot's gripper is around the puck, move the robot's gripper until the robot's gripper is above the target location
    Finally, we can lower the puck at the target location.
    - When the robot's gripper is above the target location and the puck is not already at the target location, move the robot's gripper until the robot's gripper is near the target location and the robot's gripper is open  - When the robot's gripper is near the target location and the puck is not already at the target location, move the robot's gripper until the robot's gripper is above the target location and the robot's gripper is closed  - When the robot's gripper is around the puck and the robot's gripper is at the target location, move the robot's gripper until the robot's gripper is open and the puck is left