


The task `pick-place-angled` requires the robot to pick up the puck and hold it at the target location.
To pick up the puck and hold it at the target location reliably, what steps the robot should perform?


The task `window-open-2` requires the robot to slide the window open to the left.
To slide the window open to the left reliably, what steps the robot should perform?




"""


# For each subtask, we want to specify a list of condition-action pairs
# that describe how the robot should perform the subtask.
subtask_dict = {}
subtask_dict["button-press-topdown"] = [
    [
        "gripper not-vertical-align-button",
        "put gripper above button"
    ],
    [
        "gripper vertical-align-button",
        "push down on button"
    ]
]
subtask_dict["drawer-open"] = [
    [
        "gripper not-vertical-align-drawer-handle",
        "put gripper above drawer handle"
    ],
    [
        "gripper vertical-align-drawer-handle not-around-drawer-handle",
        "put gripper around drawer handle"
    ],
    [
        "gripper around-drawer-handle",
        "pull away from drawer"
    ]
]
subtask_dict["door-open"] = [
    [
        "gripper not-almost-vertical-align-door-handle",
        "put gripper above door handle"
    ],
    [
        "gripper almost-vertical-align-door-handle not-around-door-handle",
        "put gripper around door handle"
    ],
    [
        "gripper vertical-align-door-handle",
        "pull door open"
    ]
]
subtask_dict["drawer-close"] = [
    [
        "gripper not-near-drawer-handle",
        "grab drawer handle"
    ],
    [
        "gripper forward-align-drawer-handle",
        "push drawer closed"
    ]
]
subtask_dict["peg-insert-side"] = [
    [
        "gripper not-vertical-align-peg",
        "put gripper above peg"
    ],
    [
        "peg not-left-gripper not-forward-align-gripper",
        "grab peg"
    ],
    [
        "gripper forward-align-peg peg not-horizontal-align-hole",
        "align peg to hole"
    ],
    [