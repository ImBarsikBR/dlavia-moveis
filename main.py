from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class ComissaoApp(BoxLayout):
    def calcular(self):
        try:
            valor = float(self.ids.entrada_valor.text)
            comissao = valor * 0.15
            self.ids.resultado.text = f"Comissão: R$ {comissao:.2f}"
        except ValueError:
            self.ids.resultado.text = "Digite um número válido!"

class MainApp(App):
    def build(self):
        print("Carregando interface...")
        self.title = "Calculadora de Comissão"
        return ComissaoApp()

if __name__ == '__main__':
    MainApp().run() 