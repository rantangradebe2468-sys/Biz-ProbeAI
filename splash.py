# splash.py

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock


class SplashScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.switched = False  # 🔒 prevent repeat switching

        layout = FloatLayout()

        # LOGO
        self.logo = Image(
            source="logo.png",
            size_hint=(1, 0.85),
            pos_hint={"center_x": 0.5, "top": 1},
            allow_stretch=True,
            keep_ratio=True
        )

        # TEXT
        self.label = Label(
            text="[b]BizProbe AI[/b]\n\nLoading.",
            markup=True,
            font_size=32,
            size_hint=(1, 0.2),
            pos_hint={"center_x": 0.5, "y": 0}
        )

        layout.add_widget(self.logo)
        layout.add_widget(self.label)

        self.add_widget(layout)

        # Animation
        Clock.schedule_interval(self.animate_dots, 0.5)

        # Delay
        Clock.schedule_once(self.switch_to_login, 7)

    def animate_dots(self, dt):
        text = self.label.text

        if "Loading..." in text:
            self.label.text = "[b]BizProbe AI[/b]\n\nLoading."
        elif "Loading.." in text:
            self.label.text = "[b]BizProbe AI[/b]\n\nLoading..."
        elif "Loading." in text:
            self.label.text = "[b]BizProbe AI[/b]\n\nLoading.."

    def switch_to_login(self, dt):
        if self.switched:
            return  # 🛑 STOP repeat switching

        self.switched = True
        self.manager.current = "login"