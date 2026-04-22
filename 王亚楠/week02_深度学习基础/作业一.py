import numpy as np
import torch
import json
import matplotlib.pyplot as plt
from torch import nn

"""
基于pytorch框架编写模型训练
完成一个多分类任务的训练，一个随机向量，哪一维数字最大就属于第几类
"""

# 1. 数据
def bulid_sample_data():
  x = np.random.random(5)
  row_max = np.max(x, axis = -1, keepdims = True)
  y = np.argmax(x)
  return x, y

def build_dataset(total_sample_num):
  X, Y = [], []
  for i in range(total_sample_num):
    x, y = build_sample_data()
    X.append(x)
    Y.append(y)
  return torch.FloatTensor(X), torch.LongTensor(Y)

# 2. 模型

class TorchModel(nn.Module):
  def __init__(self, input_size):
    super(TorchModel, self).__init__()
    self.linear = nn.Linear(inpur_size, input_size)
    self.loss = nn.CorssEntropyLoss()
  def forword(self, x, y = None):
    y_pred = self.linear(x)
    if y is not None:
      return self.loss(y_pred, y)
    else:
      y_pred = torch.softmax(y_pred, dim = -1)
      return y_pred

# 3. 测试 evaluate
def evaluate(model):
  model.eval()
















