import random 
import sys
from tiger import TigerPOMDP
from simulator import POMDPSimulator

#####################################################################
# This is a sample simulation loop for the DRL framework using POMDPs
#####################################################################

# initialize pomdp
pomdp = TigerPOMDP()

# initialize and pass the pomdp into simulator
sim = POMDPSimulator(pomdp) # state and initial belief automatically initialized

na = sim.n_actions() # number of actions-output layer size
ns = sim.n_states() # number of states-input layer size

opt = pomdp.optimal_policy()

steps = 100

rtot = 0.0

for i in range(steps):
    # get the initial state
    s = sim.get_screenshot()
    # pick random action
    #ai = random.randint(0,na)
    # pick optimal aciton
    ai = opt(s) 

    # progress simulation
    sim.act(ai)

    # get reward and next states
    r = sim.reward() # real valued reward
    sp = sim.get_screenshot() # pomdp state, this is a belief

    print s, ai, r, sp
    print sim.current_state, sim.current_belief.bnew

    rtot += r

    # check if reached terminal state
    if sim.episode_over():
        sim.reset_episode()

print "Total reward: ", rtot