

    Steps:  1. Put gripper above mug  2. Drop gripper around mug  3. Close gripper around mug  4. Move mug to goal

To grab the mug and pull it to the target location reliably, the robot should perform the following steps:
    First, put the gripper above mug so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above mug, the robot should place gripper above mug.
    If the gripper isn't around the mug, put it around the mug.
    - When the robot's gripper is not around mug and the robot's gripper is open, the robot should drop gripper around mug.
    If the gripper is near the mug and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near mug and the robot's gripper is open, the robot should close gripper around mug.
    We closed the gripper, and the mug is still near the gripper, so maybe we grabbed it. Try to move the mug to the goal. If we didn't grab it, we'll just go back to an earlier step.
    - When the robot's gripper is above mug and the robot's gripper is closed, the robot should place mug at goal.

The task `relocate` requires the robot to pick up the object and put it in the goal.
To pick up the object and put it in the goal reliably, what steps the robot should perform?

    Steps:  1. Put gripper above object  2. Drop gripper around object  3. Close gripper around object  4. Move object to goal

To pick up the object and put it in the goal reliably, the robot should perform the following steps:
    First, put the gripper above object so that we don't bump it while trying to grab it.
    - When the robot's gripper is not above object, the robot should place gripper above object.
    If the gripper isn't around the object, put it around the object.
    - When the robot's gripper is not around object and the robot's gripper is open, the robot should drop gripper around object.
    If the gripper is near the object and open, maybe we can grab it by closing the gripper.
    - When the robot's gripper is near object and the robot's gripper is open, the robot should close gripper around object.
    We closed the gripper, and the object is still near the gripper, so