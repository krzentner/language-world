
- When the robot's gripper is above the cube and the cube is not in the target location, the robot should push the cube to the target location.
"""

def generate_instruction(task):
    filename = os.path.join(ROOT_DIR, "data", "task_instructions", "{}.md".format(task))
    with open(filename) as f:
        s = f.read()
    return s


##
# Functions for working with the dataset
##

def normalize(data):
    # Normalize each item in the observation/action space to be in [0, 1]
    # Note that this is a no-op for boolean features, e.g. "isgripperopen".
    normalized_data = {}
    for k in data:
        if isinstance(data[k], bool):
            normalized_data[k] = data[k]
            continue
        min_value = np.min(data[k])
        max_value = np.max(data[k])
        normalized_data[k] = (data[k] - min_value) / (max_value - min_value)
    return normalized_data

def denormalize(data):
    # Inverse operation of normalize()
    denormalized_data = {}
    for k in data:
        if isinstance(data[k], bool):
            denormalized_data[k] = data[k]
            continue
        min_value = np.min(data[k])
        max_value = np.max(data[k])
        denormalized_data[k] = (data[k] * (max_value - min_value)) + min_value
    return denormalized_data

def process_data(raw_data):
    # Flatten the hierarchical dictionary structure into simple arrays,
    # and convert to numpy arrays

    states = {}
    actions = {}

    # Parse the state information
    states['image'] = np.array([data['image'] for data in raw_data])
    states['image_goal'] = np.array([data['image_goal'] for data in raw_data])
    states['image_state_achieved'] = np.array([data['image_state_achieved'] for data in raw_data])
    states['relabeled_image'] = np.array([data['relabeled_image'] for data in raw_data])

    # Parse the