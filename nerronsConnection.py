

def neuronsConnection(now,past):
    for neuron in list(now.keys()):
        value_neuron = now.get(neuron)

        value_neuron["connect"] = list(past.keys())
        now[neuron] = value_neuron


