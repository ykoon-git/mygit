import pandas as pd 
from ludwig.api import LudwigModel

df = pd.read_csv('rotten_tomatos.csv')
model = LudwigModel(config='config.yaml')

results = model.train(dataset=df)

