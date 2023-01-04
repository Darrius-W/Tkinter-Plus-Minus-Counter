import plusMinusGUI as PMGUI

def increase_res():
    result = PMGUI.display_lbl['text']
    result = int(PMGUI.display_lbl['text']) + 1
    PMGUI.display_lbl['text'] = result
    
def decrease_res():
    result = PMGUI.display_lbl['text']
    result = int(PMGUI.display_lbl['text']) - 1
    PMGUI.display_lbl['text'] = result