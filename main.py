# main.py

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle

from splash import SplashScreen
from login import LoginScreen
from api import get_prediction, get_top_opportunities
from monetization import upgrade_to_premium


# ---------------- CARD ---------------- #
class Card(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0.12, 0.12, 0.12, 1)
            self.rect = RoundedRectangle(radius=[20])
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


# ---------------- MAIN UI ---------------- #
class BizProbeUI(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=15, spacing=12)

        # HEADER
        header = BoxLayout(size_hint=(1, 0.18), spacing=10)

        logo = Image(source="logo.png", size_hint=(0.3, 1))

        title = Label(
            text="[b]BizProbe AI[/b]\nSmart Business Intelligence",
            markup=True,
            font_size=20
        )

        header.add_widget(logo)
        header.add_widget(title)
        self.add_widget(header)

        # INPUT
        input_card = Card(size_hint=(1, 0.18), padding=10)

        self.input = TextInput(
            hint_text="Enter idea (e.g. food in Cape Town)",
            multiline=False
        )

        input_card.add_widget(self.input)
        self.add_widget(input_card)

        # BUTTONS
        btn_layout = BoxLayout(size_hint=(1, 0.2), spacing=10)

        analyze_btn = Button(
            text="Analyze",
            background_normal="",
            background_color=(0.2, 0.6, 1, 1)
        )
        analyze_btn.bind(on_press=self.predict)

        top_btn = Button(
            text="Top 5 🔒",
            background_normal="",
            background_color=(0.1, 0.8, 0.4, 1)
        )
        top_btn.bind(on_press=self.show_top)

        btn_layout.add_widget(analyze_btn)
        btn_layout.add_widget(top_btn)
        self.add_widget(btn_layout)

        # UPGRADE
        upgrade_btn = Button(
            text="Upgrade to Premium 💰",
            size_hint=(1, 0.1),
            background_normal="",
            background_color=(1, 0.6, 0, 1)
        )
        upgrade_btn.bind(on_press=self.upgrade)
        self.add_widget(upgrade_btn)

        # RESULTS
        result_card = Card(padding=10)

        self.scroll = ScrollView()

        self.result = Label(
            text="Welcome to BizProbe AI 🚀",
            size_hint_y=None,
            markup=True,
            valign="top"
        )

        self.result.bind(texture_size=self.update_height)

        self.scroll.add_widget(self.result)
        result_card.add_widget(self.scroll)

        self.add_widget(result_card)

    def update_height(self, instance, value):
        self.result.height = self.result.texture_size[1]

    def detect_location(self, text):
        text = text.lower()

        if "johannesburg" in text:
            return "johannesburg"
        elif "durban" in text:
            return "durban"
        elif "township" in text:
            return "township"
        else:
            return "cape town"

    def predict(self, instance):
        data = get_prediction(self.input.text)

        ideas = "\n".join([f"• {i}" for i in data["ideas"]])

        self.result.text = f"""
[b]Type:[/b] {data['type']}
[b]Location:[/b] {data['location']}

[b]Score:[/b] {data['score']}%
[b]Status:[/b] {data['level']}

[b]Ideas:[/b]
{ideas}
"""

    def show_top(self, instance):
        location = self.detect_location(self.input.text)
        results = get_top_opportunities(location)

        if results == "LOCKED":
            self.result.text = "[b]🔒 Upgrade to Premium to unlock Top 5[/b]"
            return

        text = f"[b]Top 5 Businesses in {location.title()}[/b]\n\n"

        for i, item in enumerate(results, 1):
            ideas = ", ".join(item["ideas"])

            text += f"""
[b]{i}. {item['type'].title()}[/b]
Score: {item['score']}%
Ideas: {ideas}

"""

        self.result.text = text

    def upgrade(self, instance):
        upgrade_to_premium()
        self.result.text = "[b]🎉 Premium Activated![/b]"


# ---------------- SCREEN ---------------- #
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(BizProbeUI())


# ---------------- APP ---------------- #
class BizProbeApp(App):

    def build(self):
        sm = ScreenManager(transition=FadeTransition())

        splash = SplashScreen(name="splash")
        login = LoginScreen(name="login")
        main = MainScreen(name="main")

        sm.add_widget(splash)
        sm.add_widget(login)
        sm.add_widget(main)

        return sm


if __name__ == "__main__":
    BizProbeApp().run()