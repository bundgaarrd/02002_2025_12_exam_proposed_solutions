# Opgave 2 (Gate Distance)
import math

def gate_distance(gate1: str, gate2:str):
    gate1 = gate1.upper()
    gate2 = gate2.upper()

    gates = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4
    }

    t1 = 4 # min, between terminal
    t2 = 0.8 # min, between gates
    gate1_char = gate1[0]
    gate1_num = int(gate1[1])
    gate2_char = gate2[0]
    gate2_num = int(gate2[1])

    terminal_difference = abs(gates[gate2_char] - gates[gate1_char])

    if gate1_char == gate2_char: # in case chosen gates are in the same terminal
        total_time = abs(gate2_num - gate1_num) * t2
    else:
        total_time = terminal_difference * t1 + (gate1_num+gate2_num) * t2
    
    total_time = math.ceil(total_time)

    return f'Walking time {total_time} min'
