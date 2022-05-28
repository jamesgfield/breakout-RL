import numpy as np
import gym
# import matplotlib.pyplot as plt

# gym initialization
env = gym.make('Pong-v4')
observation = env.reset()
prev_input = None
# plt.imshow(observation)
# plt.show()

# Declaring the two actions that can happen in Pong for an agent, move up or move down
# Decalring 0 means staying still. Note that this is pre-defined specific to package.
UP_ACTION = 2
DOWN_ACTION = 3
# Hyperparameters. Gamma here allows you to measure the effect of future events
gamma = 0.99
# initialization of variables used in the main loop
x_train, y_train, rewards = [],[],[]
reward_sum = 0
episode_nb = 0

#Let’s take a look at the game in action.
import matplotlib.pyplot as plt
env = gym.make('Pong-v4') # environment info
observation = env.reset()
# The ball is released after 20 frames
for i in range(22):
 
    if i > 20:
        plt.imshow(observation)
        plt.show()

observation, _, _, _ = env.step(1)