To grab the cube and move it sideways to the target location reliably, the robot should perform the following steps:
- When the robot's gripper is not vertically aligned with the cube, the robot should put the gripper above it.
- When the cube is not left of the robot's gripper and the cube is not forward aligned with the robot's gripper, the robot should grab the cube.
- When the robot's gripper is forward aligned with the cube, and the cube is not aligned with the target location
    - The robot should move sideways while holding the cube until it is aligned with the target location.
- When the cube is horizontally aligned with the target location, and the robot's gripper is not above the target location
    - The robot should move the gripper above the target location.
- When the robot's gripper is above the target location and the cube is held securely in the gripper
    - The robot should release the cube at the target location.