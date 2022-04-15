%matplotlib inline

import numpy as np
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')
np.random.seed(123)

from autogluon.core.utils.loaders import load_pd
train_data = load_pd.load('/content/drive/MyDrive/AutoGluon/COPD_NLP/NLP-LOS.csv')
test_data = load_pd.load('/content/drive/MyDrive/AutoGluon/COPD_NLP/NLP-LOS-TEST.csv')
subsample_size = 2200  # subsample data for faster demo, try setting this to larger values
train_data = train_data.sample(n=subsample_size, random_state=0)
train_data.head(10)

from autogluon.text import TextPredictor

predictor = TextPredictor(label='label', eval_metric='acc', path='./ag_sst')
predictor.fit(train_data, time_limit=1000)

embeddings = predictor.extract_embedding(test_data)
print(embeddings)

from sklearn.manifold import TSNE
X_embedded = TSNE(n_components=3, random_state=123).fit_transform(embeddings)
for val, color in [(1, 'red'), (2, 'blue'),(3, 'green')]:
    idx = (test_data['label'].to_numpy() == val).nonzero()
    plt.scatter(X_embedded[idx, 0], X_embedded[idx, 1], c=color, label=f'label={val}')
plt.legend(loc='best')