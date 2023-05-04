
'''

    if len(task.get_unsatisfied_preconditions()) == 0:
        return 'The robot should push the puck to the target location.'
    else:
        if task.unsatisfied_preconditions[0].function == 'slide_puck_right':
            if len(task.get_unsatisfied_preconditions()) == 1:
                return 'The robot should put its gripper at the left side of the puck and slide it right.'
            elif len(task.get_unsatisfied_preconditions()) == 2:
                return 'The robot should put its gripper near the left side of the puck and slide it right.'
            else:
                return "I don't know what the robot should do."
        elif task.unsatisfied_preconditions[0].function == 'slide_puck_left':
            if len(task.get_unsatisfied_preconditions()) == 1:
                return 'The robot should put its gripper at the right side of the puck and slide it left.'
            elif len(task.get_unsatisfied_preconditions()) == 2:
                return 'The robot should put its gripper near the right side of the puck and slide it left.'
            else:
                return "I don't know what the robot should do."

        # print task.get_unsatisfied_preconditions()
        # return "I don't know what the robot should do."

        # for pre in task.get_unsatisfied_preconditions():
        #     if pre.function == 'drop_gripper_around_door_handle':
        #         return "Drop the gripper around the door handle."
        #     elif pre.function == 'move_gripper_below_door_handle':
        #         return "Move gripper below door handle."
        #     elif pre.function == 'grab_peg':
        #         return "Grab the peg."
        #     elif pre.function == 'move_gripper_above_peg':
        #         return "Move gripper above the peg."
        #     elif pre.function == 'move_gripper_above_door_handle':
        #         return "Move gripper above door handle."
        #     elif pre.function == 'move_gripper_above_drawer_handle':
        #         return "Move gripper above drawer handle."
        #     elif pre.function == 'move_gripper_above_puck':
        #         return "Move gripper above puck."
