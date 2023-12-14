
# reading fies from computer
import os
import pandas as pd

folder_path = "./Crime_socialmedia_Files"

def search(country,word):
        
    # Get a list of all files in the folder
    file_list = [file for file in os.listdir(folder_path) if file.startswith(country)]
    c=0
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
       
        with open(file_path, 'r') as file:
                content = file.read()
                c+=content.lower().count(word)
    avg=c/len(file_list)
    return avg

def years(country):
    return len([file for file in os.listdir(folder_path) if file.startswith(country)])

data={
    'Contry':['Canada','Denmark','Germany','Luxemberg','Wales'],
    'drug':[search('Canada','drug'),search('Denmark','drug'),search('Germany','drug'),search('Luxemberg','drug'),search('Wales','drug')],
    'kidnap':[search('Canada','kidnap'),search('Denmark','kidnap'),search('Germany','kidnap'),search('Luxemberg','kidnap'),search('Wales','kidnap')],
    'murder':[search('Canada','murder'),search('Denmark','murder'),search('Germany','murder'),search('Luxemberg','murder'),search('Wales','murder')],
    'extortion':[search('Canada','extortion'),search('Denmark','extortion'),search('Germany','extortion'),search('Luxemberg','extortion'),search('Wales','extortion')],
    'fraud':[search('Canada','fraud'),search('Denmark','fraud'),search('Germany','fraud'),search('Luxemberg','fraud'),search('Wales','fraud')],
    'No. of years':[years('Canada'),years('Denmark'),years('Germany'),years('Luxemberg'),years('Wales')]
}

df=pd.DataFrame(data)
print(df)