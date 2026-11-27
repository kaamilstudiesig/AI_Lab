# Artificial Intelligence Lab (23CS5PCAIN)

Lab programs for **Artificial Intelligence (23CS5PCAIN)**, Semester 5, Department of Computer Science and Engineering, BMS College of Engineering, Bengaluru.

- **USN:** 1BM24CS125
- **Language:** Python (Jupyter notebooks)
- **L-T-P:** 3-0-1 · **Credits:** 4
- **Prescribed textbook:** *Artificial Intelligence: A Modern Approach*, Stuart J. Russell & Peter Norvig, 3rd ed., Pearson

## Lab Programs

| Week | Program | Syllabus Lab # | Unit | Files |
|------|---------|----------------|------|-------|
| [Week 01](Week_01) | Tic-Tac-Toe game; Vacuum cleaner agent | 1, 4 | 1 | `tic_tac_toe.py` (+ output screenshot), `Vacuum_Cleaner.ipynb` |
| [Week 02](Week_02) | 8-Puzzle using DFS; Iterative Deepening Search | 2, 3 | 1 | `DFS_EightPuzzle.ipynb`, `IDDLS_Eight_Puzzle.ipynb` |
| [Week 03](Week_03) | 8-Puzzle using A* search | 5a | 2 | `AStar_8Puzzle.ipynb` |
| [Week 04](Week_04) | 4-Queens using Hill Climbing | 5b | 2 | `Hill_Climbing_4Queen.ipynb` |
| [Week 05](Week_05) | Simulated Annealing | 6 | 2 | `Simulated_Annealing.ipynb` |
| [Week 06](Week_06) | Propositional logic knowledge base: check whether a query is entailed (truth table) | 7 | 3 | `Propositional_Logic.ipynb` |
| [Week 07](Week_07) | Unification in first-order logic | 9 | 4 | `FOL_Unification.ipynb` |
| [Week 08](Week_08) | FOL knowledge base: prove a query using forward chaining | 11 | 4 | `FOL_Forward_Chaining.ipynb` |
| [Week 09](Week_09) | FOL to CNF conversion and proof by resolution | 8, 10 | 4 | `FOL_Resolution.ipynb` |
| [Week 10](Week_10) | Alpha-Beta Pruning | 12 | 4 | `Alpha_Beta_Pruning.ipynb` |

All file names are prefixed with `1BM24CS125_`.

## Other Contents

- [`Lab_Record/`](Lab_Record): lab record
- [`1BM24CS125_CERTIFICATE.pdf`](1BM24CS125_CERTIFICATE.pdf): course certificate

## Course Units

1. **Introduction:** agents and environments, rationality, structure of agents, problem-solving agents.
2. **Search:** BFS, DFS, iterative deepening, hill climbing, simulated annealing; heuristic functions, greedy best-first search, A*.
3. **Logical agents:** knowledge-based agents, Wumpus world, propositional logic, first-order logic.
4. **Inference in FOL:** unification, forward chaining, backward chaining, resolution. **Adversarial search:** minimax, alpha-beta pruning, Monte Carlo tree search, stochastic and partially observable games.
5. **Uncertainty:** probability, full joint distributions, independence, Bayes' rule, Bayesian networks.

## Course Outcomes

- **CO1:** Apply knowledge of agent architecture, searching and reasoning techniques for different applications.
- **CO2:** Analyse searching and inferencing techniques.
- **CO3:** Design a reasoning and gaming system for a given requirement.
- **CO4:** Conduct practical experiments demonstrating agents, searching and inferencing.

## Running

Open any `.ipynb` file in Jupyter Notebook or Google Colab and run all cells. Week 9 needs the `graphviz` package (`pip install graphviz`) to draw the resolution tree. To run Week 1's script:

```bash
python Week_01/1BM24CS125_tic_tac_toe.py
```
