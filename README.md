# Neighbor-based Multi-Agent Reinforcement Learning

The main file containing the distributed training approaches is ``DTDE/collect_the_items_v3.ipynb``

The notebook is organized in six main sections:

## Preparing the Notebook

Allows to correctly initialize the environment. Before running the experiments it is mandatory to run the cells contained in ``import and utils`` and ``defining the environment``. 
Running the cell ``environment demonstration`` is not mandatory, but suggested since it allows to check if the environment has been properly set by running a random episode.

## Training

This is the main section of the notebook and contains all the experiments explained in the thesis. Executing the cell ``preparing the environment`` is compulsory in order to be able to run the training cells.
Each one of the different approaches is located in a different subsection and consists of two parts: the training and the visualization of the metrics compared against the independent learners approach. 
By default the utilized seed is 3010, but it can be changed by replacing it in the debugging parameter of the DQNConfig object.

## Save and Load

This section allows to save the trained model and to load a previously runned model as specified by the value of ``algo_name``. Through this section is also possible to save and load the model metrics as a json.

## Results Comparison

In this section are compared the performance of the different training strategies

## Simulation

In this section it is possible to simulate an episode by using a policy or a set of policies. In the case a single policy is shared among all the agents, the ``simulate_episode`` method must be called.
In case of distinct policies for distinct agents, ``simulate_episode_multipolicy`` must instead be called.

## Comparison

This section contains additional comparisons between the trained models as boxplots
