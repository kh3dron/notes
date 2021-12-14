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


VOGUE: Try-On StyleGAN Interpolation Optimization

- Given an pair of images, person and garments A and B, put garment B on person A. 
  - I guess 512x512 image is considered high resolition for ML
- StyleGAN2 to create a middle layer which classifies anatomy from pictures - identify shirts, pants, hands, hair, neck, face

BERT: Pre-Training of Deep Bidirectional Transformers for Language Understanding

- Typically, NLP models think left to right, where each word can see the context to the left of it. 
  - "The man went to a store"
    - "store" knows that "a" refers to the store, but the "man" token is unaware of the "store" modifier. 
- Some solve this solution by also flipping all the data, then concatonating the two models after the fast. But what if we do this in one pass?
  - There's a problem of words "seeing themslves" if we do this wrong
- Another issue with LMs is relationships between sentences, so we wrote a binary classifier for if sentenc B came after sentence A in the source text. 
  
Attention Is All You Need
(Transformers for NLP)

- Old models for NLP
  - Bag of words: like a hash table of all characters, does not store order 
  - RNN: store each word as a vector, add it as a hidden state to the next word vector
    - Vanishing or exploding gradient problem: dependencies fade as they get further away
    - difficult to learn long range dependencies for this reason
  - LSTM: Type of RNN
    - 2 hidden states: store the hidden states without compounding them as hard
- Attention: the decoder can jump backwards to past values, rather than just look through linearly compressed hidden states
- Queries, Keys, Values
  - Values: interesting things about the sentence (facts)
  - Keys: how to address the values (where to find the facts)
  - Queries: requests for Values (requests for facts)
- Benefits
  - Parallelizable: because we're not stepping backwards, running attention on a sentence is just one large matmult with itself

An Image is Wirth 16x16 Words: Transformers for Image Recognition At Scale

- Transformers work on sequences, or sets, which makes images seem unlikely (too many pixels)
- We can run attention on images by feeding chunks of images as a seqence, rather than pixels, and it turns out that works quite well