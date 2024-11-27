#importing statistics
import statistics as st
#importing pandas
import pandas as pd
#importing numpy
import numpy as np
#reading file
rf=pd.read_csv("tint.csv")
print(rf.info())
#checking for null values
rf.isnull().any()
rf['Gender'].value_counts
#
nominal_data=['Gender','Embarked']
gancat=['male','female']
rf['Gender']=pd.Categorical(rf['Gender'])
medianindex=np.median(rf['Gender'].cat.codes)
print("the median index is " ,medianindex)
mediangender=gancat[int(medianindex)]
print(mediangender)
#
#
rf['Embarked']=pd.Categorical(rf['Embarked'])
embcat=['S','C','Q']
embindex=np.median(rf['Embarked'].cat.codes)
print("the embarked index is " ,embindex)
meanemb=embcat[int(embindex)]
print("the mean of embark is " ,meanemb)