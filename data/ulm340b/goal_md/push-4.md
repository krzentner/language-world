
    Steps:  1. Get gripper near the puck  2. Push puck towards target
    We should start off by putting the robot's gripper near the puck so that we can push it
    - When the robot's gripper is not near the puck, move the robot's gripper until the robot's gripper is near the puck
    Now that the gripper is near the puck, we can just push the puck.
    - When the robot's gripper is near the puck, move the robot's gripper until the robot's gripper is near the target location

The task `push-wall` requires the robot to push the puck towards the target location, with a wall blocking it halfway through.
To push the puck towards the target location, with a wall blocking it halfway through reliably, what steps the robot should perform?
    Steps:  1. Get gripper near the puck  2. Push puck towards target
    First, put the robot's gripper near the puck.
    - When the robot's gripper is not near the puck, move the robot's gripper until the robot's gripper is near the puck
    Now that the gripper is near the puck, we can just push the puck.
    - When the robot's gripper is near the puck, move the robot's gripper until the robot's gripper is near the target location

The task `push-multistep` requires the robot to push the puck towards the target location, with a wall blocking it halfway through.
To push the puck towards the target location, with a wall blocking it halfway through reliably, what steps the robot should perform?
    Steps:  1. Get gripper near the puck  2. Push puck until it hits the wall  3. Get gripper near the puck  4. Push the puck over the wall
    First, put the robot's gripper near the puck.
    - When the robot's gripper is not near the puck, move the robot's gripper until the robot's gripper is near the puck
    Now that the gripper is near the puck, we can just push the puck.
    - When the robot's gripper is near the puck and the puck is in front of the wall, move the robot's gripper until the robot's gripper is not near the puck
    As long as the robot's gripper is not near the puck, move the robot's gripper until the robot's gripper is near the puck
    - When the robot's gripper is not near the puck and the puck is not in front of the wall, move the