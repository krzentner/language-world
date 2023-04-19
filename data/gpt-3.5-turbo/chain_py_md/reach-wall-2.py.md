# reach-wall: reach to the target location with a short wall in the way
# def reach_wall(robot):
# Steps:
#   1. Move the gripper to the edge of the wall
#   2. Reach as close as possible to the target location
#   3. Move around the wall to the target location
# First, move the gripper so that it is at the edge of the wall.
# To move the gripper, we need to know the initial position of the gripper,
# the position of the wall, and the position of the target location.
# We also need to know the length of the wall (which is assumed to be along
# x-axis) and the gripper's range of motion (which is assumed to be along y-axis).
def reach_wall(robot, wall_position, target_position, gripper_position, wall_length=0.2, gripper_range=0.2):
    wall_center = wall_position[1]
    target_center = target_position[1]
    gripper_center = gripper_position[1]
    # Check if the gripper is already on the correct side of the wall.
    if gripper_center <= wall_center:
        # Check if we can reach the target location directly.
        if abs(target_center - gripper_center) <= gripper_range:
            robot.reach(target_position)
        else:
            # Move the gripper as close to the target location as possible.
            if target_center > gripper_center:
                robot.reach((target_position[0], gripper_center + gripper_range))
            else:
                robot.reach((target_position[0], gripper_center - gripper_range))
            # Move around the wall to the target location.
            if target_center > wall_center:
                robot.move((wall_position[0], target_center - wall_length/2 - gripper_range))
                robot.move((target_position[0], target_position[1]))
            else:
                robot.move((wall_position[0], target_center + wall_length/2 + gripper_range))
                robot.move((target_position[0], target_position[1]))