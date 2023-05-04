

I will give you hints below to help you complete the function.
Each time I give you a hint, try to use it to write more of your program.
If you get stuck, you can ask me for the next hint.
Don't forget to indent your program.

To run your program, type `run()`.

"""


class Controller:
    def __init__(self, env):
        self.env = env

    def put(self, target):
        print(f"Putting {target}...")
        return {"env_info": self.env.step(np.array([0., 0., 0., 0., 0., 0.]))}

    def grab(self, target):
        print(f"Grabbing {target}...")
        return {"env_info": self.env.step(np.array([0., 0., 0., 0., 0., 0.]))}

    def drop(self, target):
        print(f"Dropping {target}...")
        return {"env_info": self.env.step(np.array([0., 0., 0., 0., 0., 0.]))}

    def push(self, target):
        print(f"Pushing {target}...")
        return {"env_info": self.env.step(np.array([0., 0., 0., 0., 0., 0.]))}

    def close(self, target):
        print(f"Closing on {target}...")
        return {"env_info": self.env.step(np.array([0., 0., 0., 0., 0., 0.]))}

    def pull(self, target):
        print(f"Pulling {target}...")
        return {"env_info": self.env.step(np.array([0., 0., 0., 0., 0., 0.]))}

    def slide(self, target):
        print(f"Sliding {target}...")
        return {"env_info": self.env.step(np.array([0., 0., 0., 0., 0., 0.]))}

    def align(self, target):
        print(f"Aligning to {target}...")
        return {"env_info": self.env.step(np.