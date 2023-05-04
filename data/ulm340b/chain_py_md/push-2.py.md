

<SOLUTION>
# push: slide the puck to the target location
def push(robot):
    # Steps:
    #  1. Put gripper left of puck
    #  2. Push puck into goal
    if check("the puck is right of the robot's gripper"):
        robot.move("gripper to left of puck")
    if check("the puck is in front of the robot's gripper"):
        robot.slide("puck to goal")
</SOLUTION>
"""
    labels = [
        "button-press-topdown",
        "drawer-open",
        "peg-insert-side",
        "door-open",
        "drawer-close",
        "window-close",
        "window-open",
        "pick-place",
        "reach",
    ]
    steps = {
        "button-press-topdown": ["line up the gripper as viewed from above", "push down on the button from the top"],
        "drawer-open": ["put gripper above drawer handle", "drop gripper around drawer handle", "pull open the drawer"],
        "peg-insert-side": [
            "put gripper above the peg",
            "grab the peg with the gripper",
            "line the peg up with the hole",
            "slide the peg sideways into the hole",
        ],
        "door-open": ["put gripper above door handle", "drop gripper around door handle", "pull open the door"],
        "drawer-close": ["put gripper roughly around the drawer handle", "push the drawer closed"],
        "window-close": [
            "put gripper left of the window handle",
            "start pushing against the window handle to close the window",
            "push the window closed harder",
        ],
        "window-open": [
            "put gripper right of the window handle",
            "start pushing against the window handle to open the window",
            "push the window open harder",
        ],
        "pick-place": [
            "put gripper above puck",
            "drop gripper around puck",
            "close gripper around puck",
            "move puck to goal",
        ],
        "reach": ["reach towards the target"],
        "push": ["put gripper left of puck", "push puck into goal"],
    }
    objects = ["puck", "gripper"]
    robot = Robot()
    description = DESCRIPTION

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self