from multiagent.core import World, Agent, Landmark, MBTI_Agent
from multiagent.scenario import BaseScenario
import os

def calculateDensity(agent, world, radius=1):
    positions = []
    for rem_agent in world.agents:
        if rem_agent is agent:
            continue
        positions.append(rem_agent.state.p_pos)

    density = 0
    if (len(positions)) == 0:
        density =  0
    else:
        count = 0
        for p in positions:
            if (p[0] - agent.state.p_pos[0])**2 + (p[1] - agent.state.p_pos[1])**2 <= radius**2:
                count += 1
        
        density = count/len(positions)
    
    agent.density.append(density)
    #print("Density for agent ", agent.name, "  is: ", density)
    return density

def getMBTIReward(agent, world):
    density  = calculateDensity(agent, world)
    mbti_rew = 0
    if density == 0:
        mbti_rew = 1  if agent.I == 1 else 0
    else:
        mbti_rew +=  density if agent.E == 1 else density*-1
    #print("MBTI reward for agent ", agent, "  is: ", mbti_rew)
    return mbti_rew