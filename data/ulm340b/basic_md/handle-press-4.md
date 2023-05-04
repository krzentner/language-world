
''')


def get_skill_desc(task, i=0):
    skills = {
        'peg-insert-side': '''
        When the robot's gripper is not vertically aligned with the peg, the robot should put gripper above peg.
        When peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper, the robot should grab peg.
        When the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole, the robot should align peg to hole.
        When peg is horizontally aligned with hole, the robot should insert peg into hole.''',
        'push': '''
        When the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck, the robot should put the gripper above the puck.
        When the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck, the robot should push the gripper into the puck.
        When the robot's gripper is near the puck and the puck is below the robot's gripper, the robot should slide the puck to the goal.''',
        'window-close': '''
        When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, the robot should move gripper to left of window handle.
        When the robot's gripper is near the window handle, the robot should slide window right.
        When the robot's gripper is in front of the window handle, the robot should push window right harder.''',
        'window-open': '''
        When the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle, the robot should move gripper to right of window handle.
        When the robot's gripper is near the window handle, the robot should slide window left.
        When the robot's gripper is in front of the window handle, the robot should push window left harder.''',
        'reach': '''
        When the robot's gripper is not near reach target, the robot should reach to goal.''',
        'drawer-open': '''
        When the robot's gripper is not vertically aligned with drawer handle, the robot should put gripper above drawer handle.
        When the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle, the robot should put gripper around drawer handle.
        When the robot's gripper is around drawer handle, the robot should pull away from drawer.''',
