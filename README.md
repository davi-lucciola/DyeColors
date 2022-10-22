# DyeColors
Module for work with colors in python terminal

## How to use
First, you need to create an "Dyes" object, for paint one or more strings

**DOCSTRING**
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

```python
from dyecolors import *


dyes1 = Dyes('text_color', 'background_color', 'style_type')
paint('Here are your text colorized!', 'you can use like a print', dyes=dyes1, sep=' - ')
paint('You can pass "sep" and "end" parameters too!', dyes=dyes1, end= ' - Final!')
```
