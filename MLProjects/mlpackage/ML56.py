import pandas as pd
import numpy as np
print("\n\n", np.random.randn(6,4)  )

df= pd.DataFrame( np.random.randn(6,4),
            index=pd.date_range('20190101', periods=6, freq="D"),
            columns=['A',  'B',  'C',  'D']
                )
print("\n\n", df  )

df['E'] = df['A'].apply( lambda x : 1 if(x > 0) else 0 )
print(df)