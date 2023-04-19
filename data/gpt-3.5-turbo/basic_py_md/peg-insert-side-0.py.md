# peg-insert-side: insert the peg into the hole from the side
def peg_insert_side(robot):
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
        robot.align("peg to hole")
    if check("peg is horizontally aligned with hole"):
        robot.insert("peg into hole") 

# The code defines a function `peg_insert_side` that takes a robot as its argument.
#
# The first `if` statement checks if the gripper is not vertically aligned with the peg.
# If that is the case, it moves the gripper above the peg using the `put` method of the robot.
#
# The second `if` statement checks if the peg is not left of the gripper and is not forward aligned with the gripper.
# If that is the case, it grabs the peg using the `grab` method of the robot.
#
# The third `if` statement checks if the gripper is forward aligned with the peg and the peg is not horizontally aligned with the hole.
# If that is the case, it aligns the peg with the hole using the `align` method of the robot.
#
# The final `if` statement checks if the peg is horizontally aligned with the hole.
# If that is the case, it inserts the peg into the hole using the `insert` method of the robot.