from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime


Builder.load_file('design.kv')


class LoginScreen(Screen):
    def signUp(self):
        self.manager.current = "signupScreen"
    
    def login(self, username, password):
        with open("users.json", 'r') as readFile:
            users = json.load(readFile)
        
        if username not in users and users[username]['password'] != password:
            print("Invalid username and/or password")
        else:
            self.manager.current = "loginScreenSuccess"


class SignupScreen(Screen):
    def addUser(self, username, password):
        with open("users.json", 'r') as readFile:
            users = json.load(readFile)

        # check if username exists
        if username in users:
            print(f"{username} taken. Please choose a new username")
            return
        
        # add the user
        users[username] = {
            'username': username,
            'password': password,
            'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S.%f")
        }

        # update the directory
        with open("users.json", 'w') as writeFile:
            json.dump(users, writeFile)
        
        self.manager.current = "signupScreenSuccess"


class SignupScreenSuccess(Screen):
    def returnToLogin(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "loginScreen"
        self.manager.transition.direction = 'left'  # use left as default


class LoginScreenSuccess(Screen):
    def logout(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "loginScreen"
        self.manager.transition.direction = 'left'



class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()