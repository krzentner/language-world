# Steps:
#  1. Move hand to the puck
#  2. Grab the puck with the hand
#  3. Move the hand to the target location
#  4. Release the puck
# First, move the hand towards the location of the puck
if check("the hand is not near the puck"):
    robot.move("hand to puck")
# If the hand is near the puck, grab it with the hand
if check("the hand is near the puck and the hand is open"):
    robot.grab("puck with hand")
# Now that the hand has hold of the puck, move it to the target location
if check("the hand is holding the puck and is not at the target location"):
    robot.move("hand to target location with the puck")
# Finally, release the puck once the hand is at the target location
if check("the hand is holding the puck and is at the target location"):
    robot.release("puck from hand")