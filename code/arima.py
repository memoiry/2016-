import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data = pd.DataFrame({'value':np.log([200000.0, 253440.0, 197120.0, 98560.0, 122000.0, 171520.0, 252120.0, \
196093.0, 52200.0, 81187.0, 73600.0, 130600.0, 120000.0, 110000,140000, \
163360.0, 290040.0, 225587.0, 20200.0, 99453.0, 186000.0, 344160.0, \
267678.0, 15200.0, 63280.0, 202560.0, 387600.0, 301467.0, 28800.0, \
91813.0, 204400.0, 422160.0, 328347.0, 27120.0, 100053.0, 203200.0, \
425160.0, 330680.0, 5320.0, 82200.0, 216000.0, 398520.0, 309960.0, \
59000.0, 123000.0, 198640.0, 386320.0, 299633.0, 26120.0, 86227.0])})


forecastnum = 5*6
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
data.plot()
plt.show()

from statsmodels.graphics.tsaplots import plot_acf
plot_acf(data).show()

from statsmodels.tsa.stattools import adfuller as ADF 

print 'ADF test result:', ADF(data['value'])

D_data = data.diff().dropna()
D_data.columns = ['diff value']
D_data.plot()
plt.show()
plot_acf(D_data).show()
from statsmodels.graphics.tsaplots import plot_pacf
plot_pacf(D_data).show()
print 'diff seq ADF test result:', ADF(D_data['diff value'])

from statsmodels.stats.diagnostic import acorr_ljungbox
print 'dff white noise test result:', acorr_ljungbox(D_data, lags = 1)

from statsmodels.tsa.arima_model import ARIMA


model = ARIMA(data, (1,1,1)).fit()
model.summary2()
model.forecast(5*6)

