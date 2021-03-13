import torch
import numpy as np

"TENSOR INITIALIZATION"

"From data:"
data = [[1,2],[3,4]]
x_data = torch.tensor(data)

"From numpy:"
np_array = np.array(data)
x_np = torch.from_numpy(np_array)

"From other tensor: retains data type and shape, unless specified"
x_ones = torch.ones_like(x_data)
print(f"Ones Tensor: \n{x_ones} \n")
x_rand = torch.rand_like(x_data, dtype=torch.float)
print(f"Random Tensor: \n{x_rand} \n")

"With random or constant values"
shape = (2, 3)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)
print(f"Random Tensor: \n {rand_tensor} \n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor}")

"Tensor Attributes"
tensor = torch.rand(3, 4)
print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")

"Tensor Operations"
if torch.cuda.is_available():
    tensor = tensor.to('cuda')

"Numpy-like indexing and slicing"
tensor = torch.ones(4,4)
tensor[:,1] = 0 #Y:all, X:1
print(tensor)
t1 = torch.cat([tensor, tensor, tensor], dim=1) #0 is vertical, 1 is horizontal
print(t1)

"Multiplying tensors"
#The element-wise product:
print(f"tensor.mul(tensor) \n {tensor.mul(tensor)}")
print(f"tensor * tensor \n {tensor * tensor}")
#The matrix multiplication:
print(f"tensor.matmul(tensor.T) \n {tensor.matmul(tensor.T)}")
print(f"tensor @ tensor.T \n {tensor @ tensor.T}")

"In-place operations: have a _"
print(tensor, "\n")
tensor.add_(5)
print(tensor)

"Bridge with NumPy: CPU Tensors and Numpuy arrays can share memory locations"
t = torch.ones(5)
print(f"t: {t}")
n = t.numpy()
print(f"n: {n}")
t.add_(1)
print(f"t: {t}")
print(f"n: {n}")
"Numpy array to Tensor"
n = np.ones(5)
t = torch.from_numpy(n)
np.add(n, 1, out=n)
print(f"t: {t}")
print(f"n: {n}")

"""
christ, I need to learn linear algebra
resume here: https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html

"""