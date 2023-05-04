

And then write a series of lines like those in the example.
You are welcome to run a few steps at a time, using the button in the bottom-right, and see if the program behaves the way you would like.

''',

  'examples': [
    '# open-cabinet: open the drawer of the cabinet',
    'def open_cabinet(robot):',
    '    # Steps:',
    '    #  1. Line up the gripper as viewed from above',
    '    #  2. Push down on the cabinet handle from the top',
    '    # Because this is "topdown", we just need to line up the gripper from above.',
    '    # Line up the robot\'s gripper from above.',
    '    if check("the robot\'s gripper is not vertically aligned with cabinet handle"):',
    '        robot.put("gripper above cabinet handle")',
    '    # Now that the gripper is lined up, just push down on the cabinet handle.',
    '    if check("the robot\'s gripper is vertically aligned with cabinet handle"):',
    '        robot.push("down on cabinet handle")',
    ''
  ],

  'expected_answer': [
    '''
# box-close: pick up the box lid and place it on the box
def box_close(robot):
    # Steps:
    #  1. Put gripper above box lid
    #  2. Drop gripper around box lid
    #  3. Close gripper around box lid
    #  4. Move the box lid to the box
    # First, put the gripper roughly above box lid, so that we don't bump it while trying to grab it.
    if check("the robot's gripper is not above box lid"):
        robot.place("gripper above box lid")
    # If the gripper isn't around the box lid, put it around the box lid.
    if check("the robot's gripper is not around box lid and the robot's gripper is open"):
        robot.drop("gripper around box lid")
    # If the gripper is near the box lid and open, maybe we can grab it by closing the gripper.
    if check("the robot's gripper is near box lid and the robot's gripper