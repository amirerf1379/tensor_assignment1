# Tensor Assignment

tensor_hw is a Python module created for this assignment that perfomrs operations with Pytorch 2-dimensional Tensors

## Assignment Methods

In this assignment, we have created methods that return:
- All-Zeros Tensor
- All-Ones Tensor
- Random values Tensor
- Sum of two tensor
- Multiplication of two tensors
- Transpose a tensor
- Inverse a tensor
- 
## Installation

You can install TensorCalculator using `pip`:

```bash
pip install -U git+https://github.com/amirerf1379/tensor_assignment1.git
```
## Usage

import TensorCalculator

### Ones
ones=t.tensor_ones(2,2)
print(ones)

### Zeros
zeros=t.tensor_zeros(3,3)
print(zeros)

### Random

random=t.tensor_random(2,2)
print(random)

### Sum Tensors

tens1= t.tensor_random(4,4)
print("Tensor 1:", tens1)

tens2= t.tensor_random(4,4)
print("Tensor 2:", tens2)

sum= t.tensor_sum(tens1, tens2)
print(sum)

### Multiply tensors

mult=torch.matmul(tens1, tens2)
print(mult)

### Transpose
tens_transpose= t.tensor_transpose(tens1)
print(tens_transpose)


### Inverse
tens_inverse= t.tensor_inverse(tens2)
print(tens_inverse)



