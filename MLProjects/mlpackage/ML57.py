import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
dates = pd.date_range('20190101', periods=6, freq="D")
print( dates )   # It contains 6 dates as array

#dates =  DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
#               '2019-01-05', '2019-01-06'],
#              dtype='datetime64[ns]', freq='D')
print( dates[0]  )
print("\n\n", np.random.randn(6,4)  )


df= pd.DataFrame( np.random.randn(6,4),
            index=pd.date_range('20190101', periods=6, freq="D"),
            columns=['A',  'B',  'C',  'D']
                )
print("\n\n", df  )

df['E'] = df['A'].apply( lambda x : 1 if(x > 0) else 0 )
print(df)
print( df.groupby('E').size() )
print( "Headings in Dataframe : ", df.columns  )
print( "Row Headings in Dataframe : ", df.index  )
print( "Values in Dataframe : \n", df.values )


print( df.columns[ 1:3 ] )

#1)-See the top & bottom rows of the frame
#----------------------------------------------------------------------------------------------
print( df.head() )


print( df.tail(3) )

print( df.sample(3) )

print( df.describe() )
print( df.describe(include="all") )

print( df.T )
print("\n\n")

print( "Sorted values : \n")
print(  df.sort_values( by='B',ascending=True )  )

#print( "original values : \n ", df  )
#del df["C"]
#print( df )

#Selecting a single column, which yields a Series, equivalent to df.A
print( df.A )
print( )
print( df['A'] )



print( df['2019-01-01':'2019-01-03'] )

#Selecting via [], which slices the rows.
print( df[0:3] )

#print( specific rows by using range of index values
print( df['20190102':'20190104'] )


#Selection by Label
#For getting a cross section using a label
print( df.loc[dates[0]] )


#Selecting on a multi-axis by label
print( df.loc[ : , ['A','B'] ] )

#Boolean Indexing
print( df.A  )

print( "\n\n"  )
print( df.A  > 0  )

print( "\n\n" )
print( df[ df.A > 0 ]   )
#                   A         B         C         D
#   2019-01-04  0.194764 -0.877930 -2.115444 -1.564107
#   2019-01-05  0.960763 -0.913735  0.077043 -2.103443

print( df["B"][ df.A > 0 ] )

df2 = df.copy()
df2['E'] = ['one', 'one','two','three', 'four','three']
print( df2 )

print( df2[  df2['E'].isin(['two','four'])  ]  )

#Stats
#Performing a descriptive statistic
print( df.mean() )

print( "\n\nMean of B : " , df.B.mean()  )

print( "\n\nMean of B : " , df['B'].mean()  )
    #Assignment Task
print( df['A'][ df.B > df.B.mean() ] )
#Same operation on the other axis
print( df.mean(axis=1) )

print( "\n\nAfter deletion \n " )
print( df2.drop(df2.index[2:4], axis=0 )  )   #0 -Row Deletion

print( "\n\nAfter deletion \n " )
print( df2.drop(df2.columns[1:3], axis=1)   ) #1 -Column Deletion
#print( "\n\nAfter deletion \n " )
print( df2 )

#writing to MS Excel
#Install (1)openpyxl  and (2)xlrd pluginnns
#Writing to an excel file
df.to_excel('outputData.xlsx', sheet_name='Sheet1')
