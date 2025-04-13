from saveAi import *
import nerronsConnection,neuronsCaulculation

value = layer1.get(list(layer1.keys())[0])
value["value"] = 260

layer1[list(layer1.keys())[0]] = value


neuronsCaulculation.neuronCaulculation(layer2,layer1)
neuronsCaulculation.neuronCaulculation(layer3,layer2)
neuronsCaulculation.neuronCaulculation(layer4,layer3)
n1_val = (layer4.get(list(layer4.keys())[0])).get("value")
n2_val = (layer4.get(list(layer4.keys())[1])).get("value")
print(n1_val,n2_val)
if n1_val > n2_val:
    print("Jump")
else:
    print("Nothing")