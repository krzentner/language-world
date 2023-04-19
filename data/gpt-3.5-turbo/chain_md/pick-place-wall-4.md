The robot needs to perform the following steps for the task `pick-place-wall`:
    Steps:  1. Put gripper above puck  2. Drop gripper around puck  3. Close gripper around puck  4. Move puck to wall  5. Move gripper over the wall to the other side  6. Lower gripper down to place puck at goal
The first three steps are identical to the `pick-place` task, so we can reuse them. After the gripper has closed around the puck, the robot needs to move the puck to the short wall. 
    - When the robot's gripper is closed around puck and the puck is not yet at the wall, the robot should move puck to wall.
Next, the robot needs to move the gripper over the wall to the other side.
    - When the robot's gripper is above the wall, the robot should move the gripper over the wall to the other side.
Finally, the robot needs to lower the gripper down to place the puck at the target location.
    - When the robot's gripper is on the other side of the wall and above the goal, the robot should place the puck at the goal location by lowering the gripper down.