---
title: "Monte Carlo Tree Search with RL"
date: 2025-11-25T20:00:00
draft: true
summary: "How Monte Carlo Tree Search works and how it was enhanced with neural networks in AlphaGo"
#showtoc: true
excludeFromBlog: false
math: true

cover:
    image: "images/mcts.png"
    alt: "Monte Carlo Tree Search visualization"
    caption: "" 
    relative: false 
    hiddenInList: false
    hiddenInSingle: false
    hidden: false
---

Monte Carlo Tree Search (MCTS) is a heuristic search algorithm that combines tree search with random sampling. It was a core component in DeepMind's AlphaGo, the first AI to defeat a world champion in Go.

---

## The Core Idea

MCTS builds a search tree incrementally by running many simulations. Each simulation has four phases:

1. **Selection** - Start at root, traverse tree using a selection policy
2. **Expansion** - Add a new child node to the tree
3. **Simulation** - Play out randomly from the new node to a terminal state
4. **Backpropagation** - Update statistics along the path back to root

The key insight is that we don't need to explore the entire game tree. Instead, we focus our search on the most promising branches.

---

## The UCB1 Formula

The selection phase uses the Upper Confidence Bound (UCB1) formula to balance exploration and exploitation:

\\[
UCB1(s, a) = \frac{W(s, a)}{N(s, a)} + c \sqrt{\frac{\ln N(s)}{N(s, a)}}
\\]

Where:
- \\(W(s, a)\\) = total reward from taking action \\(a\\) in state \\(s\\)
- \\(N(s, a)\\) = number of times action \\(a\\) was taken in state \\(s\\)
- \\(N(s)\\) = total visits to state \\(s\\)
- \\(c\\) = exploration constant (typically \\(\sqrt{2}\\))

The first term is the **exploitation term** — it favors actions with high average reward. The second term is the **exploration term** — it favors actions that haven't been tried often.

---

## The Algorithm

<pre class="pseudocode no-line-numbers">
\begin{algorithm}
\caption{Monte Carlo Tree Search}
\begin{algorithmic}
\REQUIRE Initial state $s_0$, number of iterations $n$
\ENSURE Best action $a^*$
\STATE $root \gets \text{CreateNode}(s_0)$
\FOR{$i = 1$ \TO $n$}
    \STATE $node \gets root$
    \STATE $s \gets s_0$
    \STATE
    \COMMENT{Selection}
    \WHILE{$node$ is fully expanded \AND $s$ is not terminal}
        \STATE $node \gets \text{BestChild}(node, c)$
        \STATE $s \gets \text{Apply}(s, node.action)$
    \ENDWHILE
    \STATE
    \COMMENT{Expansion}
    \IF{$s$ is not terminal}
        \STATE $a \gets \text{UntriedAction}(node)$
        \STATE $s \gets \text{Apply}(s, a)$
        \STATE $node \gets \text{AddChild}(node, a, s)$
    \ENDIF
    \STATE
    \COMMENT{Simulation}
    \WHILE{$s$ is not terminal}
        \STATE $a \gets \text{RandomAction}(s)$
        \STATE $s \gets \text{Apply}(s, a)$
    \ENDWHILE
    \STATE
    \COMMENT{Backpropagation}
    \STATE $reward \gets \text{GetReward}(s)$
    \WHILE{$node \neq \text{null}$}
        \STATE $node.N \gets node.N + 1$
        \STATE $node.W \gets node.W + reward$
        \STATE $node \gets node.parent$
    \ENDWHILE
\ENDFOR
\RETURN $\text{BestChild}(root, 0).action$
\end{algorithmic}
\end{algorithm}
</pre>

---

## Why It Works

MCTS converges to the optimal policy given enough iterations. The UCB1 formula ensures that:

1. Actions with high win rates are selected more often (exploitation)
2. Under-explored actions are tried periodically (exploration)

As \\(N(s, a) \to \infty\\), the exploration term vanishes and we're left with pure exploitation of the best action.

The convergence rate depends on the branching factor \\(b\\) and the depth \\(d\\) of the tree:

\\[
\text{Error} \approx O\left(\sqrt{\frac{b \cdot d \cdot \ln n}{n}}\right)
\\]

where \\(n\\) is the number of simulations.

---

## AlphaGo's Enhancement

AlphaGo replaced the random simulation phase with a neural network evaluation. Instead of playing out randomly, it used:

\\[
V(s) = (1 - \lambda) \cdot v_\theta(s) + \lambda \cdot z
\\]

Where:
- \\(v_\theta(s)\\) = value network prediction for state \\(s\\)
- \\(z\\) = outcome of a fast rollout policy
- \\(\lambda\\) = mixing parameter

This made MCTS much more efficient — the neural network could evaluate a position in milliseconds, while random playouts might take hundreds of moves.

---

## The Role of Self-Play

AlphaGo and its successors (AlphaGo Zero, AlphaZero) used self-play to generate training data. The loop works as follows:

1. The current network plays games against itself using MCTS
2. The outcomes of these games are used as training targets
3. The network is updated to better predict game outcomes and promising moves
4. The improved network is used for the next round of self-play

This creates a virtuous cycle — better networks lead to stronger MCTS, which generates higher-quality training data, which produces even better networks. AlphaGo Zero, starting from random play with no human knowledge, surpassed the original AlphaGo in just 72 hours of training.

---

## From PUCT to AlphaZero

AlphaZero replaced UCB1 with PUCT (Predictor + UCB applied to Trees), which incorporates a learned prior from the policy network:

\\[
PUCT(s, a) = \frac{W(s, a)}{N(s, a)} + c \cdot P(s, a) \cdot \frac{\sqrt{N(s)}}{1 + N(s, a)}
\\]

Where \\(P(s, a)\\) is the prior probability from the policy network. This guides the search toward moves the network considers promising, even before they have been explored. Early in the search, the prior dominates. As \\(N(s, a)\\) grows, the empirical value takes over.

---

## Beyond Games

MCTS is not limited to board games. It has been applied to:

- **Robotics** — planning sequences of actions in continuous state spaces
- **Program synthesis** — searching over the space of possible programs
- **Transportation** — designing transit routes by searching over network configurations
- **Mathematical reasoning** — guiding proof search in theorem provers

The core idea — using learned heuristics to guide tree search — turns out to be broadly useful wherever the search space is too large for exhaustive exploration but structured enough for a learned policy to provide useful guidance.