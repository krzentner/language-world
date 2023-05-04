

The task `slide` requires the robot to slide the peg along the slider to the target location.
To slide the peg along the slider to the target location reliably, what steps the robot should perform?

The task `vbar` requires the robot to move the vbar to the target location.
To move the vbar to the target location reliably, what steps the robot should perform?

'''


# pylint: disable=line-too-long
instructions = {
    "button-press-topdown": r'''
    The task `button-press-topdown` requires the robot to push the button down from above.
    To push the button down from above reliably, the robot should perform the following steps:
        Steps:  1. Line up the gripper as viewed from above  2. Push down on the button from the top
        Because this is "topdown", we just need to line up the gripper from above. Line up the robot's gripper from above.
        - When the robot's gripper is not vertically aligned with button, the robot should put gripper above button.
        Now that the gripper is lined up, just push down on the button.
        - When the robot's gripper is vertically aligned with button, the robot should push down on button.
    ''',
    "drawer-open": r'''
    The task `drawer-open` requires the robot to pull the drawer open.
    To pull the drawer open reliably, the robot should perform the following steps:
        Steps:  1. Put gripper above drawer handle  2. Drop gripper around drawer handle  3. Pull open the drawer
        We need to put the gripper above the drawer handle before we can grab it, because of the angle of the robot's gripper.
        - When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.
        Once the gripper is lined up above the drawer handle, we should be able to grab the drawer handle by moving the gripper down around it.
        - When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, the robot should put gripper around drawer handle.
        Once the gripper is around the drawer handle, we can just pull the drawer open.
        - When the robot's gripper is around drawer handle, the robot should pull away from drawer.
    ''',
    "peg-insert-side": r'''
    The task `peg-insert-side` requires the robot to grab the peg and insert it into the hole from the side.
    To grab the peg and insert it into the