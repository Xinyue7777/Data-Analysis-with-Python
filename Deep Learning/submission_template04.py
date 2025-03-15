import numpy as np
import torch
from torch import nn
from torch.nn import functional as F

class ConvNet(nn.Module):
    def __init__(self):
        def __init__(self):
        super().__init__()
        self.layer = nn.Linear(10, 2)
    def forward(self, x):
        return self.layer(x)
# 初始化模型并加载训练好的权重（如果有）
model = MyModel()
# 保存模型（请确保已执行过训练代码）
torch.save(model.state_dict(), "model.pth")
print("模型已保存为 model.pth")
