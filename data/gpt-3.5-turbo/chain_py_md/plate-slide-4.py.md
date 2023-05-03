# plate-slide: slide the plate into the target location
def plate_slide(robot):
    # Steps:
    # 1. Align gripper with plate
    # 2. Push the plate into the target location
    # We need to align the gripper with the plate before we can push it
    # If the plate is not aligned with the gripper, we need to move the gripper above it
    # Because the plate is a flat object, check if it is aligned with the gripper from above
    if check("the plate is not aligned with the gripper"):
        robot.put("gripper above plate")
    # If the gripper is above the plate, push the plate
    if check("the gripper is above the plate"):
        robot.push("plate into target location")