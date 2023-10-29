import torch

print(torch.__version__)


__all__ = ['TensorCalculator']

class TensorCalculator():

    def __init__(self):

        return None
    
##Returns an all-Zeros Tensor
    def tensor_zeros(self, dim_x, dim_y):
    
        zeros= torch.zeros(dim_x, dim_y)
        return zeros

    
#Returns an all-ones Tensor
    def tensor_ones(self,dim_x, dim_y):

        ones = torch.ones(dim_x,dim_y)

        return ones
    
#Returns a Tensor with random values
    def tensor_random(self, dim_x, dim_y):
        random = torch.rand(dim_x, dim_y)
        return random
    
#Returns the sum of 2 tensors
    def tensor_sum(self, tens1, tens2):
        return sum(tens1, tens2)

#Multiplies multiple matrices
    def tensor_matmil(self, t1, t2):
        return torch.matmul(t1, t2)

# Returns the transpose of a tensor
    def tensor_transpose(self, tens):
        return torch.transpose(tens, 0,1)

#inverse tensor

    def tensor_inverse(self, tens):
        return torch.inverse(tens)
    
t= TensorCalculator()

# Ones
ones=t.tensor_ones(2,2)
print(ones)

# ## Zeros
zeros=t.tensor_zeros(3,3)
print(zeros)

# Random

random=t.tensor_random(2,2)
print(random)

# Sum Tensors

tens1= t.tensor_random(4,4)
print("Tensor 1:", tens1)

tens2= t.tensor_random(4,4)
print("Tensor 2:", tens2)

sum= t.tensor_sum(tens1, tens2)
print(sum)

# Multiply tensors

mult=torch.matmul(tens1, tens2)
print(mult)

#transpose
tens_transpose= t.tensor_transpose(tens1)
print(tens_transpose)


#inverse
tens_inverse= t.tensor_inverse(tens2)
print(tens_inverse)
