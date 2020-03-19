import os
from kivy.properties import ObjectProperty

from kivy.uix.widget import Widget
from kivy.uix.button import Button

from kivy.clock import Clock

from kivy.app import App
import kivy
kivy.require('1.11.0')


class FileBlock(Button):
    def __init__(self, **kwargs):
        super(FileBlock, self).__init__(**kwargs)
        self.size_hint = (1., None)
        self.background_color = (0., 0., 1., 1)
        self.background_normal = ""
        self.font_size = 25
        self.height = 50


class MainWidget(Widget):
    files_wrapper = ObjectProperty(None)
    files_list = ObjectProperty(None)

    def draw_files(self, files):
        self.files_list.clear_widgets()
        self.files_list.height = 0
        
        for file in files:
            fileblock = FileBlock(text=file)
            self.files_list.add_widget(fileblock)
            self.files_list.height += fileblock.height / 2 + 5


class FileManagerApp(App):
    current_path = os.getcwd()
    dirs = os.listdir()

    def back_up(self):
        path = os.path.join(self.current_path, '..')
        path = os.path.normpath(path)
        self.current_path = path
        os.chdir(self.current_path)
        self.dirs = os.listdir()
        self.mw.draw_files(self.dirs)

    def update_app(self, *args):
        pass

    def build(self):
        print('dsdsd')
        self.mw = MainWidget()
        self.mw.draw_files(self.dirs)
        Clock.schedule_interval(self.update_app, 1)
        return self.mw


if __name__ == "__main__":
    FileManagerApp().run()
