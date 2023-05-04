
    - When the robot's gripper is not aligned with the plate, the robot should put the gripper above the plate.
    - When the plate is not horizontally aligned with the goal, the robot should slide the plate sideways.
    - When the plate is in front of the robot's gripper, the robot should put the gripper above the plate.
    - When the plate is horizontaly aligned with the goal, the robot should move the plate sideways towards the goal.

The task `plate-slide-side-back` requires the robot to slide the plate sideways into the target location.
To slide the plate sideways into the target location reliably, what steps the robot should perform?
    - When the plate is not horizontaly aligned with the goal, the robot should move the plate sideways towards the goal.
    - When the plate is in front of the robot's gripper, the robot should put the gripper above the plate.
    - When the robot's gripper is not aligned with the plate, the robot should put the gripper above the plate.
    - When the plate is horizontaly aligned with the goal, the robot should slide the plate sideways.

"""


def get_tutorial_text(tutorial_id):
    if tutorial_id == 'button-press-topdown':
        return BUTTON_PRESS_TOPDOWN
    if tutorial_id == 'drawer-open':
        return DRAWER_OPEN
    if tutorial_id == 'drawer-close':
        return DRAWER_CLOSE
    if tutorial_id == 'door-open':
        return DOOR_OPEN
    if tutorial_id == 'peg-insert-side':
        return PEG_INSERT_SIDE
    if tutorial_id == 'window-open':
        return WINDOW_OPEN
    if tutorial_id == 'window-close':
        return WINDOW_CLOSE
    if tutorial_id == 'pick-place':
        return PICK_PLACE
    if tutorial_id == 'reach':
        return REACH
    if tutorial_id == 'push':
        return PUSH
    if tutorial_id == 'plate-slide-side':
        return PLATE_SLIDE_SIDE
    if tutorial_id == 'plate-slide-side-back':
        return PLATE_SLIDE_SIDE_BACK
    if tutorial_id == 'reach-over-wall':
        return REACH_OVER_WALL
    if tutorial_id == '