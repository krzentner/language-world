
"""

    def __init__(self, args, logger, split_manager, mode, epoch, task_manager, random_seed):
        self.logger = logger
        self.task_manager = task_manager
        self.mode = mode
        self.random_seed = random_seed

        parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument('--dataset', type=str, default=args.dataset)
        parser.add_argument('--dataset-root', type=str, default=args.dataset_root)
        parser.add_argument('--random-seed', type=int, default=args.random_seed)
        parser.add_argument('--debug', type=str, default=args.debug)
        parser.add_argument('--split', type=str, default=args.split)
        parser.add_argument('--batchsize', type=int, default=args.batchsize)
        parser.add_argument('--epoch', type=int, default=args.epoch)
        parser.add_argument('--split-by', type=str, default=args.split_by)
        parser.add_argument('--split-num', type=int, default=args.split_num)
        parser.add_argument('--split-root', type=str, default=args.split_root)
        parser.add_argument('--prebuilt-split-file', type=str, default=args.prebuilt_split_file)

        # Model args
        parser.add_argument('--imgsize', type=int, default=args.imgsize)
        parser.add_argument('--model-arch', type=str, default=args.model_arch)
        parser.add_argument('--model-type', type=str, default=args.model_type)
        parser.add_argument('--model-config', type=str, default=args.model_config)

        # Optimization args
        parser.add_argument('--num-pretrain-epochs', type=int, default=args.num_pretrain_epochs)
        parser.add_argument('--num-finetune-epochs', type=int, default=args.num_finetune_epochs)
        parser.add_argument('--max-num-epochs', type=int, default=args.max_num_epochs)
        parser.add_argument('--learning