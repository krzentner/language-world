

and then add to it until the robot can perform the task `basketball`.

You may click "Check" at any time to see how well your program completes the tasks you've already written.

Please write a program to perform all twelve tasks:

- [ ] [reach](#reach): reach to the target location
- [ ] [door-open](#door_open): pull the door open
- [ ] [drawer-close](#drawer_close): push the drawer closed
- [ ] [push](#push): slide the puck to the target location
- [ ] [button-press-topdown](#button_press_topdown): push the button down from above
- [ ] [drawer-open](#drawer_open): pull the drawer open
- [ ] [pick-place](#pick_place): pick up the puck and hold it at the target location
- [ ] [window-close](#window_close): slide the window closed to the right
- [ ] [window-open](#window_open): slide the window open to the left
- [ ] [peg-insert-side](#peg_insert_side): grab the peg and insert it into the hole from the side
- [ ] [basketball](#basketball): put the ball into into the hoop
""".format(
        reach=_name_task_def(reach_fn, True),
        door_open=_name_task_def(door_open_fn, True),
        drawer_close=_name_task_def(drawer_close_fn, True),
        push=_name_task_def(push_fn, True),
        button_press_topdown=_name_task_def(button_press_topdown_fn, True),
        drawer_open=_name_task_def(drawer_open_fn, True),
        pick_place=_name_task_def(pick_place_fn, True),
        window_close=_name_task_def(window_close_fn, True),
        window_open=_name_task_def(window_open_fn, True),
        peg_insert_side=_name_task_def(peg_insert_side_fn, True),
        basketball=_name_task_def(task, True))


_ALL_TASK_DESCRIPTS = {
    "reach": "Reach",
    "door_open": "Door open",
    "drawer_close": "Drawer close",
    "push": "Push",
    "button_press_topdown": "Top down button press",
    "drawer_open": "Drawer open",
    "pick_place":