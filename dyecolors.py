'''
A module for work with colors in terminal!

First, you need to instance an "Dyes" object and use that object on the functions

-> Colors (Font and Background):

- red
- green
- yellow
- blue
- magenta
- cyan
- white

-> Font Styles:

- bold
- underline
- negative
'''
from dyes import Dyes

# Default Values
global normalize_style
normalize_style = '\033[m'

colors_cods = {
    'red': 1,
    'green': 2,
    'yellow': 3,
    'blue': 4,
    'magenta': 5,
    'cyan': 6,
    'white': 7
}

style_cods = {
    'bold': 1,
    'underline': 4,
    'negative': 7
}

# Functions
def paint(*txts: str, dyes: Dyes, end: str = '\n', sep: str = ' ') -> None:
    '''
    This funciton is like a print, but with the colors (style)
    '''
    for index, text in enumerate(list(txts)):
        if index == len(txts)-1: print(colorize(text, dyes),  end=colorize(end, dyes))
        else: print(colorize(text, dyes), end=colorize(sep, dyes))
    
def colorize(txt: str, dyes: Dyes) -> str:
    '''
    This function colorize one string
    '''
    colorize_code = __colorize_cod(dyes.style, dyes.font_color, dyes.background_color)
    text_colorized = colorize_code + str(txt) + normalize_style
    return text_colorized

# Aux Functions
def __colorize_cod(style, font, background) -> str:
    # Defing the cods individualy
    style = __cod_style(style)
    font = __cod_font(font)
    background = __cod_background(background)

    # Making a cod string
    cods = list(filter(lambda element: element is not None, [style, font, background]))
    colorize_cod = '\033['
    for i, ansii_cod in enumerate(cods):
        if i != len(cods) - 1:
            colorize_cod += f'{ansii_cod};'
        else:
            colorize_cod += f'{ansii_cod}m'
    return colorize_cod

def __cod_font(color: str) -> str:
    'Type of code - ANSII'
    color = __is_none(color)
    if color is not None:
        cod = '3'
        cod += f'{colors_cods[color]}'  
    else:
        cod = None
    return cod

def __cod_background(color: str) -> str:
    'Type of code - ANSII'
    color = __is_none(color)
    if color is not None:
        cod = '4'
        cod += f'{colors_cods[color]}' 
    else:
        cod = None 
    return cod

def __cod_style(style: str) -> str:
    'Type of code - ANSII'
    style = __is_none(style)
    if style is not None:
        cod = f'{style_cods[style]}'
    else:
        cod = None 
    return cod

def __is_none(param: str) -> None:
    if param == '':
        param = None
    return param

if __name__ == '__main__':
    print('Documentation:', __doc__)
