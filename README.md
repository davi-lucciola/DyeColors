# DyeColors
Module for work with colors in python terminal

## How to use
First, you need to create an "Dyes" object, for paint one or more strings

```python
from dyecolors import *


dyes1 = Dyes('text_color', 'background_color', 'style_type')
paint('Here are your text colorized!', 'you can use like a print', dyes=dyes1, sep=' - ')
paint('You can pass "sep" and "end" parameters too!', dyes=dyes1, end= ' - Final!')
```
