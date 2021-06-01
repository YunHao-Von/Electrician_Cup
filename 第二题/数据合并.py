import pandas as pd
import numpy as np
rnn=np.array(pd.read_csv('RNN预测结果.csv')['指数'].tolist())*0.5
arima=np.array(pd.read_csv('ARIMA预测结果.csv')['指数'].tolist())*0.5
result=rnn+arima
result=pd.DataFrame({
    '指数':result
})
result.to_csv('最终预测结果.csv',index=False)