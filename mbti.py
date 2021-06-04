from multiagent.core import World, Agent, Landmark, MBTI_Agent, userConfig
from multiagent.scenario import BaseScenario
import numpy as np

def getAgentListFromUserConfig(conf):
    agents = []

    if (conf.num_agents != len(conf.mbti_agent_list)):
        return agents

    for agent in conf.mbti_agent_list:
        agents.append(MBTI_Agent(agent['E'], agent['N'], agent['F'], agent['P'], agent['eFlags']))
    
    return agents

def normalizeReward(reward, maxR, minR):
    #print("old reward is: ", reward, "\n\n")
    num = reward - minR
    den = maxR - minR
    num = 2*num
    reward = num/den
    reward = reward - 1
    #print("new reward is: ", reward, "\n\n")
    return reward

def getRewardForEI(agent, world):
    #print("In ", __name__)
    return 0

def updateRewardForTF(agent, world, reward_n):
    #print("In ", __name__)
    return 0

def getRewardForJP(agent, world):
    #print("In ", __name__)
    return 0    

