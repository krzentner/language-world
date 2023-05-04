

The task `peg-insert-top` requires the robot to grab the peg and insert it into the hole from the top.
To grab the peg and insert it into the hole from the top reliably, what steps the robot should perform?

The task `ball-insert-top` requires the robot to grab the ball and insert it into the bowl from the top.
To grab the ball and insert it into the bowl from the top reliably, what steps the robot should perform?

The task `peg-unstack` requires the robot to grab the upper peg and place it away.
To grab the upper peg and place it away reliably, what steps the robot should perform?

The task `pick-place-wall` requires the robot to pick up the puck and hold it over the wall.
To pick up the puck and hold it over the wall reliably, what steps the robot should perform?

The task `ball-insert-side` requires the robot to grab the ball and insert it into the bowl from the side.
To grab the ball and insert it into the bowl from the side reliably, what steps the robot should perform?

The task `ball-push` requires the robot to push the ball to the target location.
To push the ball to the target location reliably, what steps the robot should perform?

The task `box-close` requires the robot to close the box.
To close the box reliably, what steps the robot should perform?
"""


task_id_to_name = {
    "button-press-topdown": "button-press-topdown",
    "drawer-open": "drawer-open",
    "door-open": "door-open",
    "drawer-close": "drawer-close",
    "peg-insert-side": "peg-insert-side",
    "window-close": "window-close",
    "window-open": "window-open",
    "pick-place": "pick-place",
    "reach": "reach",
    "push": "push",
    "plate-slide-side": "plate-slide-side",
    "peg-insert-top": "peg-insert-top",
    "ball-insert-top": "ball-insert-top",
    "peg-unstack": "peg-unstack",
    "pick-place-wall": "pick-place-wall",
    "ball-insert-side": "ball-insert-side",
    "ball-push": "ball-push",
    "box-close": "box-close",
}

all_tasks = [
    "button-press-topdown",
    "drawer-open",
    "door-open",
