

The goal of this task is to slide a plate backwards so that it is aligned with a target location.

Steps: 

1. Put gripper right of the plate handle
2. Push against the handle to begin sliding the plate
3. Push the further to slide the plate back into the target location

# plate-slide-back: slide the plate back into the target location
def plate_slide_back(robot):
    # Steps:
    #  1. Put gripper right of the plate handle
    #  2. Push against the handle to begin sliding the plate
    #  3. Push the further to slide the plate back into the target location
    # First, we need to put the gripper right of the plate handle.
    if check("the robot's gripper is in front of the plate handle"):
        robot.move_gripper("right of the plate handle")
    # Once the gripper is near the handle we can apply pressure with the gripper 
    # to begin sliding the plate. 
    if check("the plate handle is right of the robot's gripper and the robot's gripper is not near the plate handle"):
        robot.move_gripper("almost vertically aligned with the plate handle")
    # Then, if the gripper is near the plate handle, apply more pressure
    # to slide the plate back into its target location.
    if check("the robot's gripper is near the plate handle"):
        robot.move_gripper("forward aligned with the plate handle")