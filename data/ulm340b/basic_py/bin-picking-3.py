
    if check("the robot's gripper is not above the cube"):
        robot.place("gripper above the cube")
    if check("the robot's gripper is above the cube and the robot's gripper is not around the cube and the robot's gripper is open"):
        robot.drop("gripper around the cube")
    if check("the robot's gripper is near the cube and the robot's gripper is open"):
        robot.close("gripper around the cube")
    if check("the robot's gripper is above the cube and the robot's gripper is closed"):
        robot.move("to the goal")
    if check("the robot's gripper is above the goal and the robot's gripper is closed"):
        robot.open("gripper above the goal")


# # Task: Insert the peg into the hole from the side
# # Description: This task is similar to peg-insert-side, except the peg and the hole are on opposite corners of the table
# def peg_insert_side_2(robot):
#     if check("the robot's gripper is not vertically aligned with the peg"):
#         robot.put("gripper above peg")
#     if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
#         robot.grab("peg")
#     if check("the robot's gripper is forward aligned with the peg and the peg is not horizontally aligned with hole"):
#         robot.align("peg to hole")
#     if check("peg is horizontally aligned with hole"):
#         robot.insert("peg into hole")

# # Task: Insert the peg into the hole from the top
# def peg_insert_top(robot):
#     if check("the robot's gripper is not vertically aligned with the peg"):
#         robot.put("gripper above peg")
#     if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
#         robot.grab("peg")
#     if check("the robot's gripper is forward aligned with the peg and the peg is not vertically aligned with hole"):
#         robot.align("peg to hole")
#     if check("peg is vertically aligned with hole"):
#         robot.insert("peg into hole")

# Task: Insert the peg into the hole from the top, but the peg is not visible initially
def peg_insert_top_2(robot):
 