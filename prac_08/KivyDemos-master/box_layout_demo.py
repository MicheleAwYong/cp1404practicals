from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        if random.randint(1, 10) <= 5:
            self.root.ids.my_label.text = "ouch!!"
        else:
            self.root.ids.my_label.text = "stop that!!"

    def handle_greet(self, instance):
        print('greet')

BoxLayoutDemo().run()
