import PySimpleGUI as sg

wlcm_text = '''
                This tool attempts to recover text from a corrupt Ms-Word file. '''
instruction_text = '''
                    HOW TO:

                    1. Click on the "find file" button below.
                    2. Once you point out the file let xtractor do its magic.
                    '''

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout_column = [  [sg.Text('welcome to xtractor', justification='center')],
            [sg.Text(wlcm_text)],
            [sg.Text(instruction_text)],
            [sg.I(), sg.FileBrowse('Select File', auto_size_button=True)],
            [sg.Ok("Attempt Recovery")] ]

layout = [[sg.Column(layout_column, element_justification='center')]]

# Create the Window
window = sg.Window('Xtractor: welcome', layout, size=(460,250))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        print('You caused ', values, event)
        break
    elif event=='Attempt Recovery':
        print('You entered ', values, event)

window.close()