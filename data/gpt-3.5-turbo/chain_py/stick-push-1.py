# Steps:
    #  1. Put gripper above stick
    #  2. Pick up stick
    #  3. Put gripper above thermos
    #  4. Drop stick onto thermos
    #  5. Align stick with thermos
    #  6. Push thermos to target location with stick
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above stick")
    # Once the gripper is above the stick, pick it up.
    if check("the robot's gripper is vertically aligned with the stick and the robot's gripper is not around stick"):
        robot.grab("stick")
    # Once the gripper is around the stick, put the gripper above the thermos.
    if check("the robot's gripper is around stick and the robot's gripper is not vertically aligned with thermos"):
        robot.put("gripper above thermos")
    # Once the gripper is above the thermos, drop the stick onto the thermos.
    if check("the robot's gripper is vertically aligned with thermos and the stick is not touching the thermos"):
        robot.drop("stick onto thermos")
    # Once the stick is laying on the thermos, align it with the target location.
    if check("the stick is touching the thermos, but not aligned with the target location"):
        robot.align("stick with thermos and target location")
    # Once the stick is aligned with the target location, push the thermos towards it.
    if check("the stick is aligned with the target location and touching the thermos"):
        robot.push("thermos to target location with stick")