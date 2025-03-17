---
title: "Entropy Estimation in Gaussian Mixture Models"
date: 2025-03-16T20:00:00
draft: true
summary: "In the context of using GMMs in Reinforcement Learning"
#showtoc: true
excludeFromBlog: false

cover:
    image: "images/gmm.png"
    alt: "<alt text>"
    caption: "" 
    relative: false 
    hiddenInList: false
    hiddenInSingle: false
    hidden: false
---

In algorithms such as PPO, we use a distribution at the output of the policy network from which we sample actions. In this post, we will discuss how to estimate the entropy of a Gaussian Mixture Model. 

Gaussian Mixture Models are universal function approximators i.e., given enough components, they can approximate any complex .. 



Entropy of a distribution: 
- Is a measure of the randomness or uncertainty in the policy's action distribution. A higher entropy value indicates a more uniform distribution over actions i.e., encourages the agent to try different actions rather then explot an action that yields high reward. 



