
    Steps:
    The box is large enough that we can just push the gripper into the top of the box lid. As long as the gripper isn't vertically aligned with the box lid, move the gripper to the box lid.
    - When the robot's gripper is not above the box lid and the robot's gripper is not above the lid, move the robot's gripper until the robot's gripper is above the box lid
    If the robot's gripper is above the box lid, we can close the gripper on the box lid.
    - When the robot's gripper is above the box lid, move the robot's gripper until the robot's gripper is around the box lid
    Once we've picked up the box lid, the only thing to do is to move the gripper to the box to close it.
    - When the robot's gripper is closed, move the robot's gripper until the robot's gripper is near the box

The task `button-press` requires the robot to press the button.
To press the button reliably, what steps the robot should perform?
    Steps:
    If the gripper isn't near the button, move the gripper to it.
    - When the robot's gripper is not near the button, move the robot's gripper until the robot's gripper is near the button
    - When the robot's gripper is near the button and the robot's gripper is closed, move the robot's gripper until the robot's gripper is around the button
    Once the gripper is around the button, we can push it in.
    - When the robot's gripper is around the button, move the robot's gripper until the robot's gripper is near the button
    - When the robot's gripper is near the button and the robot's gripper is around the button, move the robot's gripper until the robot's gripper is vertically aligned with the button
    Once the gripper is on top of the button, it is probably pressed in, so all that's left to do is to let go of the button.
    - When the robot's gripper is vertically aligned with the button, move the robot's gripper until the robot's gripper is not near the button
    - When the robot's gripper is not near the button and the robot's gripper is around the button, move the robot's gripper until the robot's gripper is not around the button

The task `peg-insert-topdown` requires the robot to grab the peg and insert it