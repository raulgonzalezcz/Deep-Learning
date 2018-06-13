# Using Deep Q-Network to Learn How To Play Flappy Bird

<img src="./images/flappy_bird_demp.gif" width="250">

Video about 7 mins showing the result: [DQN for flappy bird](https://www.youtube.com/watch?v=THhUXIhjkCM)

## Overview
This project follows the description of the Deep Q Learning algorithm described in Playing Atari with Deep Reinforcement Learning [2] and shows that this learning algorithm can be further generalized to the notorious Flappy Bird. My work was to establish an environment to reproduce this project without problems (using Anaconda and other tools).

## Installation Dependencies:
* Python 2.7 or 3
* TensorFlow 1.5
* pygame
* OpenCV-Python

## How to Run? (How I do it?)
```
1. Install miniconda or anaconda if you have not already. Check https://www.continuum.io/downloads
2. Create an environment for flappybird
    * Mac/Linux: conda create --name=flappybird python=2.7
    * Windows: conda create --name=flappybird python=3.5
3. Enter your conda environment
    * Mac/Linux: source activate flappybird
    * Windows: activate flappybird
4. conda install -c menpo opencv3
5. pip install pygame
6. pip install tensorflow==1.5
7. git clone https://github.com/yenchenlin/DeepLearningFlappyBird.git or download it as a ZIP archive from the original repo.
8. cd DeepLearningFlappyBird (If you downloaded the ZIP archive, it might be called DeepLearningFlappyBird-master)
9. python deep_q_network.py
```
If all went correctly, you should be seeing a deep learning based agent play Flappy Bird! The repository contains instructions for training your own agent if you're interested!

## How to stop?
Just press Crtl + C and that's all. In order to exit from your conda environment:
```
* Mac/Linux: source deactivate flappybird
* Windows: deactivate flappybird
```

## What is Deep Q-Network?
It is a convolutional neural network, trained with a variant of Q-learning, whose input is raw pixels and whose output is a value function estimating future rewards.

For those who are interested in deep reinforcement learning, I highly recommend to read the following post:

[Demystifying Deep Reinforcement Learning](http://www.nervanasys.com/demystifying-deep-reinforcement-learning/)

## Deep Q-Network Algorithm

The pseudo-code for the Deep Q Learning algorithm, as given in [1], can be found below:

```
Initialize replay memory D to size N
Initialize action-value function Q with random weights
for episode = 1, M do
    Initialize state s_1
    for t = 1, T do
        With probability ϵ select random action a_t
        otherwise select a_t=max_a  Q(s_t,a; θ_i)
        Execute action a_t in emulator and observe r_t and s_(t+1)
        Store transition (s_t,a_t,r_t,s_(t+1)) in D
        Sample a minibatch of transitions (s_j,a_j,r_j,s_(j+1)) from D
        Set y_j:=
            r_j for terminal s_(j+1)
            r_j+γ*max_(a^' )  Q(s_(j+1),a'; θ_i) for non-terminal s_(j+1)
        Perform a gradient step on (y_j-Q(s_j,a_j; θ_i))^2 with respect to θ
    end for
end for
```

## Original repository
Check out https://github.com/yenchenlin/DeepLearningFlappyBird

## References

[1] Mnih Volodymyr, Koray Kavukcuoglu, David Silver, Andrei A. Rusu, Joel Veness, Marc G. Bellemare, Alex Graves, Martin Riedmiller, Andreas K. Fidjeland, Georg Ostrovski, Stig Petersen, Charles Beattie, Amir Sadik, Ioannis Antonoglou, Helen King, Dharshan Kumaran, Daan Wierstra, Shane Legg, and Demis Hassabis. **Human-level Control through Deep Reinforcement Learning**. Nature, 529-33, 2015.

[2] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, and Martin Riedmiller. **Playing Atari with Deep Reinforcement Learning**. NIPS, Deep Learning workshop

[3] Kevin Chen. **Deep Reinforcement Learning for Flappy Bird** [Report](http://cs229.stanford.edu/proj2015/362_report.pdf) | [Youtube result](https://youtu.be/9WKBzTUsPKc)

## Disclaimer
This work is highly based on the following repos:

1. [sourabhv/FlapPyBird] (https://github.com/sourabhv/FlapPyBird)
2. [asrivat1/DeepLearningVideoGames](https://github.com/asrivat1/DeepLearningVideoGames)
