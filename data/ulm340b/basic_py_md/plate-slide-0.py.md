

Then finish it so that you get the `plate-slide-0` checkmark.

''')

# Slide the plate horizontally.

# plate-slide-0: slide the plate horizontally, pushing and pulling

# if check("the robot's gripper is not vertically aligned with the plate"):
#     robot.move("gripper to plate")
# if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near the plate"):
#     robot.put("gripper to plate")
# if check("the robot's gripper is near the plate and the plate is above the robot's gripper"):
#     robot.pull("plate")
# if check("the plate is not right of the robot's gripper and the plate is not horizontally aligned with goal"):
#     robot.slide("plate to goal")

# if check("the robot's gripper is not vertically aligned with the plate"):
#     robot.move("gripper to plate")
# if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near the plate"):
#     robot.put("gripper to plate")
# if check("the robot's gripper is near the plate and the plate is below the robot's gripper"):
#     robot.push("plate")
# if check("the plate is not left of the robot's gripper and the plate is not horizontally aligned with goal"):
#     robot.slide("plate to goal")

if check("the robot's gripper is not vertically aligned with the plate"):
    robot.move("gripper to plate")
if check("the robot's gripper is vertically aligned with the plate and the robot's gripper is not near the plate"):
    robot.put("gripper to plate")
if check("the robot's gripper is near the plate and the plate is left of the robot's gripper"):
    robot.push("plate")
if check("the plate is not right of the robot's gripper and the plate is not horizontally aligned with goal"):
    robot.slide("plate to goal")


print('''
# plate-slide-0: slide the plate horizontally, pushing and pulling
def plate_slide(robot):
''')
print(p)

print('''
That is great. Now I will show you another way to control the robot.
''')

print('''
# door-open: pull the door open, using new `move`, `wait`, and `check` commands
