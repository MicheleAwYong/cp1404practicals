import random
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 500)


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack"]

    def build(self):
        self.title = "Dynamic Labels Demo"
        self.root = Builder.load_file('dynamic_labels.kv')

        for name in self.name_list:
            temp_label = Label(
                text=name,
                size_hint_y=None,
                height=40,
                color=(0, 0.4, 0.8, 1),
                font_size='18sp',
                bold=True
            )
            self.root.ids.main.add_widget(temp_label)

        return self.root


if __name__ == '__main__':
    DynamicLabelsApp().run()