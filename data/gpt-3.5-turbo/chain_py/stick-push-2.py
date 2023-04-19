# Steps:
#  1. Put one end of the stick near the thermos
#  2. Push the other end of the stick to slide the thermos
# We'll assume that the robot can manipulate the stick directly rather than
# needing to control the ends separately.
# First, put one end of the stick near the thermos.
if check("one end of the stick is not near the thermos"):
    robot.move("one end of the stick near the thermos")
# Once one end of the stick is near the thermos, we can push the other end to
# slide the thermos.
if check("one end of the stick is near the thermos"):
    robot.push("the other end of the stick to slide the thermos")