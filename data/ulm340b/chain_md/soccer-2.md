
    - When the ball is not at goal, the robot should push ball to goal.

The task `pick-place-side` requires the robot to pick up the puck from the side and hold it at the target location.
To pick up the puck from the side and hold it at the target location reliably, what steps the robot should perform?
    - When the puck is not at goal, the robot should push ball to goal.

The task `push-side` requires the robot to slide the puck to the target location sideways.
To slide the puck to the target location sideways reliably, what steps the robot should perform?
    - When the puck is not at goal, the robot should push ball to goal.

The task `button-press-side` requires the robot to press the button from the side.
To press the button from the side reliably, what steps the robot should perform?
    - When the button is not pressed, the robot should press the button.

The task `pick-out-of-hole` requires the robot to pick up the peg out of the hole.
To pick up the peg out of the hole reliably, what steps the robot should perform?
    - When the peg is not at goal, the robot should pull the peg out of the hole.

The task `pick-out-of-hole-side` requires the robot to pick up the peg out of the hole from the side.
To pick up the peg out of the hole from the side reliably, what steps the robot should perform?
    - When the peg is not at goal, the robot should pull the peg out of the hole.

The task `soccer-side` requires the robot to kick the soccer ball into the target location.
To kick the soccer ball into the target location reliably, what steps the robot should perform?
    - When the ball is not at goal, the robot should push ball to goal.
"""


def task_specific_hints_for_task(task_name, n_hints):
    if task_name == 'reach':
        return _reach_hints
    elif task_name == 'pick-place':
        return _pick_place_hints
    elif task_name == 'push':
        return _push_hints
    elif task_name == 'pick-place-side':
        return _pick_place_side_hints
    elif task_name == 'push-side':
        return _push_side_hints
    elif task_name == 'button-press-side':
        return _button_press_side_hints
    elif task_name == 'pick-out-of-hole':
