# CorpusSeverPlatform
This is the introduction of the Corpus Sever Platform. 

# Objective 

Provide 📚 Corpus Service for LLM post training.

High-quality corpora for large-model training, at the same time, prevent data leakage and misuse, plus dedicated support for reinforcement-learning datasets.

## Features

- **High-Quality Data**  
  Curated text corpora optimized for training state-of-the-art language models.
  
- **Data Protection**  
  Robust mechanisms to ensure your data never leaks or gets misused. 

# Why do this work

- **RLVR**
According to Allen AI : 

>Reinforcement Learning with Verifiable Rewards (RLVR) is a novel method for training language models on tasks with verifiable outcomes such as mathematical problem-solving and instruction following.

>RLVR leverages the existing RLHF objective but replaces the reward model with a verification function. When applied to domains with verifiable answers, such as mathematics and verifiable instruction following tasks, RLVR demonstrates targeted improvements on benchmarks like GSM8K while maintaining performance across other tasks.

>RLVR can be seen as a simplified form of existing approaches for bootstrapping LM reasoning (Eric Zelikman et al., Du Phan et al.) or a simpler form of RL with execution feedback, in which we simply use answer matching or constraint verification as a binary signal to train the model. In other words, the policy only receives a reward when its generated responses are verifiably correct.

>We found that integrating RLVR as a component of the generalist training pipeline can gain up to 1.7, 3.3, and 1.3 points improvement over the DPO checkpoint on MATH, GSM8K and IFEval. Starting RVLR from SFT results in bigger gains, but we found the highest final models were from training with DPO before RVLR. Surprisingly, RLVR also led to improvements on other tasks that it was not optimized for including BigBenchHard, Drop, and AlpacaEval 2.

>![image](https://github.com/user-attachments/assets/30c6420d-185d-4ece-9302-0f32251fdb7e)


In this work we provide questions and judgement service for the training llm.

Questions are like:


>Verifiable data sample:
> Question:
> A laboratory has newly developed a lithium-ion battery pack for electric vehicles with a rated capacity of 5 Ah. 
> In a discharge test, the battery was subjected to a constant-current discharge at a 0.5 C rate. 
> Please answer the following question: calculate the discharge current of the battery at a 0.5 C rate, in amperes?
>
> Answers are like: Answer: 2.5 A

Instead of directly providing answers we give services that could evaluate the answers in groups.

# How we do this work

![image](https://github.com/user-attachments/assets/152ab9ea-3373-494f-aa38-7276e98a7031)


1. We provide questions only in groups, the questions are randomly chosen.
2. The answers are also evaluated in group.
3. We limit the number of answers provided by the user to prevent a force break.

# How to use the platform for training a llm

![image](https://github.com/user-attachments/assets/7c2b67a5-32ed-4f5e-bf22-0d61e06bfc4e)

1. Email for a licence
2. Read the API doc.
3. Send for questions for Initialize API.
4. Answer questions and send the answers to the evaluation API.
5. Wait for the scores.
6. Use the high score answer for reinforcement learning.


