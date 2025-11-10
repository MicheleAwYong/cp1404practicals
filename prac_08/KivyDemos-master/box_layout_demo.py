from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        name = self.root.ids.name_input.text
        if name.strip():
            greeting = f"Hello, {name}!"
        else:
            greeting = "Hello there! Please enter your name."
            self.root.ids.my_label.text = greeting
            print(f"Greet button pressed. Displaying: {greeting}")

    def handle_greet(self, instance):
        print('greet')

BoxLayoutDemo().run()
