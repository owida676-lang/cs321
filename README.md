# DFA Minimization Tool (Python)

## 📌 Description
This project implements a **Deterministic Finite Automaton (DFA) Minimization Tool** using Python.  
The tool minimizes a given DFA using the **partition refinement method**, which is commonly taught in **Theory of Computation** courses.

The program takes a DFA definition (states, alphabet, transitions, start state, and final states) and produces an equivalent **minimal DFA**.

---

## 🧠 Theory Used
- Deterministic Finite Automata (DFA)
- Equivalence of states
- Partition refinement technique
- DFA minimization

---

## ⚙️ Features
- Simple and readable Python implementation
- No external libraries required
- Clearly separates:
  - Final and non-final states
  - Iterative partition refinement
- Displays both:
  - Original DFA
  - Minimized DFA

---

## 🧾 Input Format
The DFA is defined directly in the code using:
- `states`: set of states
- `alphabet`: set of input symbols
- `transition`: dictionary mapping `(state, symbol)` → `next_state`
- `start_state`: initial state
- `final_states`: set of accepting states

---

## ▶️ How to Run
1. Make sure Python 3 is installed
2. Run the file:
   ```bash
   python dfa_minimization.py
The minimized DFA will be printed in the terminal

🧪 Example
The provided example DFA has:

4 states

Alphabet {a, b}

2 final states

After minimization, equivalent states are merged and a smaller DFA is produced.

📁 Project Structure
Copy code
dfa-minimization/
│
├── dfa_minimization.py
└── README.md
👤 Authors
. Owida
. Seif
Owida

Seif
