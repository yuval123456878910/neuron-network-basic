import layerCreate, nerronsConnection,neuronsCaulculation

layer1 = layerCreate.layerCreate(1)
neuron = layer1.get(list(layer1.keys())[0])
neuron["value"] = 20
layer1[list(layer1.keys())[0]] = neuron

layer2 = layerCreate.layerCreate(3)
layer3 = layerCreate.layerCreate(3)
layer4 = layerCreate.layerCreate(2)
nerronsConnection.neuronsConnection(layer2,layer1)
nerronsConnection.neuronsConnection(layer3,layer2)
nerronsConnection.neuronsConnection(layer4,layer3)

with open("saveAi.py","w") as saveFile:
    saveFile.write(f"layer1 = {layer1}\nlayer2 = {layer2}\nlayer3 = {layer3}\nlayer4 = {layer4}")
    saveFile.close()
"""
nerronsConnection.neuronsConnection(layer2,layer1)
nerronsConnection.neuronsConnection(layer3,layer2)
neuronsCaulculation.neuronCaulculation(layer2,layer1)
neuronsCaulculation.neuronCaulculation(layer3,layer2)
print(layer3)"""