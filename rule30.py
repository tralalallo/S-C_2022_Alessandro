from numpy import binary_repr

generic_rule_base = {"111": '',
          "110": '',
          "101": '',
          "100": '',
          "011": '',
          "010": '',
          "001": '',
          "000": '',
         }
def rule_in_use():
    number_of_rule = 3 #change this number to change rule
    position = 0
    this_rule = generic_rule_base
    binary_rule = binary_repr(number_of_rule,width=8)
    for j in this_rule:
        this_rule[j] = binary_rule[position:position+1]
        position = position + 1
    return this_rule

###############################
#function section
def number_of_blocks():
    n_blocks = 31 #modify this value to change lenght of lines
    if n_blocks % 2 == 0:
        n_blocks = n_blocks + 1   #condition for simmetry
    return n_blocks

def generate_state():
    n_whites = number_of_blocks()-1 #excluding the black block
    generated_list = ["1"]
    for i in range(n_whites):
        if i < n_whites/2:
            generated_list.insert(0,"0")
        else:
            generated_list.append("0")
    generated_state = "".join(generated_list)
    return generated_state

def evolve(state):
    rule = rule_in_use()
    evolved_list = list(state)
    for i in range(len(state)):
        for j in rule:
            if state[i-1:i+2] == j:
                evolved_list[i] = rule[j]

    evolved_state = "".join(evolved_list)
    return evolved_state

def simulation(nsteps):
    initial_state = generate_state()
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = states_seq[-1]
        new_state = evolve(old_state)
        states_seq.append(new_state)
    return states_seq

##################################
#test section
def test_generation_valid_state():
    state = generate_state()
    assert set(state) == {'1', '0'}

def test_generation_single_alive():
    state = generate_state()
    num_of_blacks = sum(1 for i in state if i=='1')
    assert num_of_blacks == 1
def test_same_state_lenght():
    old_state = generate_state()
    new_state = evolve(old_state)
    assert len(old_state) == len(new_state)
def test_same_whites():
    old_state = generate_state()
    n_whites_left = 0
    n_whites_right = 0
    for i in range(len(old_state)):
        if old_state[i:i+1] == "1":
            break
        else:
            n_whites_left = n_whites_left + 1
    for i in range(len(old_state)):
        if old_state[len(old_state)-i-1:len(old_state)-i] == "1":
            break
        else:
            n_whites_right = n_whites_right + 1
    assert n_whites_left == n_whites_right
##################################
#main program section
rule_in_use()
evolution = simulation(10)
for line in evolution:
    printed_line = ""
    for cell in line:
        if cell == '1':
            printed_line = printed_line + "\u2592"
        else:
            printed_line = printed_line + "\u2591"
    print(printed_line)

