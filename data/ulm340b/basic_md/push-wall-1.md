
- When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
- When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
- When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck to the goal.

The task `stack` requires the robot to put the smaller puck on top of the bigger puck.
To put the smaller puck on top of the bigger puck reliably, what steps the robot should perform?
- When the robot's gripper is not above smaller puck, the robot should put gripper above smaller puck.
- When the robot's gripper is above smaller puck and the robot's gripper is not near smaller puck, the robot should drop gripper into smaller puck.
- When the robot's gripper is near smaller puck and the robot's gripper is open, the robot should close gripper around smaller puck.
- When the robot's gripper is closed and the robot's gripper is above smaller puck, the robot should lift gripper out of smaller puck.
- When the robot's gripper is above bigger puck and the robot's gripper is not near bigger puck, the robot should place gripper above bigger puck.
- When the robot's gripper is near bigger puck and the robot's gripper is above bigger puck, the robot should drop smaller puck onto bigger puck.

The task `unstack` requires the robot to lift the smaller puck from the top of the bigger puck.
To lift the smaller puck from the top of the bigger puck reliably, what steps the robot should perform?
- When the robot's gripper is not near smaller puck, the robot should place gripper above smaller puck.
- When the robot's gripper is above smaller puck, the robot should drop gripper into smaller puck.
- When the robot's gripper is near smaller puck and the robot's gripper is open, the robot should close gripper around smaller puck.
- When the robot's gripper is closed and the robot's gripper is above smaller puck, the robot should lift gripper out of smaller puck.

The task `cleanup` requires the robot to place the small puck and the large puck in the bin.
To place the small puck and the large puck in the bin reliably, what steps the robot should perform?
- When the robot's gripper is not above smaller puck, the robot should put gripper above smaller puck.
- When the robot's gripper is above smaller puck and