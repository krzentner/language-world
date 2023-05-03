# Steps:
    #  1. Put gripper around door knob
    #  2. Turn dial on the door
    # First, put the gripper around the door knob.
    if check("the robot's gripper is not around the door knob"):
        robot.grab("door knob")
    # If the dial is not lined up with the desired position, turn it.
    if check("the dial is not in the desired position"):
        robot.turn("dial")
    # If the dial is now in the desired position, we're done.
    if check("the dial is in the desired position"):
        robot.release("door knob")

# object-placement: place an object at the desired location
# def object_placement(robot):
    # Steps:
    #  1. Put gripper next to object
    #  2. Grab object with gripper
    #  3. Lift object
    #  4. Move object to desired location
    #  5. Lower object
    # First, put the gripper roughly next to the object.
    if check("the robot's gripper is not next to the object"):
        robot.move("gripper next to object")
    # If the gripper is next to the object, try grabbing it.
    if check("the robot's gripper is next to the object and the robot's gripper is open"):
        robot.grab("object")
    # If the gripper has grasped the object, try lifting it.
    if check("the robot's gripper is holding the object and the object is not lifted"):
        robot.lift("object")
    # If the gripper is holding the object and it's lifted, try moving it to the
    # desired location.
    if check("the robot's gripper is holding the object and the object is lifted and the object is not at the desired location"):
        robot.move("object to desired location")
    # If the gripper is holding the object and it's at the desired location,
    # lower it.
    if check("the robot's gripper is holding the object and the object is at the desired location and the object is not lowered"):
        robot.lower("object")

# object-retrieval: retrieve an object from a specific location
# def object_retrieval(robot):
    # Steps:
    #  1. Put gripper next to object
    #  2. Grab object with gripper
    #  3. Move object to desired location
    # First, put the gripper roughly next to the object.
    if check("the robot's gripper is not next to the object"):
        robot.move("gripper next to object")
    # If the gripper is next to the object, try grabbing it.
    if check("the robot's gripper is next to the object and the robot's gripper is open"):
        robot.grab("object")
    # If the gripper has grasped the object, try moving it to the desired
    # location.
    if check("the robot's gripper is holding the object and the object is not at the desired location"):
        robot.move("object to desired location")