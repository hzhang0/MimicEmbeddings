#!/h/haoran/anaconda3/bin/python
#SBATCH --output=/h/haoran/projects/mimic_embeddings/output
#SBATCH --partition=cpu
#SBATCH -c 58

import pandas as pd
import numpy as np
import gensim
import sys
import nltk
import pickle
import os
from sklearn.model_selection import ParameterGrid

# Necessary to add cwd to path when script run
# by SLURM (since it executes a copy)
sys.path.append(os.getcwd())

df = pd.read_csv('notes.csv') #2,083,180 notes
df = df[~(df['iserror'] == 1)] #886 notes with errors

termsToRemove = ['Admission Date:', 'Discharge Date:', 'Service:', 'ADDENDUM:', 'Dictated By:', 'Completed by:', 'D:', 'T:', 'JOB#:', '\?\?\?\?\?\?', 'INTERPRETATION:', 'Findings', 'Attending Physician:', 'Referral date:']

texts = df['text'].str.replace(r'(%s)'%('|'.join(termsToRemove)),'').str.replace(r'\[\*\*.*?\*\*\]', '')
toks = texts.str.lower().apply(nltk.word_tokenize).values
print(sum(map(len, toks)), 'tokens')

#param_grid = {'size': [100, 200, 300],
#        'min_count': [5, 10, 50],
#        'window': [1, 5, 20]}

param_grid = {'size': [200, 300],
        'min_count': [2,3,4],
        'window': [20]        
        }

for i in ParameterGrid(param_grid):
    #skipgrams
    model = gensim.models.Word2Vec(toks, sg=1, workers = 80, seed =42, **i)
    pickle.dump(model, open('embeddings/%sd_%sc_%sw'%(i['size'], i['min_count'], i['window']), 'wb'))



