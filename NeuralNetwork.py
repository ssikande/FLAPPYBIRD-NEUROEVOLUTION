import matrixManipulation as mm
import math
import random

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def dsigmoid(y):
    return y * (1 - y)

class NeuralNetwork:
    #just a two layer network 
    #define the amount of nodes in each layer
    def __init__(self, numI, numH, numO):
        if isinstance(numI, NeuralNetwork):
            self.input_nodes = numI.input_nodes
            self.hidden_nodes = numI.hidden_nodes
            self.output_nodes = numI.output_nodes

            self.weights_ih = numI.weights_ih.copy()
            self.weights_ho = numI.weights_ho.copy()
            self.bias_h = numI.bias_h.copy()
            self.bias_o = numI.bias_o.copy()

            #self.learning_rate = 0.1

        else:
            self.input_nodes = numI
            self.hidden_nodes = numH
            self.output_nodes = numO
            #assign random weights and biases 
            self.weights_ih = mm.Matrix(self.hidden_nodes, self.input_nodes)
            self.weights_ho = mm.Matrix(self.output_nodes, self.hidden_nodes)
            self.weights_ih.randomize()
            self.weights_ho.randomize()

            self.bias_h = mm.Matrix(self.hidden_nodes, 1)
            self.bias_o = mm.Matrix(self.output_nodes, 1)
            self.bias_h.randomize()
            self.bias_o.randomize()

            self.learning_rate = 0.1

    def predict(self, input_arr):
        _,_,output = self.forward_propagation(input_arr)
        return mm.Matrix.toArray(output)
    
    def forward_propagation(self, input_arr):
        #the formula for forward propagation is you take the inputs as a matrix
        #multiply it by the weights add the bias and activate it do this for all layers 
        #then you get the output
        input = mm.Matrix.fromArray(input_arr)
        hidden = mm.Matrix.multiply(self.weights_ih, input)
        hidden.add(self.bias_h)
        hidden.map(sigmoid)

        output = mm.Matrix.multiply(self.weights_ho, hidden)
        output.add(self.bias_o)
        output.map(sigmoid)

        return input, hidden, output
    
    def back_propagation(self, prev_layer, errors, current_layer):
        #the formula for the deltas is lr * error * derivative * transposed previous layer
        gradients = mm.Matrix.map_static(current_layer, dsigmoid)
        gradients.multiply_scalar(errors)
        gradients.multiply_scalar(self.learning_rate)
        prev_layer_t = mm.Matrix.transpose(prev_layer)
        weight_deltas = mm.Matrix.multiply(gradients, prev_layer_t)
        return weight_deltas, gradients

    def update_params(self, weights, weight_delta, biases, bias_delta):
        #increasing the weights toward to output 
        weights.add(weight_delta)
        #the formula for bias deltas is lr * error which currently is the same as gradient
        biases.add(bias_delta)

    def train(self, input_arr, target_arr):
        #forward propagate through the network 
        input, hidden, outputs = self.forward_propagation(input_arr)
        #get the targets ready in matrix format
        targets = mm.Matrix.fromArray(target_arr)
        #get error for the output layer
        output_errors = mm.Matrix.subtract(targets, outputs)
        #back propagate and using gradient descent formula get the deltas to adjust the weights
        weight_ho_deltas, gradients = self.back_propagation(hidden, output_errors, outputs)
        #update values
        self.update_params(self.weights_ho, weight_ho_deltas, self.bias_o, gradients)
        #get the errors for the hidden layer
        ###################this is the part that i still have a hard time understanding################
        weights_ho_t = mm.Matrix.transpose(self.weights_ho)
        hidden_errors = mm.Matrix.multiply(weights_ho_t, output_errors)
        #again now that you have the errors back propagate using the gradient descent formula
        weight_ih_deltas, hidden_gradients = self.back_propagation(input, hidden_errors, hidden)
        #update vals
        self.update_params(self.weights_ih, weight_ih_deltas, self.bias_h, hidden_gradients)

    def mutate(self, rate):
        def apply_mutation(val):
            if random.randint(0, 5) < rate:
                return val + random.gauss(0, 0.1)
            else:
                return val

        self.weights_ih.map(apply_mutation)
        self.weights_ho.map(apply_mutation)
        self.bias_h.map(apply_mutation)
        self.bias_o.map(apply_mutation)


    def copy(self):
        copied_nn = NeuralNetwork(self.input_nodes, self.hidden_nodes, self.output_nodes)
        copied_nn.weights_ih = self.weights_ih.copy()
        copied_nn.weights_ho = self.weights_ho.copy()
        copied_nn.bias_h = self.bias_h.copy()
        copied_nn.bias_o = self.bias_o.copy()
        copied_nn.learning_rate = self.learning_rate
        return copied_nn
