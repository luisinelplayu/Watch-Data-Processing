# Watch Data processing functions

import pandas as pd

# Watch data open function

def watch_data_open(csvpath):
    # Open as a dataframe with pandas
    csv = pd.read_csv(csvpath)
    return csv