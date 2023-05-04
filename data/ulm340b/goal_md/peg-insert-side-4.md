

The task `peg-unstack` requires the robot to grab the peg and move it to the goal location.
To grab the peg and move it to the goal location reliably, what steps the robot should perform?

The task `peg-insert-top` requires the robot to grab the peg and insert it into the hole from the top.
To grab the peg and insert it into the hole from the top reliably, what steps the robot should perform?

The task `block-insert-side` requires the robot to grab the block and insert it into the hole from the side.
To grab the block and insert it into the hole from the side reliably, what steps the robot should perform?

The task `block-insert-top` requires the robot to grab the block and insert it into the hole from the top.
To grab the block and insert it into the hole from the top reliably, what steps the robot should perform?

The task `block-push` requires the robot to grab the block and slide it to the target location.
To grab the block and slide it to the target location reliably, what steps the robot should perform?

The task `sweep` requires the robot to push the eraser to the target location.
To push the eraser to the target location reliably, the robot should perform the following steps:
    Steps:  1. Put gripper above eraser  2. Push gripper into top of eraser  3. Slide eraser to goal
    The robot can slide the eraser by trapping it by pushing down on it from above and moving the gripper. If the eraser isn't below the gripper as seen from above, move the gripper above the eraser.
    - When the robot's gripper is not above eraser and the robot's gripper is not vertically aligned with eraser, move the robot's gripper until the robot's gripper is vertically aligned with eraser
    If the gripper is aligned with the eraser but not near it, move the gripper down to the eraser to slide it.
    - When the robot's gripper is vertically aligned with eraser and the robot's gripper is not near eraser, move the robot's gripper until the robot's gripper is above eraser and the robot's gripper is closed
    If the gripper is near the eraser, we've probably trapped the eraser and can slide it to the target location. Close the gripper to make sure we keep control of the eraser.
    - When the robot's gripper is near the eraser and the eraser is below the robot's gripper, move the robot's gripper until the robot's gripper is above the target location



Instructions:

1. Please describe the goal of the task in