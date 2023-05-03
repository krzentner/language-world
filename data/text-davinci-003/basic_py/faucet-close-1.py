
    if check("the robot's gripper is not near the faucet handle"):
        robot.place("gripper near faucet handle")
    if check("the robot's gripper is near the faucet handle and the robot's gripper is open"):
        robot.close("gripper around faucet handle")
    if check("the robot's gripper is around the faucet handle"):
        robot.turn("faucet right")

# light-off: flip the light switch down
def light_off(robot):
    if check("the robot's gripper is not above the light switch"):
        robot.put("gripper above the light switch")
    if check("the robot's gripper is vertically aligned with the light switch and the robot's gripper is not near the light switch"):
        robot. grip("gripper around the light switch")
    if check("robot's gripper is near the light switch"):
        robot.flip("light switch down")