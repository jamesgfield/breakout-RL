import os
import pickle

from dqn_construction import show_video_of_model

# read saved model
current_file_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{current_file_path}/models/target_net-5000>12-06--13-27.pkl', 'rb') as inp:
    target_net = pickle.load(inp)


if(__name__ == '__main__'):
    show_video_of_model('CartPole-v1', target_net)
