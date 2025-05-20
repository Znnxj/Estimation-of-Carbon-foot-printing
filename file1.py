#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
df = pd.read_csv('CO2 dataset.csv')


# In[2]:


df


# In[3]:


df.info()


# In[4]:


df.isnull().sum()


# In[6]:


df_cleaned = df.dropna(subset=['carbon_intensity_avg'])


# In[7]:


df_cleaned.isnull().sum()


# In[9]:


x = df_cleaned[['zone_key','Country','no_hours_with_data','carbon_intensity_avg']]

x


# In[12]:


x.to_csv('newco2.csv',index=False)


# In[10]:


# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Load your dataset
df = x

# Separate features and target variable
X = df[['no_hours_with_data', 'Country', 'zone_key']]
y = df['carbon_intensity_avg']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a preprocessor for categorical variables
categorical_features = ['Country', 'zone_key']
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

# Create a column transformer
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_features)
    ])

# Create a pipeline with preprocessor and linear regression model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Train the model
model.fit(X_train, y_train)

# Save the model using joblib
joblib.dump(model, 'linear_regression_model.joblib')

# Now you can use the saved model for predictions
loaded_model = joblib.load('linear_regression_model.joblib')

# Example prediction
new_data = pd.DataFrame({'no_hours_with_data': [5000], 'Country': ['Australia'], 'zone_key': ['AUS-NSW']})
prediction = loaded_model.predict(new_data)
print("Predicted carbon intensity:", prediction)


# In[ ]:




