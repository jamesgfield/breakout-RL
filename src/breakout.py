import gym
env = gym.make("ALE/Breakout-v5", render_mode="human")
observation, info = env.reset(seed=42, return_info=True)

for _ in range(10000):
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)

    if done:
        observation, info = env.reset(return_info=True)
    print("hello there")

env.close()