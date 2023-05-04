
"""
        return _instr_tmpl

    def gen_trial_id(self):
        """ generates a unique id for the trial """
        #trial_id = 'Trial_{}-Task_{}'.format(self.trial_num, self.task)
        trial_id = str(self.trial_num)
        return trial_id

    def init_task_data_folder(self, trial_id=None):
        """
        init a trial folder based on task name,
        so that the data is saved properly.
        """

        if trial_id is None:
            trial_id = self.gen_trial_id()

        if self.task == 'button-press-topdown':
            folder_name = 'tasks/button-press-topdown/' + trial_id
        elif self.task == 'door-lock':
            folder_name = 'tasks/door-lock/' + trial_id
        elif self.task == 'door-unlock':
            folder_name = 'tasks/door-unlock/' + trial_id
        elif self.task == 'drawer-close':
            folder_name = 'tasks/drawer-close/' + trial_id
        elif self.task == 'drawer-open':
            folder_name = 'tasks/drawer-open/' + trial_id
        elif self.task == 'door-open':
            folder_name = 'tasks/door-open/' + trial_id
        elif self.task == 'peg-insert-side':
            folder_name = 'tasks/peg-insert-side/' + trial_id
        elif self.task == 'plate-slide-side':
            folder_name = 'tasks/plate-slide-side/' + trial_id
        elif self.task == 'plate-slide-back':
            folder_name = 'tasks/plate-slide-back/' + trial_id
        elif self.task == 'window-open':
            folder_name = 'tasks/window-open/' + trial_id
        elif self.task == 'window-close':
            folder_name = 'tasks/window-close/' + trial_id
        elif self.task == 'pick-place':
            folder_name = 'tasks/pick-place/' + trial_id
        elif self.task == 'reach':
            folder_name = 'tasks/reach/' + trial_id
