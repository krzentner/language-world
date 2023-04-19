

Solution: 

# door-close: push the door closed to the target location
# def door_close(robot):
    # Steps:
    #  1. Put gripper near the door handle
    #  2. Put gripper around door handle
    #  3. Push the door closed
    # First, move the gripper near the door handle.
    if check("the robot's gripper is not near the door handle"):
        robot.move("gripper near door handle")
    # Now we can grab the door handle with the gripper.
    if check("the robot's gripper is near the door handle and the robot's gripper is open"):
        robot.grab("door handle")
    # Now that we have the door handle, we can push the door closed.
    if check("the robot's gripper is around the door handle"):
        robot.push("door closed")