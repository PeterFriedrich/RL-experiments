import gym
env = gym.make('CartPole-v0')

def basic_policy(obs):
    angle = obs[2]
    return 0 if angle < 0 else 1

totals = []
for episode in range(500):
    episode_rewards = 0
    obs = env.reset()
    for setp in range(1000): # 1000 steps max, we don't want to run forever
        action = basic_policy(obs)
        obs, reward, done, info = env.setup(action)
        episode_rewards += reward
        if done:
            break
    totals.append(episode_rewards)
