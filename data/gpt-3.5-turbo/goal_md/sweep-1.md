To grab the cube and move it sideways to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above cube  2. Drop gripper around cube  3. Close gripper around cube  4. Lift the cube slightly off the table  5. Move the gripper and the cube horizontally to the target location  6. Lower the cube onto the target location
    First, put the gripper roughly above the cube, so that we don't bump into it while trying to grab it.
    - When the robot's gripper is not vertically aligned with the cube, move the robot's gripper until the robot's gripper is vertically aligned with the cube
    Once the gripper is lined up above the cube, we should be able to grab it by moving the gripper down around it.
    - When the robot's gripper is vertically aligned with the cube and the robot's gripper is not around the cube, move the robot's gripper until the robot's gripper is around the cube and the robot's gripper is closed
    Once the gripper is around the cube, lift it slightly off the table to make sure it's securely held.
    - When the robot's gripper is around the cube and the cube is not lifted off the table, move the robot's gripper until the cube is slightly lifted off the table
    If the target location is not aligned with the gripper, move the gripper and the cube horizontally to the target location.
    - When the robot's gripper is holding the cube and the cube is not above the target location and the robot's gripper is not horizontally aligned with the target location, move the robot's gripper and the cube until they are horizontally aligned with the target location
    Finally, lower the cube onto the target location.
    - When the robot's gripper and the cube are horizontally aligned with the target location, move the robot's gripper until the cube is sitting on the target location