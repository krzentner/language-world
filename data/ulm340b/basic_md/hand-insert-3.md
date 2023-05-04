''


def build_state_graph(env_name):
    ## create state nodes
    num_states = 60 # hard coded number of states, this should be done dynamically
    state_to_id = {}
    id_to_state = {}
    for i in range(num_states):
        state = 'state%d'%i
        state_to_id[state] = i
        id_to_state[i] = state


    # create task nodes
    task_names = ['button-press-topdown', 'drawer-open', 'drawer-close', 'door-open',
                  'window-close', 'window-open', 'peg-insert-side', 'reach', 'push',
                  'pick-place', 'hand-insert']
    tasks_to_id = {}
    id_to_task = {}
    for i in range(len(task_names)):
        task_name = task_names[i]
        tasks_to_id[task_name] = i
        id_to_task[i] = task_name

    # build edges between states and tasks
    edge_list = ['state15', 'button-press-topdown', 'state0', 'button-press-topdown']
    for edge_list_entry in edge_list:
        tokens = edge_list_entry.split()
        source = state_to_id[tokens[0]]
        target = tasks_to_id[tokens[1]]
        edge_data = EdgeData(source, target, is_pre=True, is_post=True)
        edge_list_entry += ", is_pre=True, is_post=True"
        edge_list_entry += ", edge_type=%s"%tokens[1]
        edge_data.type = tokens[1]
        edge_list_entry += ", task=%s"%tokens[1]
        edge_data.task = tokens[1]
        edge_list_entry += ", action_name=%s"%tokens[2]
        edge_data.action_name = tokens[2]
        graph.add_edge(edge_data)
    print(edge_list)

    ## add edges within states
    edges_between_states = {'state0': ['state10'],
                            'state1':