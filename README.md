# FLAPPYBIRD-NEUROEVOLUTION

These are alos part of some of the coding train challenges. I changed the implementation to python and my favorite game engine PYXEL. The flappy Bird file uses the neural network and the matrix manipulation files to learn to go thorugh the maze of pipes and jump at the right times. Combining genetic algorithms and neural networks to create neuroevolution!

## Functionalities

### 1. NeuralNetwork Class

#### Initialization

- `__init__(numI, numH, numO)`: Initializes the neural network with the specified number of input, hidden, and output nodes.

#### Training

- `train(input_arr, target_arr)`: Trains the neural network using backpropagation with the provided input and target arrays.

#### Prediction

- `predict(input_arr)`: Predicts the output for a given input array.

#### Mutation

- `mutate(rate)`: Introduces random mutations to the weights and biases of the neural network with a given mutation rate.

#### Copy

- `copy()`: Creates a deep copy of the neural network.

### 2. Activation Functions

- `sigmoid(x)`: Sigmoid activation function.
- `dsigmoid(y)`: Derivative of the sigmoid activation function.

### 3. Forward Propagation

- `forward_propagation(input_arr)`: Performs forward propagation to compute the output of the neural network for a given input array.

### 4. Backpropagation

- `back_propagation(prev_layer, errors, current_layer)`: Performs backpropagation to compute the weight deltas and gradients for adjusting the weights and biases.

### 5. Update Parameters

- `update_params(weights, weight_delta, biases, bias_delta)`: Updates the weights and biases of the neural network using the computed weight deltas and biases.

## Matrix Manipulation Library Documentation

This matrix manipulation library provides various functionalities for performing operations on matrices.

### 1. Matrix Class

#### Initialization

- `__init__(rows, cols)`: Initializes a matrix with the specified number of rows and columns.

#### Addition

- `add(n)`: Adds the elements of another matrix `n` to the current matrix.

#### Copy

- `copy()`: Creates a deep copy of the matrix.

#### Subtraction

- `subtract(a, b)`: Subtracts matrix `b` from matrix `a` and returns the result.

#### Mapping

- `map(fn)`: Applies a function `fn` to each element of the matrix.

#### Static Mapping

- `map_static(m, fn)`: Applies a function `fn` to each element of the matrix `m` and returns the result.

#### Conversion

- `fromArray(arr)`: Converts a 1D array `arr` into a column matrix.
- `toArray(m)`: Converts a matrix `m` into a 1D array.

#### Multiplication

- `multiply(a, b)`: Multiplies matrix `a` by matrix `b` and returns the result.

#### Scalar Multiplication

- `multiply_scalar(n)`: Multiplies each element of the matrix by a scalar `n`.

#### Transpose

- `transpose(m)`: Transposes the matrix `m`.

#### Randomization

- `randomize()`: Assigns random values to the elements of the matrix within the range [-1, 1].

#### Print

- `print()`: Prints the matrix elements.
