
    # Steps:
    #  1. Put gripper above cube
    #  2. Push the gripper down into the cube
    #  3. Slide the cube towards the target
    #  4. Drop the cube at the target
    # First, put the gripper above the cube, so we don't bump the cube while
    # trying to grab it.
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    # If the gripper isn't near the cube, push the gripper down into the cube.
    # Maybe we'll push it into the right place.
    if check("the robot's gripper is not near cube"):
        robot.push("gripper into cube")
    # If the gripper is near the cube, we can probably slide the cube around.
    # Close the gripper so the cube doesn't slide out.
    if check("the robot's gripper is near cube"):
        robot.slide("cube to goal")
    # Once the cube is close to the target, open the gripper to drop the cube at
    # the target location.
    if check("the robot's gripper is near reach target"):
        robot.drop("cube at target")

# sweep-onto: grab the cube and put it on the table
def sweep_onto(robot):
    # Steps:
    #  1. Put gripper above cube
    #  2. Push the gripper down into the cube
    #  3. Slide the cube towards the target
    #  4. Drop the cube at the target
    # First, put the gripper above the cube, so we don't bump the cube while
    # trying to grab it.
    if check("the robot's gripper is not above cube"):
        robot.put("gripper above cube")
    # If the gripper isn't near the cube, push the gripper down into the cube.
    # Maybe we'll push it into the right place.
    if check("the robot's gripper is not near cube"):
        robot.push("gripper into cube")
    # If the gripper is near the cube, we can probably slide the cube around.
    # Close the gripper so the cube doesn't slide out.
