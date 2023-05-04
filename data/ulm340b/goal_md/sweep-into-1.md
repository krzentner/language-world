
Steps:  1. Put gripper above cube  2. Drop gripper around cube  3. Close gripper around cube  4. Move cube to goal
    First, put the gripper above the cube.
    - When the robot's gripper is not above the cube, move the robot's gripper until the robot's gripper is above the cube
    If the gripper isn't around the cube, put it around the cube.
    - When the robot's gripper is not around cube and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the cube and the robot's gripper is closed
    If the gripper is near the cube and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is above cube and the robot's gripper is closed, move the robot's gripper until the robot's gripper is near the target location

The task `hook-pull` requires the robot to grab the handle with the hook and pull it out.
To grab the handle with the hook and pull it out reliably, what steps the robot should perform?
Steps:  1. Put hook on the hook handle  2. Close the hook  3. Pull the hook handle out
    First, put the hook above the hook handle.
    - When the hook is not above hook handle, move the hook until the hook is above hook handle
    If the hook is lined up above the hook handle we can close the hook.
    - When the hook is above hook handle, move the hook until the hook is around the hook handle and the hook is closed
    If the hook is around the hook handle and closed we can pull the hook handle out.
    - When the hook is around the hook handle and the hook is closed, move the hook until the hook is above the hook handle and the hook is open

The task `c-shape` requires the robot to move the c shape to the target location.
To move the c shape to the target location reliably, what steps the robot should perform?
Steps:  1. Put gripper above c-shape  2. Push gripper into top of c-shape  3. Slide c-shape to goal
    The robot can move the c-shape by trapping it by pushing down on it from above and moving the gripper. If the c-shape isn't below the gripper as seen from above, move the gripper above the c-shape.
    - When the robot's gripper is not above c-shape and the robot's gripper is not vertically aligned