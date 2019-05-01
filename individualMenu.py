import PySimpleGUI as sg
import csv
import os.path
import pandas as pd
import howdoi
import sys

#==============================================================================
def IndividualMenu():
    layout = [
                [sg.Text('Please select a function', auto_size_text=True)],  
                [sg.Text('1. Create a team', auto_size_text=True)],
                [sg.Text('2. Add results', auto_size_text=True)],
                [sg.Text('3. View results', auto_size_text=True)],
                [sg.Text('4. View ranked list', auto_size_text=True)],
                [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'),sg.Quit()]]      
    # Show the Window to the user    
    window = sg.Window('Main Menu', no_titlebar=True).Layout(layout)      
     # Event loop. Read buttons, make callbacks      
    while True:      
        # Read the Window    
      event, value = window.Read()      
        # Take appropriate action based on button      
      if event == '1':      
            CreateTeam()      
      elif event == '2':      
            AddResults()
      elif event == '3':
            ResultsMenu()
      elif event == '4':
            CreateRankList()
      elif event =='Quit'  or event is None:  
            window.Close()    
            break      
    
        # All done!      
    sg.PopupOK('Done')