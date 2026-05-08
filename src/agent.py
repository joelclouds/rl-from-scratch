class Agent:
    id = 0

    def __init__(self):
        type(self).id += 1
        self.id = type(self).id
        self.reward = 0

        self.action_history = ()

    def act(self, actions):
        
