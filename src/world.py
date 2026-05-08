class GridWorld:
    agent_states = {'UP' : (1, 0), 'DOWN' : (-1, 0), 'LEFT' : (0, -1), 'RIGHT' : (0, 1)}
    start_pos = (0, 0)
    goal_pos = (3, 3)
    rewards = {'step': -1, 'goal': 10, 'obstacle': -10}

    def __init__(self, rows=4, cols=4, obstacles : list[tuple] = []):
        self.environ = None
        self._init_environ(rows, cols, obstacles)

    def _init_environ(self, rows, cols, obstacles: list[tuple]):
        """
        Setup the Environment
        """
        assert rows and cols
        grid = [ [None for i in range(cols)] for i in range(rows) ]

        for x, y in obstacles:
            grid[x][y] = 'obstacle'

        self.environ = {
            'grid' : grid,
            'pos'  : type(self).start_pos
        }

    def _evaluate_action(self, action: str):
        next_pos = self.environ['pos'] + type(self).agent_states[action.upper()]

        try:
            self.environ['grid'].copy()[next_pos[0]][next_pos[1]] = None
            self.environ['pos'] = next_pos

            if next_pos == type(self).goal_pos:
                return type(self).rewards['goal'], True

            if self.environ['grid'][next_pos[0]][next_pos[1]] == 'obstacle':
                return type(self).rewards['obstacle'], False
        except Exception as e:
            print(e)
        finally:
            return type(self).rewards['step'], False

    def get_reward(self, action: str):
        """
        The reward function for our environment.
        Returns next_state, reward, done
        """
        next_state = type(self).agent_states
        reward, done = self._evaluate_action(action)

        return next_state, reward, done

if __name__ == "__main__":
    env = GridWorld(obstacles=[(1,1), (2,2)])
    print(env.environ)
