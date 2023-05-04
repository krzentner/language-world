
    # Steps:
    #  1. Put gripper above the door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # First, put the gripper above the door handle.
    if check("the robot's gripper is not above door handle"):
        robot.put("gripper above door handle")
    # Once the gripper is above the door handle, we should be able to grab it by
    # moving the gripper around it.
    if check("the robot's gripper is above door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    # Once the gripper is around the door handle, we can just pull the door
    # open.
    if check("the robot's gripper is around door handle"):
        robot.pull("door open")

# knob-turn-cw: turn the knob 90 degrees clockwise
def knob_turn_cw(robot):
    # Steps:
    #  1. Put gripper in front of the knob
    #  2. Push on the knob to get it to rotate
    #  3. Push harder on the knob
    # To rotate the knob clockwise, we should start from the right of it.
    # If the robot's gripper is not right of the knob, move the gripper to the
    # right of the knob.
    if check("the robot's gripper is not right of the knob"):
        robot.move("the robot's gripper right of the knob")
    # If the robot's gripper is in front of the knob, push left.
    if check("the robot's gripper is in front of the knob"):
        robot.push("knob left")
    # If the robot's gripper is left of the knob, push harder.
    if check("the robot's gripper is left of the knob"):
        robot.push("knob harder")

# knob-turn-ccw: turn the knob 90 degrees counterclockwise
def knob_turn_ccw(robot):
    # Steps:
    #  1. Put gripper left of the knob
    #  2. Push on the knob to get it to rotate
    #  3. Push harder on the knob
   