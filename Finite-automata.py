text = "ababcabcabababd"
pattern = "ababd"


alphabet = set(text)

m = len(pattern)
transition = [{} for _ in range(m + 1)]

for state in range(m + 1):
    for char in alphabet:
        #  հաջորդ վիճակի հաշվում
        next_state = state
        while next_state > 0 and (next_state == m or pattern[next_state] != char):
            next_state -= 1
        if next_state < m and pattern[next_state] == char:
            next_state += 1
        transition[state][char] = next_state

state = 0
matches = []

for i, char in enumerate(text):
    #  նոր վիճակի որոնում
    state = transition[state].get(char, 0)
    if state == len(pattern):
        
        matches.append(i - len(pattern) + 1)


print("Matches found at positions:", matches)
