

The code should include the following:

* "If the gripper is not above the peg"
* "If the gripper is left of the peg"
* "If the gripper is forward aligned with the peg"
* "If the robot's gripper is vertically aligned with the peg"
* "If the gripper is not near the target location"
"""

print(
    "# pick-out-of-hole: pick up the peg out of the hole and hold it at the target location")
print("def pick_out_of_hole(robot):")
print("    # Steps:")
print(
    "    #  1. Put gripper above peg")
print("    #  2. Grab the peg with the gripper")
print("    #  3. Line the peg up with the goal")
print("    #  4. Move peg to the goal")
print("    # If the gripper is not above the peg")
print("    if check(\"the robot's gripper is not above the peg\"):")
print("        robot.move_gripper(\"above the peg\", close_gripper=True)")
print("    # If the gripper is left of the peg")
print("    if check(\"the gripper is left of the peg\"):")
print("        robot.move_gripper(\"vertically aligned with the peg\", close_gripper=True)")
print(
    "    # If the gripper is forward aligned with the peg")
print("    if check(\"the robot's gripper is forward aligned with the peg\"):")
print(
    "        robot.move_gripper(\"almost vertically aligned with the peg\", close_gripper=True)")
print(
    "    # If the robot's gripper is vertically aligned with the peg")
print("    if check(\"the robot's gripper is vertically aligned with the peg\"):")
print("        robot.move_gripper(\"vertically aligned with the target location\", close_gripper=True)")
print("    # If the gripper is not near the target location")
print(
    "    if check(\"the gripper is not near the target location\"):")
print("        robot.move_gripper(\"near the target location\")")


"""

"""


print("""
# This code uses two kinds of primitives:
#  - `move_gripper`: takes `goal` and optionally `close_gripper