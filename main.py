import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from datetime import datetime
from kivy.core.window import Window
import os

# Descargar imagen de fondo
imagen_url = "https://i.pinimg.com/736x/36/5a/71/365a718faf40b8c2dea0f7d8afbb67b9.jpg"
imagen_local = "fondo.jpg"
if not os.path.exists(imagen_local):
    r = requests.get(imagen_url)
    with open(imagen_local, "wb") as f:
        f.write(r.content)

class EdadApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)

        root = BoxLayout(orientation='vertical')

        self.background = Image(source=imagen_local, allow_stretch=True, keep_ratio=False)
        root.add_widget(self.background)

        overlay = BoxLayout(orientation='vertical', padding=50, spacing=20, size_hint=(1, None))
        overlay.size = (Window.width, Window.height)
        overlay.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        self.input = TextInput(hint_text='Ingresa fecha nacimiento (dd/mm/aaaa)', multiline=False, size_hint=(1, None), height=40)
        self.result_label = Label(text='', size_hint=(1, None), height=40, color=(1,1,1,1))

        btn = Button(text='Calcular Edad', size_hint=(1, None), height=40)
        btn.bind(on_press=self.calcular_edad)

        overlay.add_widget(self.input)
        overlay.add_widget(btn)
        overlay.add_widget(self.result_label)

        root.add_widget(overlay)
        return root

    def calcular_edad(self, instance):
        try:
            fecha_nac = datetime.strptime(self.input.text, "%d/%m/%Y")
            hoy = datetime.today()
            edad = hoy.year - fecha_nac.year
            if (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day):
                edad -= 1
            self.result_label.text = f"Tienes {edad} años."
        except ValueError:
            self.result_label.text = "Fecha inválida. Usa dd/mm/aaaa."

if __name__ == '__main__':
    EdadApp().run()
