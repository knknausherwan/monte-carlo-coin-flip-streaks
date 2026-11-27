# Monte Carlo Simulation: Coin Flip Streak Probability

A Python implementation of the **Monte Carlo method** to estimate the probability of observing at least six consecutive identical outcomes in a sequence of 100 fair coin flips.

The project uses repeated randomized experiments to approximate a probability that can also be investigated analytically, demonstrating how computational simulation can be used for probabilistic analysis.

## Objective

Estimate the probability that a sequence of 100 independent fair coin flips contains at least one streak of six or more consecutive Heads or Tails.

Rather than evaluating every possible sequence mathematically, this project uses Monte Carlo simulation to approximate the probability through repeated random sampling.

## Monte Carlo Methodology

The simulation follows a stochastic sampling approach:

1. **Experiment initialization:** Define the number of independent simulation trials, the sequence length, and the required streak length.
2. **Random sampling:** Generate 100 independent coin-flip outcomes using a uniform random distribution.
3. **Streak detection:** Apply a sliding-window approach using list slicing to examine every possible sequence of six consecutive outcomes.
4. **Event classification:** Determine whether the generated sequence contains at least one streak of six consecutive Heads or Tails.
5. **Trial aggregation:** Increment the success counter when the event occurs.
6. **Probability estimation:** Divide the number of successful experiments by the total number of simulation trials.

The estimated probability is calculated as:

\[
\hat{P}(A) = \frac{\text{Number of successful trials}}{\text{Total simulation trials}}
\]

where \(A\) represents the event of observing at least one streak of six identical outcomes.

## Simulation Parameters

| Parameter | Value | Description |
|---|---:|---|
| Number of trials | 10,000 | Independent Monte Carlo experiments |
| Flips per trial | 100 | Random coin-flip outcomes |
| Streak length | 6 | Consecutive identical outcomes |
| Outcome probability | 0.5 | Probability of Heads or Tails |

## Technologies and Concepts

- **Python 3** – Simulation implementation.
- **Monte Carlo Method** – Numerical probability estimation through repeated random sampling.
- **Stochastic Processes** – Modeling independent random coin-flip outcomes.
- **Random Sampling** – Generating uniformly distributed binary outcomes.
- **Sliding Window** – Detecting consecutive patterns in generated sequences.
- **Statistical Estimation** – Approximating event probabilities from observed frequencies.

## Execution

### Prerequisites

- Python 3.x
- No external dependencies required.

### Run the simulation

Clone the repository:

```bash
git clone https://github.com/USERNAME/monte-carlo-coin-flip-streaks.git
```

Navigate to the project directory:

```bash
cd monte-carlo-coin-flip-streaks
```

Execute the simulation:

```bash
python coin_flip_streaks.py
```

## Results and Interpretation

The simulation estimates the probability of observing at least one qualifying streak across 10,000 independent experiments.

A typical estimated probability is approximately **80%**.

Since Monte Carlo simulation relies on random sampling, the estimated probability will vary between executions. Increasing the number of trials generally reduces sampling variability and improves the stability of the estimate.

## Learning Outcomes

This project explores the practical application of computational probability and reinforces:

- Monte Carlo simulation techniques.
- Stochastic modeling and random sampling.
- Empirical probability estimation.
- Random variable generation.
- Pattern detection using list slicing.
- Iterative simulation and statistical aggregation.
- The relationship between theoretical probability and numerical approximation.

## Project Context

This project is inspired by the *Coin Flip Streaks* practice project in **Automate the Boring Stuff with Python** by Al Sweigart.

It extends the exercise's programming concepts into a practical introduction to Monte Carlo simulation and computational statistics.

## License

Released for educational and personal learning purposes.
