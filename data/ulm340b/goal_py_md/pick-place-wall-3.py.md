

"""



import json

def check(property):
    return property in json.loads("""
    {"window handle":"near","wall":"near","drawer handle":"near","door handle":"near","button":"near","peg":"near","hole":"near","puck":"near","reach target":"near"}
    """)

def move_gripper(direction, close_gripper=False):
    if direction in json.loads("""
    {"near","vertically aligned with","almost vertically aligned with","left of","right of","around","above","below","horizontally aligned with"}
    """):
        print("moving in the direction %s" % direction)
    else:
        print("Can not move to %s" % direction)

    print(json.dumps({"robot gripper position": "near the puck"}, indent=4))
    if close_gripper:
        print(json.dumps({"robot gripper state": "closed"}, indent=4))
    else:
        print(json.dumps({"robot gripper state": "open"}, indent=4))

def window_close(robot):
    # Steps:
    #  1. Put gripper left of the window handle
    #  2. Start pushing against the window handle to close the window
    #  3. Push the window closed harder
    # If the the window handle is right of the robot's gripper, we should move the
    # gripper near the window handle to start pushing
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("right of the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window close now by moving the gripper right.
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move_gripper("almost vertically aligned with the window handle")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("forward aligned with the window handle")

def window_open(robot):
    # Steps:
    #  1. Put gripper right of the window handle
    #  2. Start pushing against the window handle to