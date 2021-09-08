# <i class="far fa-edit fa-fw"></i> Practice: Neural Networks and Images

## Question 0

Suppose I wanted to use a neural network to take images as inputs and predict whether the image was a picture of a cat, dog, or [axolotl](https://media.giphy.com/media/4YWu31EsM1ToJnAzqc/giphy.gif). Suppose the input images are in RGB color and were 50x50 pixels. How many input neurons would there be in our network?

**<i class="far fa-edit fa-fw"></i> Your Task**

Write your answer down in your own space.

## Question 1

For the same network in the last problem, how many output neurons will there be?

**<i class="far fa-edit fa-fw"></i> Your Task**

Write your answer down in your own space.

## Question 2

Below we have mixed up a list of the **parameters** and **hyperparameters** of a neural network model. In this problem, please select all the values that are the model **parameters**.

**<i class="far fa-edit fa-fw"></i> Your Task**

Select one or more options. Write your answer down in your own space.

_<i class="far fa-square fa-fw"></i> Option 0_

Number of hidden layers

_<i class="far fa-square fa-fw"></i> Option 1_

Number of hidden nodes in each hidden layer

_<i class="far fa-square fa-fw"></i> Option 2_

Weights between neurons

_<i class="far fa-square fa-fw"></i> Option 3_

Bias for each neuron

## Question 3

Consider the following network with the structure and weights used below (colors only for emphasis). The weights for each connection are shown above the connection and the bias is shown inside the neuron. By convention, a bias of 10 means 10 is subtracted from the weighted sum of inputs before being passed to the "squishification" function (e.g., will fire positively if the weighted sum exceeds 10).

```{image} https://static.us.edusercontent.com/files/Kd786GuC8sNauSwZzfnpO6JO
:alt: A network with two input nodes, two middle nodes with the bias 1 and 2 respectively, and an output node with a bias of 0. The first input node has two outgoing edges connecting to each of the middle nodes. The edge connecting to the node with bias 1 has weight 2, and the edge connecting to the node with bias 2 has weight 1. The second input node also has two outgoing edges to each of the middle nodes with weight 2 connecting to the node with bias 1 and weight 3 connecting to the node with bias 2. Both of the middle nodes have one outgoing edge connecting to the output node with weight 0, and both of them have weight 1.
:width: 687
:align: center
```

For simplicity, we will use a different "squishification function". Instead of the Sigmoid, we will use the "Step" function $\sigma(x)$ defined below. All it does is clamp the output to 0 if the weighted sum (including bias) is less than or equal to 0 and the output is 1 if it is positive. The output neuron uses this same function.

$$\sigma(x) = \begin{cases} 0 & x \leq 0 \\ 1 & x > 0\\\end{cases}$$

What is the output if we use the input `(1, 0)` where `1` is the input value to the top neuron and `0` is the input value to the bottom neuron?

_Hint: Your output should be an integer._

**<i class="far fa-edit fa-fw"></i> Your Task**

Write your answer down in your own space.

## Question 4

Consider the `sklearn` code to make a neural network

```text
model = MLPClassifier(hidden_layer_sizes=(3, 4, 3, 1))

```

**True or false** , this code specifies a network with the architecture shown in the image below.

```{image} https://static.us.edusercontent.com/files/p4aQn7nnk0h3DqYetAKV4blO
:alt: A fully connected neural network with 4 layers. The first input layer has 3 nodes, the second layer has 4 nodes, the third has 3 nodes, the fourth output layer has 1 node.
:width: 691
:align: center
```

**<i class="far fa-edit fa-fw"></i> Your Task**

Write your answer down in your own space.
