# neuron-network-basic
Neuron network basic

# setup
In the file "CreateSave.py" there you craete layers with the fuction from the file "layerCreate.py" ( layer1 = layerCreate((number of neurons you want)) ). To connect the neurons you need to use the function from the file "nerronsConnection.py" ( nerronsConnection(layer3 (to), layer1 (from)) ). To get the layers you need to output (print) all layers or write them to a difrent file (like i did).<br><br>
IMPORTANT:
you need to set a value to the neurons in the first layer to work!

after you did the steps you need to caulculate the layers you do this by using the function "neuronCaulculation" from the file "neuronCaulculation.py" ( neuronCaulculation(layer2 (from/now)), layer1 (to/past) ).

Finel you output (print) the last line.

# example
#inpurting functions<br>
import layerCreate, nerronsConnection, neuronsCaulculation<br>

#layers setup <br>
layer1 = layerCreate.layerCreate(2)<br>
layer2 = layerCreate.layerCreate(3)<br>
layer3 = layerCreate.layerCreate(3)<br>
layer4 = layerCreate.layerCreate(2)<br>
<br>
<br>
#setting the first input<br>
layerVal1 = layer1.get(list(layer1.keys())[0])<br>
layerVal1["value"] = 10<br>
layer1[list(layer1.keys())[0]] = layerVal1<br>
<br>
layerVal2 = layer1.get(list(layer1.keys())[1])<br>
layerVal2["value"] = 20<br>
layer1[list(layer1.keys())[1]] = layerVal2<br>
<br>
#connecting<br>
nerronsConnection.neuronsConnection(layer2,layer1)<br>
nerronsConnection.neuronsConnection(layer3,layer2)<br>
nerronsConnection.neuronsConnection(layer4,layer3)<br>

#caulculting<br>
neuronsCaulculation.neuronCaulculation(layer2,layer1)<br>
neuronsCaulculation.neuronCaulculation(layer3,layer2)<br>
neuronsCaulculation.neuronCaulculation(layer4,layer3)<br>
<br>
#output<br>
print(layer1, layer2, layer3, layer4)<br>


# credit:
Yuval t++++++n l+++++++++f

