from main_window import AppRunner, MainWindow

class FantasyWindow(MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__('Team Tau Fantasy Football')

if __name__ == '__main__':
    app = AppRunner(FantasyWindow)
    app.start()