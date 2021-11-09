video parsing style GAN 

- 1 - Monet Kaggle Competition
  - Build a generator
    - downsamples input images with pooling, etc. 
    - upsamples them through the NN
  - Build a  descriminator
    - classifies each pixel as 1 for authentic and 0 for stylized
  - Build the CycleGAN model
    - subclass with a keras.Model 
    - Training:
      - tun through generator, then transform back to normal 
      - difference between original and trice translated is "cycle consistency loss", to be minimized
  - Define Loss Functions
    - The perfect generator will have the distriminator only output 1s
    - 


- 2 - Try with non-monet dataset