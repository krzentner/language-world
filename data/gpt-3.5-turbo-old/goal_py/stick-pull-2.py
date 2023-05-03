# Steps:
#  1. Lift the stick to be above the thermos
#  2. Move the stick to grab the handle of the thermos
#  3. Pull the stick towards the target location to slide the thermos
# First, lift the stick above the thermos
if check("the stick is not lifted above the thermos"):
    robot.move_stick("lifted above the thermos")
# Move the stick to grab the handle of the thermos
if check("the stick is not holding the handle of the thermos"):
    robot.move_stick("holding the handle of the thermos")
# Once the stick is holding the handle of the thermos, pull it towards the target
if check("the stick is holding the handle of the thermos and the stick is not near the target location"):
    robot.move_stick("near the target location")