from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("LoginPage.kv")
class QuizPageApp(App):
    def build(self):
        return QuizManager()

class ErrorScreen(Screen):
    def next_question(self):
        self.manager.current = 'question2'

class CorrectScreen(Screen):
    def next_question(self):
        self.manager.current = 'question2'

class QuizManager(ScreenManager):
    pass

class Question1Screen(Screen):
    def answer_question(self, bool):
        if bool:
            self.manager.current = 'correct'
        else:
            self.manager.current = 'wrong'
class Question2Screen(Screen):
    def answer_question(self, bool):
        if bool:
            self.manager.current = 'correct'
        else:
            self.manager.current = 'wrong'




QuizPageApp().run()