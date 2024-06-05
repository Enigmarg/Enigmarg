from engine import Engine
from interfaces.login import Login
from util import DATABASE, USER


if __name__ == "__main__":
    DATABASE.connect()
    login_screen = Login(DATABASE)
    login_screen.create_login_screen()
    if login_screen.logged_in:
        USER.set_id(login_screen.player_id)
        gameEngine = Engine()
        gameEngine.run()
