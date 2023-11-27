from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import time
import pandas as pd
import urllib.request, json
import os
from dotenv import load_dotenv

def all_df_pexels(style_list):
    url = "".format(os.environ.get("PEXEL_API_KEY"))
    response = urllib.request.urlopen(url)
    api = response.read()


    """Fuction gets API data from a list of styles 
    and creates one full df with the required columns"""
    style_df = []
    
    for index, style in enumerate(style_list):
        data_list = []
        for i in range(1,10):
                photos = api.search(style, page=i, results_per_page=45)['photos']
                data_list.append(pd.DataFrame.from_dict(photos))
                
        merged = pd.concat(data_list)
        merged = merged[['id', 'alt']]
        merged['style'] = style
        style_df.append(merged)
    
    all_df = pd.concat(style_df)
    
    return all_df

sgd = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None)),
               ])
sgd.fit(X_train, y_train)
%time
y_pred = sgd.predict(X_test)
print('accuracy %s' % accuracy_score(y_pred, y_test))