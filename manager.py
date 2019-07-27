import json
import heroku3

class Manager():
    __settings = {}
    __data = {}
    __heroku = None
    __apps = None

    def __init__(self, settings):
        self.__settings = settings
        pass

    def readConfig(self):
        with open(self.__settings['CONFIG_FILE'], 'r') as f:
            self.__data = json.loads(f.read())

    def accountsNames(self):
        return list(self.__data.keys())

    def authenticate(self, accountName):
        self.__heroku = heroku3.from_key(self.__data[accountName]['API_KEY'])
        self.__apps = self.__heroku.apps(order_by='name', sort='asc')

    def getAppsNames(self):
        names = []
        for app in self.__apps:
            names.append(app.name)
        return names

    def appStart(self, appName):
        for app in self.__apps:
            if app.name == appName:
                for proc in app.process_formation():
                    # app.process_formation()[proc.type].scale(1)
                    proc.scale(1)

    def appStop(self, appName):
        for app in self.__apps:
            if app.name == appName:
                # for dyno in app.dynos():
                #     dyno.kill()
                
                proclist = app.process_formation()
                for proc in proclist:
                    proc.scale(0)

    def appRestart(self, appName):
        for app in self.__apps:
            if app.name == appName:
                app.restart()

    def enableMaintenanceMode(self, appName):
        for app in self.__apps:
            if app.name == appName:
                app.enable_maintenance_mode()

    def disableMaintenanceMode(self, appName):
        for app in self.__apps:
            if app.name == appName:
                app.disable_maintenance_mode()

    def test(self, appName):
        for app in self.__apps:
            if app.name == appName:
                dynos = app.dynos()
                print(app.dynos())

                for dyno in app.dynos():
                    print(dyno)
                    print(dyno.command)
                    dyno.restart()

                proclist = app.process_formation()
                print(proclist)
                for proc in proclist:
                    print(proc.type)
                    print(proc.names)
                    print(proc)
