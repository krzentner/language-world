
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is above the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is to the right of the window handle"):
        robot.push("window right harder")

# latch-press: push the latch down with the robot's gripper
def latch_press(robot):
    if check("the robot's gripper is not vertically aligned with the latch"):
        robot.place("gripper above latch")
    if check("the robot's gripper is vertically aligned with latch"):
        robot.push("latch down")


# # pick-place-wall: pick up the puck and hold it at the target location while starting right next to the wall
# def pick_place_wall(robot):
#     if check("the robot's gripper is not above the puck"):
#         robot.place("gripper above puck")
#     if check("the robot's gripper is not around puck and the robot's gripper is open"):
#         robot.drop("gripper around puck")
#     if check("the robot's gripper is near puck and the robot's gripper is open"):
#         robot.close("gripper around puck")
#     if check("the robot's gripper is above puck and the robot's gripper is closed"):
#         robot.place("puck at goal")

# pull-drawer: pull the drawer open
# def pull_drawer(robot):
#     if check("the robot's gripper is not vertically aligned with drawer handle"):
#         robot.place("gripper above drawer handle")
#     if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
#         robot.place("gripper around drawer handle")
#     if check("the robot's gripper is around drawer handle"):
#         robot.pull("away from drawer")

# window-close-v2: slide the window closed to the right
# def window_close_v2(robot):
#     if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
#         robot.move("gripper to right of window handle")
#     if check("the robot'