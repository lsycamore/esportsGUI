import PySimpleGUI as sg
import csv
import os.path
import pandas as pd
import howdoi
import sys
import os
dir = os.path.dirname(os.path.realpath(__file__))+r"\teams.csv"
df = pd.read_csv(dir, sep=',', engine='python')  # Header=None means you directly pass the columns names to the dataframe
teams = df[['_TeamName_','_points_']]
results=teams.sort_values("_points_")
data = results.values.tolist()               # read everything else into a list of rows
header_list = results.iloc[0].tolist()   # Uses the first row (which should be column names) as columns names
data = results[1:].values.tolist()    

layout = [[sg.Table(values=data, headings=header_list, display_row_numbers=True,
                        auto_size_columns=False, num_rows=min(25,len(data)))]]

window = sg.Window('Table', grab_anywhere=False)
event, values = window.Layout(layout).Read()

sys.exit(69)
#print(os.path.dirname(os.path.realpath(__file__))+r"\teams.csv")