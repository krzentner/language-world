

The robot needs to slide a plate into a target location.

Steps:
  1. Put gripper above the plate
  2. Drop gripper around the plate
  3. Slide the plate to target location
  
 # plate-slide: slide the plate into the target location
 # def plate_slide(robot):
    # steps:
    # 1. put gripper above plate
    if check("the robot's gripper is not above the plate"):
        robot.put("gripper above plate")
    # 2. Drop gripper around plate
    if check("the robot's gripper is not around the plate and the robot's gripper is open"):
        robot.drop("gripper around plate")
    # 3. Slide the plate to the target location
    if check("the robot's gripper is around the plate"):
        robot.slide("plate to target location")