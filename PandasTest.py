import PySimpleGUI as sg
import csv
import os.path
import pandas as pd
import howdoi
import sys
dir = r"\\socfs02.suffolkone.local\Students$\LS40548\BTEC\Unit 4 - Programming\Github clone\esportsGUI\teams.csv"
df = pd.read_csv(dir)
teams = df[['_TeamName_','_points_']]
#print(df[['_TeamName_','_points_']])
print(teams)
print(teams.sort_values("_points_"))
#/socfs02.suffolkone.local/Students$/LS40548/BTEC/Unit 4 - Programming/Github clone/esportsGUI/teams.csv