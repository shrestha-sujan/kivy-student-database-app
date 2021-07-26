import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('your_api_json_file.json', scope)
client = gspread.authorize(creds)
iQue_sheet = client.open("InventoryBackend").get_worksheet(1)


Window.size = (500, 600)

#root layout
class InventoryWindow(Screen):
    pass

#Layout in question
class AddPartWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.np = []

    
    stu_name = ObjectProperty(None)
    serial_number = ObjectProperty(None)
    dob = ObjectProperty(None)

    
    def new_part(self):
        self.stu_name = self.ids.stu_name.text
        self.serial_number = self.ids.serial_number.text
        self.dob = self.ids.dob.text

        self.np = [self.stu_name, self.serial_number, self.dob]
        iQue_sheet.append_row(self.np)

        record_data = iQue_sheet.get_all_records()
        print(record_data)

class OnOrderWindow(Screen):
    pass

class OrderFormWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class DataApp(App):
    def build(self):
        #These are used to enable going back and forth between screens using buttons
        sm = ScreenManager()
        self.title='19TE422'
        sm.add_widget(InventoryWindow(name='inv_window'))
        sm.add_widget(OnOrderWindow(name='on_order_window'))
        sm.add_widget(AddPartWindow(name='add_part_window'))
        sm.add_widget(OrderFormWindow(name='order_form_window'))
        return sm
        

if __name__ == "__main__":
    DataApp().run()