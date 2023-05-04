
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")

def make_target_action_pair(action):
    if action == "reach":
        return reach
    if action == "button-press-topdown":
        return button_press_topdown
    if action == "peg-insert-side":
        return peg_insert_side
    if action == "drawer-close":
        return drawer_close
    if action == "drawer-open":
        return drawer_open
    if action == "door-open":
        return door_open
    if action == "pick-place":
        return pick_place
    if action == "push":
        return push
    if action == "window-close":
        return window_close
    if action == "window-open":
        return window_open
    # if action == "window-open-hand":
    #     return window_open_hand
    # if action == "window-close-hand":
    #     return window_close_hand

    # if action == "door-close":
    #     return door_close
    # if action == "door-open-turn":
    #     return door_open_turn
    # if action == "door-close-hand":
    #     return door_close_hand
    # if action == "dial-safe":
    #     return dial_safe
    # if action == "dial-microwave":
    #     return dial_microwave
    # if action == "door-close-hand":
    #     return door_close_hand
    # if action == "drawer-open-angled":
    #     return drawer_open_angled
    # if action == "window-open-hand":
    #     return window_open_hand
    # if action == "pick-place-angled":
    #     return pick_place_angled
    # if action ==