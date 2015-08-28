from mechanics import UI
from mechanics import StoryStructure as SS
import random

#random.seed(7)
s = SS.StoryStructure('data/test.txt')
ui = UI.UI(s)
ui.run()
