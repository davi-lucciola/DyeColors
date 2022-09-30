'''
Main class of the module. 
Use with the functions for "paint" the text with the DYES!
'''

class Dyes:
    '''
    "Dyes" Class, is like an style of text
    '''
    colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')
    styles = ('bold', 'underline', 'negative')

    def __init__(self, color: str = '', background: str = '', style: str = '') -> None:
        '''
        The idea is create an styles objects for print strings with colors in terminal.

        Keywords arguments:
        color -- the color for define a color font
        backgroud -- the color for define a color background

        Colors (Font and Background):
        - red
        - green
        - yellow
        - blue
        - magenta
        - cyan
        - white

        Font Styles:
        - bold
        - underline
        - negative
        '''
        color, background, style = self.__initial_test(color, background, style)
        self.__font_color = color
        self.__backgroud_color = background
        self.__style = style
    
    def __initial_test(self, color: str, background: str, style: str) -> None:
        'An initial test for valid colors (background and text) and style'
        color = self.__color_test(color)
        background = self.__color_test(background)
        style = self.__style_test(style)

        if (color == background) and (color != '' and background != ''): 
            raise Exception("The background and font colors can't be the same")
        
        return color, background, style
        
    
    def __color_test(self, color: str) -> str:
        'Test if the color passed are valid'
        color = color.strip().lower()
        if color == '':
            pass
        elif (color not in self.colors): 
            raise Exception("That color not exist or is not supported")
        return color
    
    def __style_test(self, style: str) -> str:
        'Test if the style passed are valid'
        style = style.strip().lower()
        if style == '':
            pass
        elif (style not in self.styles):
            raise Exception("That style not exist or is not supported")
        return style

    def __repr__(self) -> str:
        representation = f'Font_Color: {self.font_color}'
        representation += f'\nBackground_Color: {self.background_color}'
        representation += f'\nFont_Style: {self.style}'
        return representation

    # Getters
    @property
    def font_color(self):
        return self.__font_color
    
    @property
    def background_color(self):
        return self.__backgroud_color
    
    @property
    def style(self):
        return self.__style

    # Setters
    @font_color.setter
    def font_color(self, color):
        self.__color_test(color)
        self.__font_color = color
    
    @background_color.setter
    def background_color(self, color):
        self.__color_test(color)
        self.__backgroud_color = color

    @style.setter
    def style(self, style):
        self.__style_test(style)
        self.__style = style

if __name__ == '__main__':
    print(__doc__)
