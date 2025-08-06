from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class EdadApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)

        layout = FloatLayout()

        fondo = Image(source='fondo.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(fondo)

        self.entrada = TextInput(
            hint_text="Año de nacimiento",
            size_hint=(0.6, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            multiline=False,
            input_filter='int'
        )
        layout.add_widget(self.entrada)

        boton = Button(
            text="Calcular edad",
            size_hint=(0.4, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.55}
        )
        boton.bind(on_press=self.calcular_edad)
        layout.add_widget(boton)

        self.resultado = Label(
            text="",
            font_size=24,
            color=(1, 1, 1, 1),
            size_hint=(1, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.35}
        )
        layout.add_widget(self.resultado)

        return layout

    def calcular_edad(self, instance):
        try:
            anio = int(self.entrada.text)
            edad = 2025 - anio
            self.resultado.text = f"Tienes {edad} años"
        except:
            self.resultado.text = "Ingresa un año válido"

if __name__ == '__main__':
    EdadApp().run()
