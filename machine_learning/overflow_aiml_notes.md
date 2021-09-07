-   Recurrent neural networks: NN's that take time data into account, often used to preidict future events. 
    -   Used in NLP (each word is at a new time), kinematics problems
    -   Suffers from Vanishing Gradient problem - can be coutnered with LSTM or GRU 

-   Vanishing Gradient problem: Gradients shrink at earlier hidden layers, so they are adjusted less. 

-   Max Pooling: a way to shrink tensors, using a filter size and stride. For a filter of 2x2 and stride of 2, every 2x2 region becomes a single cell with the value of the max value in the 2x2 zone. 
    -   There's other types of pooling, such as average pooling

- Gradient Boosted Trees / Gradient Boosting
    - like random forests, but more sequential? 