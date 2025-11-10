from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        name = self.root.ids.input_name.text
        greeting = f"Hello {name}"
        self.root.ids.output_label.text = greeting
        print(f"Greet button pressed. Displaying: {greeting}")

    def handle_clear(self):
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = "Output cleared."
        print("Clear button pressed. Input and output cleared.")

if __name__ == '__main__':
    BoxLayoutDemo().run()
