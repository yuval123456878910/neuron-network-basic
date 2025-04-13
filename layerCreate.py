# work!

def layerCreate(num):
    import random
    dict_n = {}
    for on_number in range(num):
        dict_n["n" + str(on_number)] = {"value": int(),"input": int(), "connect": list(), "weight": random.uniform(-1,1), "bias": random.uniform(-5,5)}
    return dict_n
