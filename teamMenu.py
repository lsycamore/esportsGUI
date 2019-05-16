
import PySimpleGUI as sg
import csv
import os.path
import pandas as pd
import howdoi
import sys

#==============================================================================
def tmenu():

    
    layout = [
                [sg.Text('Please select a function', auto_size_text=True)],  
                [sg.Text('1. Create a team', auto_size_text=True)],
                [sg.Text('2. Add results', auto_size_text=True)],
                [sg.Text('3. View results', auto_size_text=True)],
                [sg.Text('4. View ranked list', auto_size_text=True)],
                [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'),sg.Quit()]]      
    # Show the Window to the user    
    window = sg.Window('Main Menu', no_titlebar=False).Layout(layout)      
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
#==============================================================================
def CreateTeam():    

    layout = [      
              [sg.Text('Please enter the new Team')],      
              [sg.Text('Team Name', size=(15, 1)), sg.InputText('', key='_TeamName_')],           
              [sg.Text('Member1', size=(15, 1)), sg.InputText('Name', key='_member1_')],      
              [sg.Text('Member2', size=(15, 1)), sg.InputText('Name', key='_member2_')],
              [sg.Text('Member3', size=(15, 1)), sg.InputText('Name', key='_member3_')],      
              [sg.Text('Member4', size=(15, 1)), sg.InputText('Name', key='_member4_')],
              [sg.Text('Member5', size=(15, 1)), sg.InputText('Name', key='_member5_')],      
              [sg.Submit(), sg.Cancel()]      
             ]      

    window = sg.Window('Simple data entry GUI').Layout(layout)  

    event, values = window.Read()  

    window.Close()
    file_exists = os.path.isfile("teams.csv")
    with open("teams.csv", "a") as csvfile:
        colnames = ["_TeamName_", "_member1_","_member2_","_member3_","_member4_","_member5_","_points_",]
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        fields = [values['_TeamName_'], values['_member1_'], values['_member2_'],values['_member3_'], values['_member4_'], values['_member5_']]
        
        if not file_exists:
            writer.writerow(colnames)

    
        writer.writerow(fields)



    print(event, values['_TeamName_'], values['_member1_'], values['_member2_'])    
#==============================================================================
def AddResults():  
    colnames = ["_TeamName_", "_member1_","_member2_","_member3_","_member4_","_member5_",]
    data = pd.read_csv('teams.csv', names=colnames, header = 0)
    layout = [      
            [sg.Text('Please select team 1'),sg.Drop(key = "Team1",values=(data._TeamName_.tolist()), auto_size_text=True),sg.Text('Goals:'),sg.InputText('Name', key='_goals1_')],      
            [sg.Text('Please select team 2'),sg.Drop(key = "Team2",values=(data._TeamName_.tolist()), auto_size_text=True),sg.Text('Goals:'),sg.InputText('Name', key='_goals2_')],           
            [sg.Submit(), sg.Cancel()]      
            ]      
    
    window = sg.Window('Simple data entry GUI').Layout(layout)  
    
    event, values = window.Read()  
    
    window.Close()
    file_exists = os.path.isfile("scores.csv")
    with open("scores.csv", "a") as csvfile:
        colnames = ["_TeamName_", "_Goals_","_Goals_","_TeamName_",]
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        fields = [values['Team1'], values['_goals1_'], values['_goals2_'],values['Team2'],]
        
        if not file_exists:
            writer.writerow(colnames)

    
        writer.writerow(fields)
   # with open("teams.csv", "w+") as csvfile:

#==============================================================================
def ResultsMenu():
    sg.SetOptions(auto_size_buttons=True)
    # --- populate table with file contents --- #
    dir = os.path.dirname(os.path.realpath(__file__))+r"\teams.csv"
    data = []
    header_list = []
    

    try:
        df = pd.read_csv(dir, sep=',', engine='python', header=None)  # Header=None means you directly pass the columns names to the dataframe
        data = df.values.tolist()               # read everything else into a list of rows
        header_list = df.iloc[0].tolist()   # Uses the first row (which should be column names) as columns names
        data = df[1:].values.tolist()       # Drops the first row in the table (otherwise the header names and the first row will be the same)
    except:
        sg.PopupError('Error reading file')
        sys.exit(69)

    layout = [[sg.Table(values=data, headings=header_list, display_row_numbers=True,
                            auto_size_columns=False, num_rows=min(25,len(data)))]]

  

    layout = [[sg.Table(values=data, headings=header_list, display_row_numbers=True,
                            auto_size_columns=False, num_rows=min(25,len(data)))]]

    window = sg.Window('Table', grab_anywhere=False)
    event, values = window.Layout(layout).Read()

    sys.exit(69)

#==============================================================================
def CreateRankList():
    sg.SetOptions(auto_size_buttons=True)
    # --- populate table with file contents --- #

    data = []
    header_list = []

    try:
        df = pd.read_csv("teams.csv", sep=',', engine='python', header=None)  # Header=None means you directly pass the columns names to the dataframe
        data = df.values.tolist()               # read everything else into a list of rows
        header_list = df.iloc[0].tolist()   # Uses the first row (which should be column names) as columns names
        data = df[1:].values.tolist()       # Drops the first row in the table (otherwise the header names and the first row will be the same)

    except:
        sg.PopupError('Error reading file')
        sys.exit(69)
  

    layout = [[sg.Table(values=data, headings=header_list, display_row_numbers=True,
                            auto_size_columns=False, num_rows=min(25,len(data)))]]

    window = sg.Window('Table', grab_anywhere=False)
    event, values = window.Layout(layout).Read()


#==============================================================================