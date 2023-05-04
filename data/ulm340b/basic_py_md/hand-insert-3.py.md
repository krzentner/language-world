

"""

def hand_insert(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")


# t0_code = '''# button-press-topdown: push the button down from above
# def button_press_topdown(robot):
#     if check("the robot's gripper is not vertically aligned with button"):
#         robot.put("gripper above button")
#     if check("the robot's gripper is vertically aligned with button"):
#         robot.push("down on button")

# # drawer-open: pull the drawer open
# def drawer_open(robot):
#     if check("the robot's gripper is not vertically aligned with drawer handle"):
#         robot.put("gripper above drawer handle")
#     if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
#         robot.put("gripper around drawer handle")
#     if check("the robot's gripper is around drawer handle"):
#         robot.pull("away from drawer")

# # drawer-close: push the drawer close
# def drawer_close(robot):
#     if check("the robot's gripper is not near the drawer handle"):
#         robot.grab("drawer handle")
#     if check("the robot's gripper is forward aligned with drawer handle"):
#         robot.push("drawer closed")

# # door-open: pull the door open
# def door_open(robot):
#     if check("the robot's gripper is not almost vertically aligned with door handle"):
#         robot.put("gripper above door handle")
#     if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
#         robot.put("gripper around door handle")
#     if check("the robot's gripper is vertically aligned with the door handle"):
#         robot.pull("door open")

