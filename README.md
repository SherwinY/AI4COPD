# AI fot COPD

![GitHub top language](https://img.shields.io/github/languages/top/sherwinY/AI4COPD)


## 简介
本项目是一个基于AutoGluon开发的COPD病人院内死亡概率及住院时长的预测模型。

## 环境
```Bash
pip install -U pip
pip install -U setuptools wheel

pip install autogluon

```

## 目录说明
[LOSPrediction.py](LOSPrediction.py)可以依据病例中的文本信息实现对COPD病人住院时长的预测  

[MortalityPrediction.py](MortalityPrediction.py)可以根据表格化的检查检验数据实现对COPD病人院内死亡率的预测  

[Embeddingvisualization.py](Embeddingvisualization.py)使用TSNE来可视化神经网络提取的嵌入，其中的每一个集群对应一个标签
