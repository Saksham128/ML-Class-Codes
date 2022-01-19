import pandas as pd
import numpy as np
dates = pd.date_range('20190101', periods=6, freq="D")
print( dates )   # It contains 6 dates as array

#dates =  DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
#               '2019-01-05', '2019-01-06'],
#              dtype='datetime64[ns]', freq='D')
print( dates[0]  )