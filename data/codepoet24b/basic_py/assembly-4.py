# push: slide the puck to the target location
def push(robot):
    if check("the robot's gripper is not above puck and the robot's gripper is not vertically aligned with the puck"):
        robot.put("the gripper above the puck")
    if check("the robot's gripper is vertically aligned with the puck and the robot's gripper is not near puck"):
        robot.push("the gripper into the puck")
    if check("the robot's gripper is near the puck and the puck is below the robot's gripper"):
        robot.slide("the puck to the goal")

# button-press-topdown: push the button down from above
def button_press_topdown(robot):
    if check("the robot's gripper is not vertically aligned with button"):
        robot.put("gripper above button")
    if check("the robot's gripper is vertically aligned with button"):
        robot.push("down on button")

# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")

# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.pull("door open")

# drawer-close: push the drawer close
def drawer_close(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

# drawer-open: pull the drawer open
def drawer_open(robot):
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.put("gripper around drawer handle")
    if check("the robot's gripper is around drawer handle"):
        robot.pull("away from drawer")

# pick-place: pick up the puck and hold it at the target location
def pick_place(robot):
    if check("the robot's gripper is not above the puck"):
        robot.place("gripper above puck")
    if check("the robot's gripper is not around puck and the robot's gripper is open"):
        robot.drop("gripper around puck")
    if check("the robot's gripper is near puck and the robot's gripper is open"):
        robot.close("gripper around puck")
    if check("the robot's gripper is above puck and the robot's gripper is closed"):
        robot.place("puck at goal")

# window-close: slide the window closed to the right
def window_close(robot):
    if check("the window handle is right of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move("gripper to left of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window right")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window right harder")

# window-open: slide the window open to the left
def window_open(robot):
    if check("the robot's gripper is not vertically aligned with the window handle and the robot's gripper is below the window handle"):
        robot.move("gripper to right of window handle")
    if check("the robot's gripper is near the window handle"):
        robot.slide("window left")
    if check("the robot's gripper is in front of the window handle"):
        robot.push("window left harder")

# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole")

# assembly: grab the wrench and wrap it around the peg
def assembly(robot):
    if check("the robot's gripper is not near the wrench"):
        robot.reach("to wrench")
    if check("the robot's gripper is near the wrench and the robot's gripper is not around the wrench"):
        robot.grab("wrench")
    if check("the robot's gripper is around the wrench and the wrench is not near peg"):
        robot.move("wrench to peg")
    if check("the robot's gripper is near peg and the peg is not horizontal"):
        robot.rotate("wrench to horizontal")
    if check("the robot's gripper is near peg and the peg is horizontal"):
        robot.wrap("wrench around peg")


# if __name__ == "__main__":
#     robot = Robot("robot")
#     push(robot)
#     button_press_topdown(robot)
#     reach(robot)
#     door_open(robot)
#     drawer_close(robot)
#     drawer_open(robot)
#     pick_place(robot)
#     window_close(robot)
#     window_open(robot)
#     peg_insert_side(robot)
#     assembly(robot)


# def check(status):
#     print("Checking if " + status + ".")
#     if eval(status):
#         print("Verified that " + status + ".")
#     else:
#         print("ERROR: " + status + " failed.")


# print("Robot test starting...")
# push(robot)
# print("push complete...")
# button_press_topdown(robot)
# print("button_press_topdown complete...")
# reach(robot)
# print("reach complete...")
# door_open(robot)
# print("door_open complete...")
# drawer_close(robot)
# print("drawer_close complete...")
# drawer_open(robot)
# print("drawer_open complete...")
# pick_place(robot)
# print("pick_place complete...")
# window_close(robot)
# print("window_close complete...")
# window_open(robot)
# print("window_open complete...")
# peg_insert_side(robot)
# print("peg_insert_side complete...")
# assembly(robot)
# print("assembly complete...")
# print("Robot test complete...")


def check(status):
    print("Checking if " + status + ".")
  