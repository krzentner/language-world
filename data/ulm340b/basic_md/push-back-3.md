
\question
    {When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
     When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
     When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck to the goal.
    }
    \correct
    {When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
     When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
     When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck backwards to the goal.
    }
    \incorrect
    {}
    \correct
    {}
    \incorrect
    {}
    \correct
    {}
    \incorrect
    {}

To slide the puck backwards to the target location reliably, the robot should perform the following steps:
    - When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
    - When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
    - When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck backwards to the goal.

The task `pick-place-wall` requires the robot to pick up the puck and hold it on top of the wall.
To pick up the puck and hold it on top of the wall reliably, the robot should perform the following steps:
    - When the robot's gripper is not above the puck, the robot should place gripper above puck.
    - When the robot's gripper is not around puck and the robot's gripper is open, the robot should drop gripper around puck.
    - When the robot's gripper is near puck and the robot's gripper is open, the robot should close gripper around puck.
    - When the robot's gripper is above puck and the robot's gripper is closed, the robot should place puck above wall.

The task `push-wall` requires the