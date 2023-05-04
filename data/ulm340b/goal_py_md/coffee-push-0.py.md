

### Test case
```
test_tasks = [
    # [ task, robot_type ]
    ["button-press-topdown", "pr2"],
    ["drawer-open", "pr2"],
    ["drawer-close", "pr2"],
    ["door-open", "pr2"],
    ["window-close", "pr2"],
    ["window-open", "pr2"],
    ["peg-insert-side", "pr2"],
    ["push", "pr2"],
    ["reach", "pr2"],
    ["pick-place", "pr2"],
]


def check_task(task, robot_type):
    robot = {
        "pr2": 1,
    }[robot_type]

    if task not in test_tasks:
        return False

    steps = {
        "button-press-topdown": [
            ("the robot's gripper is not vertically aligned with button", 1),
            ("the robot's gripper is vertically aligned with button and the robot's gripper is not near button", 2),
        ],
        "drawer-open": [
            ("the robot's gripper is not vertically aligned with drawer handle", 1),
            ("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle", 2),
            ("the robot's gripper is around drawer handle and the robot's gripper is not horizontally aligned with drawer handle", 3),
        ],
        "drawer-close": [
            ("the robot's gripper is not near drawer handle", 1),
            ("the robot's gripper is near drawer handle and the robot's gripper is not around drawer handle", 2),
        ],
        "door-open": [
            ("the robot's gripper is not almost vertically aligned with door handle", 1),
            ("the robot's gripper is almost vertically aligned with door handle and the robot's gripper is not left of the door handle", 2),
        ],
        "window-close": [
            ("the robot's gripper is in front of the window handle", 1),
            ("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle", 2),
            ("the robot's gripper is near the window handle", 3),
        ],
        "window-open": [
            ("the robot's gripper is not near the window handle", 1),
            ("the robot's gripper is near