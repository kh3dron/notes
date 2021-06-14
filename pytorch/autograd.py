import torch, torchvision


"Usage in Pytorch"
model = torchvision.models.resnet18(pretrained=True)
data = torch.rand(1, 3, 64, 64)
labels = torch.rand(1,1000)

prediction = model(data)
loss = (prediction - labels).sum()
loss.backward()

optim = torch.optim.SGC(model.parameters(), lr=1e-2, momentum=.9)
optim.step()

"Differentiation in Autograd"
a = torch.tensor([2., 3.], requires_grad = True)
b = torch.tensor([6., 4.], requires_grad = True)
Q = 3*a**2 - b**2