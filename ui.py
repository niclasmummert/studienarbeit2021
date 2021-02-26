import base64
import csv
import io
import os
import random
import importlib.util
import sys

import pandas as pd
import PIL
import PySimpleGUI as sg
from PIL import Image

spec = importlib.util.spec_from_file_location("knn_module", "knn_module.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

spec = importlib.util.spec_from_file_location("ml_module", "ml_module.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

spec = importlib.util.spec_from_file_location("bewertung", "bewertung.py")
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


from bewertung import open_window
from knn_module import knn_prediction
from ml_module import ml_prediction
import importlib
import importlib

new_size = (680,680)
filename = "user_df.csv"
folder = r"images1"
n = 2

def convert_to_bytes(file_or_bytes, resize=None):
    '''
    Will convert into bytes and optionally resize an image that is a file or a base64 bytes object.
    Turns into  PNG format in the process so that can be displayed by tkinter
    :param file_or_bytes: either a string filename or a bytes base64 image object
    :type file_or_bytes:  (Union[str, bytes])
    :param resize:  optional new size
    :type resize: (Tuple[int, int] or None)
    :return: (bytes) a byte-string object
    :rtype: (bytes)
    '''
    if isinstance(file_or_bytes, str):
        img = PIL.Image.open(file_or_bytes)
    else:
        try:
            img = PIL.Image.open(io.BytesIO(base64.b64decode(file_or_bytes)))
        except Exception as e:
            dataBytesIO = io.BytesIO(file_or_bytes)
            img = PIL.Image.open(dataBytesIO)

    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height/cur_height, new_width/cur_width)
        img = img.resize((int(cur_width*scale), int(cur_height*scale)), PIL.Image.ANTIALIAS)
    with io.BytesIO() as bio:
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()

def main():
    
    fields = ["prev_suspensiontype", "surfacetype", "suspensiontype"]
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader() 

    img_iterator = 0
    last_suspensiontype = "Normal"
    output = "Normal"
    currentsuspensiontype = "Normal"
    sg.ChangeLookAndFeel("Dark")
    comfort_btn = sg.Button("Comfort", button_color=("white", "grey"), key="Comfort", size=(6,1))
    normal_btn = sg.Button("Normal", button_color=("white", "grey"), key="Normal", size=(6,1))
    sport_btn = sg.Button("Sport", button_color=("white", "grey"), key="Sport", size=(6,1))
    sportplus_btn = sg.Button("Sport+", button_color=("white", "grey"), key="Sportplus", size=(6,1))
    abbruch_btn = sg.Button(button_text="Abbruch", button_color=("white", "grey"))
    weiter_btn = sg.Button(button_text="Weiter", button_color=("white", "blue"), disabled=True)
    png_files = [folder + "/" + f for f in os.listdir(folder) if ".png" or ".PNG" in f]

    layout=[[sg.Image(key="-showImage")],
            [comfort_btn, normal_btn, sport_btn, sportplus_btn],
            [abbruch_btn, weiter_btn]]

    window = sg.Window("UI", layout, resizable=True, text_justification="center", element_justification="left", finalize=True, auto_size_buttons=True, location=(350,150))
    window["-showImage"].update(data=convert_to_bytes(png_files[img_iterator], resize=new_size))

    while True:
        window[output].set_size((12,2)) # ouput wird ausgegeben
        event, values = window.read()
            
        if event == sg.WIN_CLOSED or event == "Abbruch":
            break
        if event == "Comfort" or event == "Normal" or event == "Sport" or event == "Sportplus":
            window[currentsuspensiontype].update(button_color=("white", "grey"))
            window[event].update(button_color=("white", "green"))
            weiter_btn.update(disabled=False)
            #last_suspensiontype = currentsuspensiontype   # suspensiontype Wert des vorherigen Bilds in last_suspensiontype gespeichert
            currentsuspensiontype = event # ausgewählte suspensiontype wird in currentsuspensiontype gespeichert
        if event == "Weiter":
            weiter_btn.update(disabled=True)
            window[currentsuspensiontype].update(button_color=("white", "grey"))
            current_surfacetype = ml_prediction(png_files[img_iterator]) # current/old Bild analysiert
            img_iterator = img_iterator + 1 # wechseln auf nächstes Bild
            window[output].set_size((6,1)) # alter ML-gestützer Button kleiner gemacht
            next_surfacetype = ml_prediction(png_files[img_iterator]) # next/current Bild analysiert
            print("Image Number: ", img_iterator)           # img_iterator zeigt Wert neues Bild
            print(next_surfacetype, "  ", last_suspensiontype) # suspensiontype des vorherigen Bilds und next/current Bild   
            output = knn_prediction(last_suspensiontype, next_surfacetype, img_iterator) # Analyse des next/current Bilds zur verhebung des Buttons 
            print("analysed surfacetype for the current/old image: " , current_surfacetype)
            print("analysed surfacetype for the next/current image: ", next_surfacetype) # next/current Bild analysiert
            print("predicted output for the next/current image: ", output) # Analyse wird ausgegeben
            #window[output].set_size((12,2)) # ouput wird ausgegeben
            with open(filename, "a+", newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = fields)
                row = [{"prev_suspensiontype":last_suspensiontype,"surfacetype":current_surfacetype,"suspensiontype":currentsuspensiontype}]
                writer.writerows(row)
            df = pd.read_csv(filename)
            print(df)
            last_suspensiontype = currentsuspensiontype   # suspensiontype Wert des vorherigen Bilds in last_suspensiontype gespeichert
            if img_iterator == n:
                sec_window = open_window()
                window.close()
            window["-showImage"].update(data=convert_to_bytes(png_files[img_iterator], resize=new_size))
    os.remove(filename)
    window.close()

if __name__ == "__main__":
    main()
