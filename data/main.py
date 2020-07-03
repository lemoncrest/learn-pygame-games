from data import setup,tools
from data.states import main_menu,load_screen,first_level
import profile

"""
Add states to control here.
"""
def main():
    run = tools.Control(setup.ORIGINAL_CAPTION)
    state_dict = {
        "MAIN_MENU": main_menu.Menu(),
        "LOAD_SCREEN": load_screen.Load_Screen(),
        "FIRST_LEVEL": first_level.First_Level()
    }
    run.setup_states(state_dict,"MAIN_MENU")
    run.main()
