import PySimpleGUI as sg
from openpyxl import Workbook
from openpyxl.reader.excel import load_workbook

def convFalseTrue(value):
    if value == True:
        return 1
    else:
        return 0

def maptoexcel(values):
    mywb = load_workbook("AuswertungBefragung.xlsx")
    mysheet = mywb["A0-1"]
    value = convFalseTrue(values[15])
    mysheet["C3"] = value
    value = convFalseTrue(values[14])
    mysheet["D3"] = value
    value = convFalseTrue(values[13])
    mysheet["E3"] = value
    value = convFalseTrue(values[12])
    mysheet["F3"] = value
    value = convFalseTrue(values[11])
    mysheet["G3"] = value
    value = convFalseTrue(values[25])
    mysheet["C4"] = value
    value = convFalseTrue(values[24])
    mysheet["D4"] = value
    value = convFalseTrue(values[23])
    mysheet["E4"] = value
    value = convFalseTrue(values[22])
    mysheet["F4"] = value
    value = convFalseTrue(values[21])
    mysheet["G4"] = value
    value = convFalseTrue(values[35])
    mysheet["C5"] = value
    value = convFalseTrue(values[34])
    mysheet["D5"] = value
    value = convFalseTrue(values[33])
    mysheet["E5"] = value
    value = convFalseTrue(values[32])
    mysheet["F5"] = value
    value = convFalseTrue(values[31])
    mysheet["G5"] = value
    value = convFalseTrue(values[45])
    mysheet["C6"] = value
    value = convFalseTrue(values[44])
    mysheet["D6"] = value
    value = convFalseTrue(values[43])
    mysheet["E6"] = value
    value = convFalseTrue(values[42])
    mysheet["F6"] = value
    value = convFalseTrue(values[41])
    mysheet["G6"] = value
    value = convFalseTrue(values[55])
    mysheet["C7"] = value
    value = convFalseTrue(values[54])
    mysheet["D7"] = value
    value = convFalseTrue(values[53])
    mysheet["E7"] = value
    value = convFalseTrue(values[52])
    mysheet["F7"] = value
    value = convFalseTrue(values[51])
    mysheet["G7"] = value
    value = convFalseTrue(values[65])
    mysheet["C8"] = value
    value = convFalseTrue(values[64])
    mysheet["D8"] = value
    value = convFalseTrue(values[63])
    mysheet["E8"] = value
    value = convFalseTrue(values[62])
    mysheet["F8"] = value
    value = convFalseTrue(values[61])
    mysheet["G8"] = value
    value = convFalseTrue(values[75])
    mysheet["C9"] = value
    value = convFalseTrue(values[74])
    mysheet["D9"] = value
    value = convFalseTrue(values[73])
    mysheet["E9"] = value
    value = convFalseTrue(values[72])
    mysheet["F9"] = value
    value = convFalseTrue(values[71])
    mysheet["G9"] = value
    value = convFalseTrue(values[85])
    mysheet["C10"] = value
    value = convFalseTrue(values[84])
    mysheet["D10"] = value
    value = convFalseTrue(values[83])
    mysheet["E10"] = value
    value = convFalseTrue(values[82])
    mysheet["F10"] = value
    value = convFalseTrue(values[81])
    mysheet["G10"] = value
    value = convFalseTrue(values[95])
    mysheet["C11"] = value
    value = convFalseTrue(values[94])
    mysheet["D11"] = value
    value = convFalseTrue(values[93])
    mysheet["E11"] = value
    value = convFalseTrue(values[92])
    mysheet["F11"] = value
    value = convFalseTrue(values[91])
    mysheet["G11"] = value
    value = convFalseTrue(values[105])
    mysheet["C12"] = value
    value = convFalseTrue(values[104])
    mysheet["D12"] = value
    value = convFalseTrue(values[103])
    mysheet["E12"] = value
    value = convFalseTrue(values[102])
    mysheet["F12"] = value
    value = convFalseTrue(values[101])
    mysheet["G12"] = value
    mywb.save("AuswertungBefragung.xlsx")

def open_window():
    layout = [[sg.Text("Bewerte folgende Aussagen...", size=(101,1)), sg.Text("Stimme gar nicht zu", size=(23,1)), sg.Text("Stimme zu")],
        [sg.Text('_'  * 100)],
        [sg.Text("Ich glaube, dass ich das interaktive System regelmäßig nutzen werde", size=(105,1)), sg.Radio(text="", group_id=1, default=False, size=(2,1), key=15, enable_events=True), sg.Radio(text="", group_id=1, default=False, size=(2,1), key=14, enable_events=True), sg.Radio(text="", group_id=1, default=True, size=(2,1), key=13, enable_events=True), sg.Radio(text="", group_id=1, default=False, size=(2,1), key=12, enable_events=True), sg.Radio(text="", group_id=1, default=False, size=(2,1), key=11, enable_events=True)],  
        [sg.Text("Ich finde das interaktive System ziemlich komplex", size=(105,1)), sg.Radio(text="", group_id=2, default=False, size=(2,1), key=25, enable_events=True), sg.Radio(text="", group_id=2, default=False, size=(2,1), key=24, enable_events=True), sg.Radio(text="", group_id=2, default=True, size=(2,1), key=23, enable_events=True), sg.Radio(text="", group_id=2, default=False, size=(2,1), key=22, enable_events=True), sg.Radio(text="", group_id=2, default=False, size=(2,1), key=21, enable_events=True)],
        [sg.Text("Ich empfinde das interaktive System als einfach zu nutzen", size=(105,1)), sg.Radio(text="", group_id=3, default=False, size=(2,1), key=35, enable_events=True), sg.Radio(text="", group_id=3, default=False, size=(2,1), key=34, enable_events=True), sg.Radio(text="", group_id=3, default=True, size=(2,1), key=33, enable_events=True), sg.Radio(text="", group_id=3, default=False, size=(2,1), key=32, enable_events=True), sg.Radio(text="", group_id=3, default=False, size=(2,1), key=31, enable_events=True)],
        [sg.Text("Ich denke, dass ich eine technische Unterstützung beim Bedienen dieses interaktiven Systems brauchen könnte", size=(105,1)), sg.Radio(text="", group_id=4, default=True, size=(2,1), key=45, enable_events=True), sg.Radio(text="", group_id=4, default=False, size=(2,1), key=44, enable_events=True), sg.Radio(text="", group_id=4, default=True, size=(2,1), key=43, enable_events=True), sg.Radio(text="", group_id=4, default=False, size=(2,1), key=42, enable_events=True), sg.Radio(text="", group_id=4, default=False, size=(2,1), key=41, enable_events=True)],
        [sg.Text("Ich finde, dass viele Funktionen sehr gut in diesem interaktiven System integriert sind", size=(105,1)), sg.Radio(text="", group_id=5, default=False, size=(2,1), key=55, enable_events=True), sg.Radio(text="", group_id=5, default=False, size=(2,1), key=54, enable_events=True), sg.Radio(text="", group_id=5, default=True, size=(2,1), key=53, enable_events=True), sg.Radio(text="", group_id=5, default=False, size=(2,1), key=52, enable_events=True), sg.Radio(text="", group_id=5, default=False, size=(2,1), key=51, enable_events=True)],
        [sg.Text("Ich glaube, dass das interaktive System viele Unstimmigkeiten hat", size=(105,1)), sg.Radio(text="", group_id=6, default=False, size=(2,1), key=65, enable_events=True,), sg.Radio(text="", group_id=6, default=False, size=(2,1), key=64, enable_events=True), sg.Radio(text="", group_id=6, default=True, size=(2,1), key=63, enable_events=True), sg.Radio(text="", group_id=6, default=False, size=(2,1), key=62, enable_events=True), sg.Radio(text="", group_id=6, default=False, size=(2,1), key=61, enable_events=True)],
        [sg.Text("Ich kann mir vorstellen, dass viele Anwender/innen dieses interaktive System schnell erlernen", size=(105,1)), sg.Radio(text="", group_id=7, default=False, size=(2,1), key=75, enable_events=True), sg.Radio(text="", group_id=7, default=False, size=(2,1), key=74, enable_events=True), sg.Radio(text="", group_id=7, default=True, size=(2,1), key=73, enable_events=True), sg.Radio(text="", group_id=7, default=False, size=(2,1), key=72, enable_events=True), sg.Radio(text="", group_id=7, default=False, size=(2,1), key=71, enable_events=True)],
        [sg.Text("Ich finde das interaktive System recht mühsam in der Nutzung", size=(105,1)), sg.Radio(text="", group_id=8, default=False, size=(2,1), key=85, enable_events=True), sg.Radio(text="", group_id=8, default=False, size=(2,1), key=84, enable_events=True), sg.Radio(text="", group_id=8, default=True, size=(2,1), key=83, enable_events=True), sg.Radio(text="", group_id=8, default=False, size=(2,1), key=82, enable_events=True), sg.Radio(text="", group_id=8, default=False, size=(2,1), key=81, enable_events=True)],
        [sg.Text("Ich habe mich bei der Nutzung des interaktiven Systems sehr sicher gefühlt", size=(105,1)), sg.Radio(text="", group_id=9, default=False, size=(2,1), key=95, enable_events=True), sg.Radio(text="", group_id=9, default=False, size=(2,1), key=94, enable_events=True), sg.Radio(text="", group_id=9, default=True, size=(2,1), key=93, enable_events=True), sg.Radio(text="", group_id=9, default=False, size=(2,1), key=92, enable_events=True), sg.Radio(text="", group_id=9, default=False, size=(2,1), key=91, enable_events=True)],
        [sg.Text("Ich muss noch viel erlernen, bevor ich das interaktive System nutzen kann", size=(105,1)), sg.Radio(text="", group_id=10, default=False, size=(2,1), key=105, enable_events=True), sg.Radio(text="", group_id=10, default=False, size=(2,1), key=104, enable_events=True), sg.Radio(text="", group_id=10, default=True, size=(2,1), key=103, enable_events=True), sg.Radio(text="", group_id=10, default=False, size=(2,1), key=102, enable_events=True), sg.Radio(text="", group_id=10, default=False, size=(2,1), key=101, enable_events=True)],
        [sg.Text('_'  * 80)],
        [sg.Button("Abbrechen", key="Exit", button_color=("white", "grey")), sg.Button("OK", key="OK", button_color=("white", "grey"))]]
    window = sg.Window("Bewertung", layout, modal=True, return_keyboard_events=True, finalize=True)
    
    while True:
        event, values = window.read()

        if event == chr(13) or event == "OK":
            maptoexcel(values)
            break
        if event == "Exit" or event == sg.WIN_CLOSED:
            break 

    window.close()
    return window
