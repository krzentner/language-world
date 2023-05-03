
    if check("the robot's gripper is not near the door handle"):
        robot.grab("door handle")
    if check("the robot's gripper is near the door handle and the robot's gripper is open"):
        robot.close("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.pull("pull away from door")

# latch-turn-close: turn the latch to close the gate
def latch_turn_close(robot):
    if check("the robot's gripper is not near the latch"):
        robot.grab("latch")
    if check("the robot's gripper is near the latch and the robot's gripper is open"):
        robot.close("gripper around latch")
    if check("the robot's gripper is around latch and the latch is open"):
        robot.turn("gripper clockwise")
    if check("the robot's gripper is around latch and the latch is not open"):
        robot.pull("gripper away from latch")