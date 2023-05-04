

As you write the program, write the documentation for the program above the program.
I will ask you to make predictions for the next step in the program while you are writing it,
to evaluate whether you understand your program before you execute it.

""",
            True,
        ),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **{
                **{"image_width": 300},
                **kwargs,
            }
        )

    def parley(self):
        if self.state.parleys_seen < 3:
            self.state.parleys_seen += 1
            return self.instructions()
        elif self.state.parleys_seen == 3:
            return self.start_task(self.state.last_utterance)
        elif self.state.task_type == "door-open":
            return self.play_door_open(self.state.last_utterance)
        elif self.state.task_type == "drawer-open":
            return self.play_drawer_open(self.state.last_utterance)
        elif self.state.task_type == "drawer-close":
            return self.play_drawer_close(self.state.last_utterance)
        elif self.state.task_type == "reach":
            return self.play_reach(self.state.last_utterance)
        elif self.state.task_type == "pick-place":
            return self.play_pick_place(self.state.last_utterance)
        elif self.state.task_type == "peg-insert-side":
            return self.play_peg_insert_side(self.state.last_utterance)
        elif self.state.task_type == "push":
            return self.play_push(self.state.last_utterance)
        elif self.state.task_type == "button-press-topdown":
            return self.play_button_press_topdown(self.state.last_utterance)
        elif self.state.task_type == "button-press-wall":
            return self.play_button_press_wall(self.state.last_utterance)
        else:
            return self.parley()

    def update_parleys_seen(self, action):
        if action != "start":
            self.state.parleys_seen += 1

    def instructions(self):
        return Input({"text": self.INSTRUCTION