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
        self.background_normal = ""
        self.font_size = 25
        self.height = 50


class MainWidget(Widget):
    files_wrapper = ObjectProperty(None)
    files_list = ObjectProperty(None)

    def check_file_type(self, file):
        path = os.path.join(os.getcwd(), file)
        if os.path.isfile(path):
            return 'file'
        elif os.path.isdir(path):
            return 'dir'

    def draw_files(self, files, open_dir_callback, open_file_callback):
        self.files_list.clear_widgets()
        self.files_list.height = 0

        for file in files:
            file_type = self.check_file_type(file)
            fileblock = None
            if file_type == 'file':
                fileblock = FileBlock(text=file, background_color = (0.5, 0., 1., 1), on_press=open_file_callback)
            elif file_type == 'dir':
                fileblock = FileBlock(text=file, background_color=(0, 0.5, 0.5, 1), on_press=open_dir_callback)
                
            self.files_list.add_widget(fileblock)
            self.files_list.height += fileblock.height / 2 + 5


class FileManagerApp(App):
    current_path = os.getcwd()
    dirs = os.listdir()

    def open_dir(self, instance):
        path = os.path.join(self.current_path, instance.text)
        path = os.path.normpath(path)
        self.current_path = path
        os.chdir(self.current_path)
        self.dirs = os.listdir()

        self.update_files()
        
    def open_file(self, instance):
        pass

    def back_up(self):
        path = os.path.join(self.current_path, '..')
        path = os.path.normpath(path)
        self.current_path = path
        os.chdir(self.current_path)
        self.dirs = os.listdir()

        self.update_files()

    def update_app(self, *args):
        pass

    def update_files(self):
        self.mw.draw_files(self.dirs, self.open_dir, self.open_file)

    def build(self):
        self.mw = MainWidget()
        self.update_files()
        Clock.schedule_interval(self.update_app, 1)
        return self.mw


if __name__ == "__main__":
    FileManagerApp().run()
