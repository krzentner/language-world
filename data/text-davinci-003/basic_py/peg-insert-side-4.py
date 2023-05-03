
    if check("the peg is not near the robot's gripper and the robot's gripper is open"):
        robot.grab("peg")
    if check("the robot's gripper is closed and the peg is not above the hole"):
        robot.move("peg above the hole")
    if check("the peg is above the hole and the robot's gripper is closed"):
        robot.rotate("peg into the hole")

# plug-in: grab the plug and plug it into the socket
def plug_in(robot):
    if check("the robot's gripper is not near the plug and the robot's gripper is not around the plug"):
        robot.grab("plug")
    if check("the robot's gripper is around the plug and the robot's gripper is  not near the plug"):
        robot.put("plug near socket")
    if check("the robot's gripper is near the socket and the socket is below the robot's gripper"):
        robot.rotate("plug into socket")