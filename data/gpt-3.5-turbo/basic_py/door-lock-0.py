def door_lock(robot):
    if check("the robot's gripper is not near the door lock"):
        robot.move("gripper to door lock")
    if check("the robot's gripper is around the door lock and the dial is not at the correct combination"):
        robot.turn("the dial to the correct combination")
    if check("the dial is at the correct combination"):
        robot.push("the lock button to lock the door")