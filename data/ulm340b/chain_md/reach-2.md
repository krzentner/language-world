
    There's no object, just move the gripper to the goal location.
    - When the robot's gripper is not at the goal location, the robot should reach toward the goal.
""".splitlines()

# # A demonstration of the task
task_demonstrations = {'peg-insert-side': """
P1:  <move gripper above peg> <grab peg> <line peg up with hole> <insert peg into hole>
P2:  <move gripper above peg> <grab peg> <line peg up with hole> <insert peg into hole>
P3:  <move gripper above peg> <grab peg> <line peg up with hole> <insert peg into hole>
""",
        'button-press-topdown': """
P1:  <move gripper above button> <press down on button>
P2:  <move gripper above button> <press down on button>
P3:  <move gripper above button> <press down on button>
""",
        'door-open': """
P1:  <move gripper above door handle> <grab door handle> <pull door open>
P2:  <move gripper above door handle> <grab door handle> <pull door open>
P3:  <move gripper above door handle> <grab door handle> <pull door open>
""",
        'window-close': """
P1:  <move gripper left of the window handle> <slide window right> <push window right harder>
P2:  <move gripper left of the window handle> <slide window right> <push window right harder>
P3:  <move gripper left of the window handle> <slide window right> <push window right harder>
""",
        'drawer-open': """
P1:  <move gripper above drawer handle> <grab drawer handle> <pull drawer open>
P2:  <move gripper above drawer handle> <grab drawer handle> <pull drawer open>
P3:  <move gripper above drawer handle> <grab drawer handle> <pull drawer open>
""",
        'window-open': """
P1:  <move gripper right of the window handle> <slide window left> <push window left harder>
P2:  <move gripper right of the window handle> <slide window left> <push window left harder>
P3:  <move gripper right of the window handle> <slide window left> <push window left harder>
""",
        'drawer-close': """
P1:  <move gripper around drawer handle> <