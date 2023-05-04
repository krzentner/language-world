
    if check("the robot's gripper is not vertically aligned with the mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is not around mug"):
        robot.grab("mug")
    if check("the robot's gripper is around the mug"):
        robot.move("mug to goal")

# coffee-pull: grab the mug and move it to the target location
def coffee_pull(robot):
    if check("the robot's gripper is not vertically aligned with the mug"):
        robot.put("gripper above mug")
    if check("the robot's gripper is not around mug"):
        robot.grab("mug")
    if check("the robot's gripper is around the mug"):
        robot.move("mug to goal")

# towel-pull: grab the towel and move it to the target location
def towel_pull(robot):
    if check("the robot's gripper is not vertically aligned with the towel"):
        robot.put("gripper above towel")
    if check("the robot's gripper is not around towel"):
        robot.grab("towel")
    if check("the robot's gripper is around the towel"):
        robot.move("towel to goal")

# towel-push: grab the towel and move it to the target location
def towel_push(robot):
    if check("the robot's gripper is not vertically aligned with the towel"):
        robot.put("gripper above towel")
    if check("the robot's gripper is not around towel"):
        robot.grab("towel")
    if check("the robot's gripper is around the towel"):
        robot.move("towel to goal")

# peg-insert-side-wall: grab the peg and insert it into the hole from the side
def peg_insert_side_wall(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not forward aligned with the robot's gripper and peg is not left aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):