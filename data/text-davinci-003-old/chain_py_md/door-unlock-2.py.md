

The steps for the program are:

1. Put gripper above door lock
2. Drop gripper around door lock
3. Turn the dial on the door

# door-unlock: turn the dial on the door
# def door_unlock(robot):
    # Steps:
    #  1. Put gripper above door lock
    #  2. Drop gripper around door lock
    #  3. Turn the dial on the door
    # We need to put the gripper above the door lock before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with door lock"):
        robot.put("gripper above door lock")
    # Once the gripper is lined up above the door lock, we should be able to
    # grab the door lock by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with door lock and the robot's gripper is not around door lock"):
        robot.put("gripper around door lock")
    # Once the gripper is around the door lock, we can just turn the dial.
    if check("the robot's gripper is around door lock"):
        robot.turn("dial on door")