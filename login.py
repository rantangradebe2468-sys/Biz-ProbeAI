# login.py

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

from auth import login, signup


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.title = Label(text="BizProbe AI Login", font_size=24)

        self.username = TextInput(hint_text="Username", multiline=False)
        self.password = TextInput(hint_text="Password", password=True, multiline=False)

        self.message = Label(text="")

        login_btn = Button(text="Login")
        signup_btn = Button(text="Sign Up")

        login_btn.bind(on_press=self.do_login)
        signup_btn.bind(on_press=self.do_signup)

        layout.add_widget(self.title)
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(login_btn)
        layout.add_widget(signup_btn)
        layout.add_widget(self.message)

        self.add_widget(layout)

    def do_login(self, instance):
        user = self.username.text
        pwd = self.password.text

        success, msg = login(user, pwd)

        self.message.text = msg

        if success:
            self.manager.current = "main"

    def do_signup(self, instance):
        user = self.username.text
        pwd = self.password.text

        success, msg = signup(user, pwd)

        self.message.text = msg