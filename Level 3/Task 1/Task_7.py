import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
df=pd.read_csv("Dataset .csv")
df.head()
y=df["Aggregate rating"]
x=df.drop(["Aggregate rating","Restaurant Name","Address","Locality Verbose"],axis=1)
le=LabelEncoder()
for col in x.select_dtypes(include="object").columns:
    x[col]=le.fit_transform(x[col])
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
lr=LinearRegression()
lr.fit(x_train,y_train)
y_pred_lr=lr.predict(x_test)
dt=DecisionTreeRegressor(random_state=42)
dt.fit(x_train,y_train)
y_pred_dt=dt.predict(x_test)
rf=RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(x_train,y_train)
y_pred_rf=rf.predict(x_test)
def evaluate_model(y_test,y_pred,model_name):
    result=f"""
{model_name}
MAE:{mean_absolute_error(y_test,y_pred)}
RMSE:{np.sqrt(mean_squared_error(y_test,y_pred))}
R2 Score : {r2_score(y_test,y_pred)}
{"-"*30}
"""
    return result
print(evaluate_model(y_test,y_pred_lr,"Linear Regression"))
print(evaluate_model(y_test,y_pred_dt,"Decision Tree"))
print(evaluate_model(y_test,y_pred_rf,"Random Forest"))
with open("Task_7_output_text.txt","w") as f:
    f.write(str(evaluate_model(y_test,y_pred_lr,"Linear Regression")))
    f.write(str(evaluate_model(y_test,y_pred_dt,"Decision Tree")))
    f.write(str(evaluate_model(y_test,y_pred_rf,"Random Forest"))) 
    
