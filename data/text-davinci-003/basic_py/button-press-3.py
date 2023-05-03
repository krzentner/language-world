
    if check("the robot's gripper is not forward aligned with button"):
        robot.move("gripper in front of button")
    if check("the robot's gripper is forward aligned with the button"):
        robot.push("button")

# pick-store: pick up the puck and place it in the bin
def pick_store(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck in bin")