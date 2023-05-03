# stick-push: use the stick to push the thermos to the target location
# def stick_push(robot):
# Steps:
#  1. Put the sticky end of the stick under the thermos
#  2. Lift the thermos with the stick
#  3. Slide the thermos to target location
#  4. Lower the thermos onto the target location
# First, orient the sticky end of the stick under the thermos.
if check("the sticky end of stick is not under the thermos"):
    robot.move_stick("under the thermos")
# Raise the thermos with the stick.
if check("robot is not holding thermos with stick"):
    robot.lift_thermos()
# Slide the thermos to target location.
if check("the thermos is not at target location"):
    robot.slide_thermos("to the target location")
# Lower the thermos onto the target location.
if check("the thermos is not securely placed at target location"):
    robot.lower_thermos()