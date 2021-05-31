from multiagent.core import World, Agent, Landmark, MBTI_Agent, userConfig
from multiagent.scenario import BaseScenario
import numpy as np
import scipy.spatial as spatial

def getAgentListFromUserConfig(conf):
    agents = []

    if (conf.num_agents != len(conf.mbti_agent_list)):
        return agents

    for agent in conf.mbti_agent_list:
        agents.append(MBTI_Agent(agent['E'], agent['N'], agent['F'], agent['P'], agent['eFlags']))
    
    return agents

def calculateDensityKDTree(agent, world, radius=1):
    positions = []
    index = 0
    i = 0
    for rem_agent in world.agents:
        if rem_agent is agent:
            index = i
        i += 1
        positions.append(rem_agent.state.p_pos)

    tree = spatial.KDTree(np.array(positions))
    radius = 3.0

    neighbors = tree.query_ball_tree(tree, radius)
    frequency = np.array(list(map(len, neighbors)))
    density = frequency/radius**2

    return density[index]

def calculateDensity(agent, world, radius=1):
    positions = []
    for rem_agent in world.agents:
        if rem_agent is agent:
            continue
        positions.append(rem_agent.state.p_pos)

    density = 0
    if (len(positions)) == 0:
        return 0

    count = 0
    for p in positions:
        if (p[0] - agent.state.p_pos[0])**2 + (p[1] - agent.state.p_pos[1])**2 <= radius**2:
            count += 1

    density = count/len(positions)

    agent.personality.density.append(density)
    #print("Density for agent ", agent.name, "  is: ", density)
    return density

def getMBTIReward(agent, world):
    if not agent.personality.enableEI:
        return 1
    density  = calculateDensity(agent, world)
    agent.personality.density.append(density)
    diff = abs(density - agent.personality.E)
    mbti_rew = 1 if diff == 0 else diff*-1
    return mbti_rew