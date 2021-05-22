from multiagent.core import World, Agent, Landmark, MBTI_Agent
from multiagent.scenario import BaseScenario
import os

def calculateDensity(agent, world):
    positions = []
    for rem_agent in world.agents:
        if rem_agent is agent:
            continue
        positions.append(rem_agent.state.p_pos)

    if (len(positions)) == 0:
        return 0

    count = 0
    for p in positions:
        if p[0]**2 + p[1]**2 <= 1:
            count += 1
            
    return count/len(positions)

def getMBTIReward(agent, world):
    mbti_rew = 0
    density  = calculateDensity(agent, world)

    if agent.E == 1:
        mbti_rew +=  density if density >= 0.5 else density*-1
    else:
        mbti_rew +=  density*-1 if density >= 0.5 else density

    return mbti_rew