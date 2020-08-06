import pandas as pd 

items = {'Images' : pd.Series(data = [1]),
         'left_side': pd.Series(data = [1]),
         'right_side': pd.Series(data = [1]),
         'throttle': pd.Series(data = [1]),
         'break':  pd.Series(data = [1])}

data = pd.DataFrame(items)