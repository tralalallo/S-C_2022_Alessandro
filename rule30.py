#dictionaries section
rule30 = {"000": '.',
          "00.": '.',
          "0.0": '.',
          "...": '.',
          "0..": '0',
          ".00": '0',
          ".0.": '0',
          "..0": '0',
         }
###############################
#function section
def generate_state():
    return "...........0..........."

def evolve(state):
    evolved_list = list(state)
    rules_list = list(rule30.keys())
    for i in range(20):
        for j in range(8):
            if state[i:i+3] == rules_list[j]:
                evolved_list[i] = rule30.get(rules_list[j])

    evolved_state = "".join(evolved_list)
    return evolved_state

def simulation(nsteps):
    initial_state = generate_state()
    states_seq = [initial_state]
    for i in range(nsteps):
        old_state = states_seq[-1]
        #print("oldstate: ",old_state)
        new_state = evolve(old_state)
        states_seq.append(new_state)
    return states_seq

##################################
#test section
def test_generation_valid_state():
    state = generate_state()
    assert set(state) == {'.', '0'}

def test_generation_single_alive():
    state = generate_state()
    num_of_0 = sum(1 for i in state if i=='0')
    assert num_of_0 == 1
def test_same_state_lenght():
    old_state = generate_state()
    new_state = evolve(old_state)
    assert len(old_state) == len(new_state)
##################################
#main program section
evolution = simulation(10)
for i in evolution:
    print(i)
