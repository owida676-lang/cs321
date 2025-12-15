# Simple DFA Minimization Tool
# Uses partition refinement (easy to understand, no external libraries)

from collections import defaultdict

class DFA:
    def __init__(self, states, alphabet, transition, start_state, final_states):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transition = transition  # dict: (state, symbol) -> state
        self.start_state = start_state
        self.final_states = set(final_states)

    def minimize(self):
        # 1. Initial partition: final vs non-final states
        P = [self.final_states, self.states - self.final_states]
        P = [p for p in P if p]  # remove empty sets

        changed = True
        while changed:
            changed = False
            new_P = []

            for group in P:
                # split group based on transition behavior
                blocks = defaultdict(set)
                for state in group:
                    key = []
                    for symbol in self.alphabet:
                        next_state = self.transition.get((state, symbol))
                        # find which partition next_state belongs to
                        for i, p in enumerate(P):
                            if next_state in p:
                                key.append(i)
                                break
                        else:
                            key.append(None)
                    blocks[tuple(key)].add(state)

                if len(blocks) > 1:
                    changed = True
                    new_P.extend(blocks.values())
                else:
                    new_P.append(group)

            P = new_P

        # 2. Build new minimized DFA
        state_map = {}
        for i, group in enumerate(P):
            for state in group:
                state_map[state] = i

        new_states = set(range(len(P)))
        new_start = state_map[self.start_state]
        new_finals = {state_map[s] for s in self.final_states}
        new_transition = {}

        for (state, symbol), next_state in self.transition.items():
            new_transition[(state_map[state], symbol)] = state_map[next_state]

        return DFA(new_states, self.alphabet, new_transition, new_start, new_finals)

    def display(self):
        print("States:", self.states)
        print("Alphabet:", self.alphabet)
        print("Start State:", self.start_state)
        print("Final States:", self.final_states)
        print("Transitions:")
        for (s, a), ns in self.transition.items():
            print(f"  δ({s}, '{a}') -> {ns}")


# ---------------- EXAMPLE USAGE ----------------

# Define a DFA
states = {0, 1, 2, 3}
alphabet = {'a', 'b'}
transition = {
    (0, 'a'): 1, (0, 'b'): 2,
    (1, 'a'): 0, (1, 'b'): 3,
    (2, 'a'): 3, (2, 'b'): 0,
    (3, 'a'): 2, (3, 'b'): 1,
}
start_state = 0
final_states = {0, 3}

dfa = DFA(states, alphabet, transition, start_state, final_states)
print("Original DFA")
dfa.display()

min_dfa = dfa.minimize()
print("\nMinimized DFA")
min_dfa.display()
