
Steps: 1. Move gripper above the cube, 2. Move gripper down on the cube 3. Move gripper above the target bin 4. Drop the cube in the target bin
- When the robot's gripper is not vertically aligned with cube and the robot's gripper is not open and cube is not near the robot's gripper, move the robot's gripper until the robot's gripper is vertically aligned with cube and the robot's gripper is open
- When cube is not near the robot's gripper and the robot's gripper is not open, move the robot's gripper until the robot's gripper is above the cube and the robot's gripper is open
- When cube is not near the robot's gripper and the robot's gripper is open, move the robot's gripper until the robot's gripper is above the cube
- When the robot's gripper is not vertically aligned with target bin, move the robot's gripper until the robot's gripper is vertically aligned with target bin

The task `insert` requires the robot to insert the peg into the hole.
To insert the peg into the hole reliably, what steps the robot should perform?
Steps: 1. Move gripper down on top of the peg, 2. Grab the peg 3. Move the gripper above the hole 4. Insert the peg in the hole
- When peg is not vertically aligned with hole, move the robot's gripper until the robot's gripper is vertically aligned with peg
- When peg is not near the robot's gripper, move the robot's gripper until the robot's gripper is near the peg and the robot's gripper is open
- When the robot's gripper is not vertically aligned with hole and peg is not vertically aligned with hole, move the robot's gripper until the robot's gripper is vertically aligned with the hole

The task `stack` requires the robot to stack the cube on the target.
To stack the cube on the target reliably, what steps the robot should perform?
Steps: 1. Move gripper down on top of the cube, 2. Grab the cube 3. Move the gripper above the target 4. Drop the cube in the target
- When the robot's gripper is not open and the robot's gripper is not near the cube, move the robot's gripper until the robot's gripper is near the cube and the robot's gripper is open
- When the robot's gripper is open and the robot's gripper is not near the cube, move the robot's gripper until the robot's gripper is near the cube
-