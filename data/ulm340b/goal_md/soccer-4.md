 Write the strategy here:
    Steps:
    - When
    - When
    - When
    """

    def __init__(self, task_names: Optional[List[str]] = None):
        self.world = World(create_agents=True,
                           timestep=1/25.,
                           set_task_callable=lambda s, r: s.set_task(task_name=r),
                           )

        self.current_task = 'button-press-topdown'
        self.tasks_to_train = {
            'button-press-topdown': {
                'task_name': 'button-press-topdown',
                'steps': ['line-up-the-gripper-as-viewed-from-above', 'push-down-on-the-button-from-the-top']
            },
            'drawer-open': {
                'task_name': 'drawer-open',
                'steps': ['put-gripper-above-drawer-handle', 'drop-gripper-around-drawer-handle', 'pull-open-the-drawer']
            },
            'door-open': {
                'task_name': 'door-open',
                'steps': ['put-gripper-above-door-handle', 'drop-gripper-around-door-handle', 'pull-open-the-door']
            },
            'window-close': {
                'task_name': 'window-close',
                'steps': ['put-gripper-left-of-the-window-handle', 'start-pushing-against-the-window-handle-to-close-the-window', 'push-the-window-closed-harder']
            },
            'peg-insert-side': {
                'task_name': 'peg-insert-side',
                'steps': ['put-gripper-above-the-peg', 'grab-the-peg-with-the-gripper', 'line-the-peg-up-with-the-hole', 'slide-the-peg-sideways-into-the-hole']
            },
            'drawer-close': {
                'task_name': 'drawer-close',
                'steps': ['put-gripper-roughly-around-the-drawer-handle', 'push-the-drawer-closed']
