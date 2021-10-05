On the Utility of Emergent Behaviors from Curious Exploration

Abstract
- reward functions that give bonuses for curiosity often overwrite it once the curiosity leads to discovering new task - agents don't become lifelong learners. Instead, try not to overwrite the curiosity once we arrive at the objective. 
- Curiosity is helpful for sparse tasks - agents have to be encuoraged when they find no immediate results
    - Sometimes, curiosity is enough to complete an entire task (eploration-related tasks)
- Once an agent reaches a higher-rewaraded task, it may succumb to __Catastrophic Forgetting__, IE overwriting teh curiosity to  insted converge on the new task at hand. The intermediate processes are discaraded, even though they will be helpful again in future tasks. 
- Curiosity learning: rewards exploration of regions of the state-action space which are hard to predict
- Add in punishment / negative reward for not continuing to learn
    - this could be an expoential backoff-like measure for agents that don't change the way they satisfy their reward function often enough
        - __writing in restlessness into a reward function__ 