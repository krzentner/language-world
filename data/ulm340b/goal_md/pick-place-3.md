
    Please type them below. If you have multiple steps, please separate them by newlines.
    <AnswerPlaceholder>

The task `pick-place-side` requires the robot to pick up the peg and hold it on the side at the target location.
To pick up the peg and hold it on the side at the target location reliably, what steps the robot should perform?
    Please type them below. If you have multiple steps, please separate them by newlines.
    <AnswerPlaceholder>

The task `drawer-open-topdown` requires the robot to push the drawer open from above.
To push the drawer open from above reliably, the robot should perform the following steps:
    Steps:  1. Line up gripper  2. Drop gripper to the drawer handle  3. Push the drawer open
    First, we need to line the robot's gripper up from above.
    - When the robot's gripper is not vertically aligned with drawer handle, move the robot's gripper until the robot's gripper is vertically aligned with the drawer handle
    As long as the gripper is lined up with the drawer handle, we should be able to open the drawer by moving the gripper to the drawer handle.
    - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not near drawer handle, move the robot's gripper until the robot's gripper is near the drawer handle
    As long as the robot's gripper is near the drawer handle, we can probably open the drawer now by moving the gripper left.
    - When the robot's gripper is near drawer handle and the robot's gripper is not left of the drawer handle, move the robot's gripper until the robot's gripper is left of the drawer handle

The task `drawer-close-topdown` requires the robot to push the drawer closed from above.
To push the drawer closed from above reliably, the robot should perform the following steps:
    Steps:  1. Line up the gripper from above  2. Move the gripper in front of the drawer handle  3. Push the drawer closed
    First, we need to line the robot's gripper up from above.
    - When the robot's gripper is not almost vertically aligned with drawer handle, move the robot's gripper until the robot's gripper is almost vertically aligned with the drawer handle
    As long as the gripper is lined up with the drawer handle, we can probably close the drawer now by moving the gripper down and forward.
    - When the robot's gripper is in front of the drawer handle, move