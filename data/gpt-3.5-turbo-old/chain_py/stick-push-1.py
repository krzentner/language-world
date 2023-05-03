# Steps:
# 1. Put one end of the stick next to the thermos
# 2. Push the other end of the stick to slide the thermos to the target location
# We'll start by putting one end of the stick next to the thermos.
if check("one end of the stick is not next to the thermos and the other end is not near the robot's gripper"):
    robot.move("one end of the stick next to the thermos")
# Now that the stick is in place, we can use it to slide the thermos to the
# target location.
if check("one end of the stick is next to the thermos and the other end is near the robot's gripper"):
    robot.slide("thermos to the goal using the stick")