# -*- coding: UTF-8 -*-
#global section
rule30 = {"███": '░',
          "██░": '░',
          "█░█": '░',
          "░░░": '░',
          "█░░": '█',
          "░██": '█',
          "░█░": '█',
          "░░█": '█',
         }
n_blocks = 31
###############################
#function section
def generate_state():
    n_whites = n_blocks-1 #excluding the black block
    generated_list = ["█"]
    for i in range(n_whites):
        if i <= n_whites/2:
            generated_list.insert(0,"░")
        else:
            generated_list.append("░")
    generated_state = "".join(generated_list)
    return generated_state

def evolve(state):
    evolved_list = list(state)
    for i in range(n_blocks):
        for j in rule30:
            if state[i-1:i+2] == j:
                evolved_list[i] = rule30[j]

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
    assert set(state) == {'░', '█'}

def test_generation_single_alive():
    state = generate_state()
    num_of_blacks = sum(1 for i in state if i=='█')
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
        if old_state[i:i+1] == "█":
            break
        else:
            n_whites_left = n_whites_left + 1
    for i in range(len(old_state)):
        if old_state[len(old_state)-i-1:len(old_state)-i] == "█":
            break
        else:
            n_whites_right = n_whites_right + 1
    assert n_whites_left == n_whites_right
##################################
#main program section
evolution = simulation(10)
for i in evolution:
    print(i)
