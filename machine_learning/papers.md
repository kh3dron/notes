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


Zero-Shot Text-to-Image Generation

- Zero-Shot learning: classification that can make relative comparisons on new data. Example: give an AI that can classify horses, explain to it that a zebra is a striped horse, and it may be able to classify zebras. 
  - Requires undertstanding labels in the same semantic space as the training data - understand what "stripes" look like
- Problems for AI image generation:
  - depth (blending foreground and background elements)
  - uncertainty (features that fade instead of cut off, like whispy hair)
- Auoregressive Model: function that depends on its own prior value plus a random term (think volatility, moving average)
- Wow! some absolutely incredible examples of images created from text. "With varying degrees of reliability, our model appears to be able to combine distinct concepts in plausible ways, create anthropomorphized versions of animals, render text, and perform some types of image-to-image translation"
- If we were to define the vector space of an image pixel by pixel, the model would waste too much time on details and miss the larger shapes and structures. Structure is more important to people for identifying objects, so we had to find a way to target that.
- Image processing:
  - downscale the images and the text data, pair them together as single entities

#### GLOSSARY: INTERESTING TERMS AND CONCEPTS

- Catastrophic Forgetting
- Curiosity Learning
- Zero Shot Learning
- Transformers
- Auoregressive Model