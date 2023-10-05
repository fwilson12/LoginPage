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
            self.ids.invalid_credentials.color = 'red'

    def register(self):
        self.manager.current = 'register'


class RegisterScreen(Screen):
    def register(self, newuser, newpass, newpass2):
        newuser = str(newuser)
        newpass = str(newpass)
        newpass2 = str(newpass2)
        lowers = 'abcdefghijklmnopqrstuvwxyz'
        uppers = 'ABCDEFGHIJKLMNOPQRSTUV'
        nums = '123456789'
        spec = '!@#$%^&*()~_+-='
        lower_check = False
        upper_check = False
        num_check = False
        special_check = False
        for letter in newpass:
            if letter in lowers:
                lower_check = True
        for letter in newpass:
            if letter in uppers:
                upper_check = True
        for letter in newpass:
            if letter in nums:
                num_check = True
        for letter in newpass:
            if letter in spec:
                special_check = True
        print(newpass+ newpass2)
        if newuser in users.keys():
            self.ids.problem.text = 'that username is already in use'
        elif newpass != newpass2:
            self.ids.problem.text = 'new passwords must match'
        elif len(newpass) < 8:
            self.ids.problem.text = 'password must be at least 8 characters'
        elif not lower_check:
            self.ids.problem.text = 'password must contain a lowercase character'
        elif not upper_check:
            self.ids.problem.text = 'password must contain an uppercase character'
        elif not num_check:
            self.ids.problem.text = 'password must contain a number'
        elif not special_check:
            self.ids.problem.text = 'password must contain a special character'
        if num_check == True and lower_check == True and upper_check == True and special_check == True and len(
                newpass) >= 8 and newpass == newpass2:
            self.ids.problem.color = 'green'
            self.ids.problem.text = 'account successfully created'
            users[newuser] = newpass
            print(users)

    def gologin(self):
        self.manager.current = 'login'


class LogoutScreen(Screen):
    def logout(self):
        self.manager.current = 'login'


users = {}
LoginPage2App().run()
