

The task `reach-gap` requires the robot to reach to the target location with a gap in the ground.
To reach to the target location with a gap in the ground reliably, what steps the robot should perform?

The task `reach-narrow-gap` requires the robot to reach to the target location with a gap in the ground and narrow walls on either side.
To reach to the target location with a gap in the ground and narrow walls on either side reliably, what steps the robot should perform?

The task `reach-ramp` requires the robot to reach to the target location by moving up a ramp.
To reach to the target location by moving up a ramp reliably, what steps the robot should perform?

The task `reach-through-wall` requires the robot to reach to the target location by moving through a wall.
To reach to the target location by moving through a wall reliably, what steps the robot should perform?

The task `reach-under-wall` requires the robot to reach to the target location by reaching under a wall.
To reach to the target location by reaching under a wall reliably, what steps the robot should perform?

The task `reach-over-wall` requires the robot to reach to the target location by reaching over a wall.
To reach to the target location by reaching over a wall reliably, what steps the robot should perform?


'''


def generate_explanation(task):
    task_id, explanation, explanation_str = task_explanations[task]

    # replace step numbers with steps to be clear
    explanation_str = explanation_str.replace('Step 1: ', 'Step: ')
    explanation_str = explanation_str.replace('Step 2: ', 'Step: ')
    explanation_str = explanation_str.replace('Step 3: ', 'Step: ')
    explanation_str = explanation_str.replace('Step 4: ', 'Step: ')
    explanation_str = explanation_str.replace('Step 5: ', 'Step: ')

    # replace steps with actual actions
    explanation_str = explanation_str.replace('Step: Line up the robot\'s gripper above the drawer handle', 'Step: Move gripper to above drawer handle.')
    explanation_str = explanation_str.replace('Step: Drop gripper around drawer handle', 'Step: Move gripper down around drawer handle.')
    explanation_str = explanation_str.replace('Step: Pull open the drawer', 'Step