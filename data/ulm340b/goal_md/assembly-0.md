Please enter them in the box below.
'''

def get_tutorial_action_descriptions(task_descs, all_task_keys=None, all_action_descs=None):
    """
    Returns a list of action descriptions with keys.
    """
    if all_task_keys is None:
        all_task_keys = {'push', 'reach', 'pick-place', 'door-open', 'drawer-open', 'window-close', 'window-open', 'drawer-close', 'button-press-topdown', 'assembly', 'peg-insert-side'}
    if all_action_descs is None:
        all_action_descs = {
            'push': 'move the gripper while keeping the puck below the gripper',
            'reach': 'move the robot\'s gripper to the target location',
            'pick-place': 'move the puck to the goal',
            'door-open': 'pull open the door',
            'drawer-open': 'pull open the drawer',
            'window-close': 'slide the window closed to the right',
            'window-open': 'slide the window open to the left',
            'drawer-close': 'push the drawer closed',
            'button-press-topdown': 'push down on the button from the top',
            'assembly': 'grab the wrench and wrap it around the peg',
            'peg-insert-side': 'slide the peg sideways into the hole',
        }
    task_descs = {key: task_descs.get(key, all_action_descs.get(key)) for key in task_descs}
    return task_descs

def write_task_key_file(task_descs, key_file):
    with open(key_file, 'w') as f:
        for k,v in task_descs.items():
            f.write(f'{k}\t{v}\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Generate instructions text for tutorials",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('key_file')
    parser.add_argument('--task-keys', type=lambda x: x.split(','), default=