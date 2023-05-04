

Then continue the program using the same style as before.

Thank you for your help!

''')

def check(desc):
    return True

def robot_put(verb, arg):
    print("robot put %s %s" % (verb, arg))

def robot_push(verb, arg):
    print("robot push %s %s" % (verb, arg))

def robot_slide(verb, arg):
    print("robot slide %s %s" % (verb, arg))

def robot_pull(verb, arg):
    print("robot pull %s %s" % (verb, arg))

def robot_align(verb, arg):
    print("robot align %s %s" % (verb, arg))

def robot_grab(verb, arg):
    print("robot grab %s %s" % (verb, arg))

def robot_move(verb, arg):
    print("robot move %s %s" % (verb, arg))

def robot_insert(verb, arg):
    print("robot insert %s %s" % (verb, arg))

def robot_reach(verb, arg):
    print("robot reach %s %s" % (verb, arg))

def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot_put("gripper above button")
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot_push("down on button")

def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot_put("gripper above drawer handle")
  