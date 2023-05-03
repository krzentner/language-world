To slide the puck backwards to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above the rear of the puck  2. Push gripper into the top of the puck while moving back towards the target location  3. Slide the puck backwards to the goal
    Unlike when pushing the puck forward, we need to start with the gripper above the rear of the puck. So, if the gripper isn't already above the rear of the puck, first move it there.
    - When the robot's gripper is not above the rear of the puck, the robot should move gripper above the rear of the puck.
    With the gripper above the rear of the puck, push into the top of the puck while moving back towards the target location. This should slide the puck backwards.
    - When the robot's gripper is above the puck's rear and the robot's gripper is not near the puck, the robot should push the gripper into the top of the puck while moving back towards the goal.
    If the gripper is near the puck, we've probably trapped the puck and can slide it backwards to the target location. Close the gripper to make sure we keep control of the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck backwards to the goal.