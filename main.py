from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("LoginPage.kv")
Builder.load_file("LoginPage2.kv")

# class QuizPageApp(App):
#     def build(self):
#         return QuizManager()
#
# class ErrorScreen(Screen):
#     def next_question(self):
#         self.manager.current = 'question2'
#
# class CorrectScreen(Screen):
#     def next_question(self):
#         self.manager.current = 'question2'
#
# class QuizManager(ScreenManager):
#     pass
#
# class Question1Screen(Screen):
#     def answer_question(self, bool):
#         if bool:
#             self.manager.current = 'correct'
#         else:
#             self.manager.current = 'wrong'
# class Question2Screen(Screen):
#     def answer_question(self, text):
#         if text.lower() == 'curve':
#             self.manager.current = 'correct'
#         else:
#             self.ids.invalid_guess.text = 'did you get a lobotomy?'
#             self.ids.invalid_guess.color = 'green'
#
#
#
#
#
# QuizPageApp().run()


class LoginPage2App(App):
    def build(self):
        return LoginManager()


class LoginManager(ScreenManager):
    pass

class LoginScreen(Screen):
    def login(self, user, password):
        if user in users.keys() and password in users.values():
            self.manager.current = 'logout'
        else:
            self.ids.invalid_credentials.text = 'register a new account'
            self.ids.invalid_credentials.color = 'blue'


class RegisterScreen(Screen):
    pass

class LogoutScreen(Screen):
    def logout(self):
        self.manager.current = 'login'

users = {'krazyman50': 'geometryDasher87!', 'belugawhale': 'OceanCreature87%'}
LoginPage2App().run()