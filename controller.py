import manager
import window

class Controller():
    __manager = None
    __window = None

    def __init__(self):
        settings = {'CONFIG_FILE': 'config.json'}

        self.__manager = manager.Manager(settings)
        self.__window = window.Window(self.__manager)
        pass