from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.config import Config

# Параметра окна
Config.set("graphics", "resizable", False)
Config.set("graphics", "width", "270")
Config.set("graphics", "height", "290")


class GameApp(App):
    def __init__(self):
        super().__init__()
        self.switch = True
    
    def game(self, f):
        f.disabled = True
        f.text = 'O' if self.switch else 'X'
        self.switch = not self.switch
        winner = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
        vector = lambda i: [self.buttons[x].text for x in i]
        color = '#00FF7F' #цвет выделенных кнопок после победы
        for i in winner:#пробег по списку победных сочетаний 
            if vector(i).count('X') == 3 or vector(i).count('O') == 3:
                win = True
                for i in i:
                    self.buttons[i].color = color
                for btn in self.buttons:
                    btn.disabled = True
                break

    def restart(self,f): 
        self.switch = True
        for btn in self.buttons:
            btn.color = '#ffff00'
            btn.text = ""
            btn.disabled = False

#Создание кнопок
    def build(self):
        self.title = "Крестики-нолики"
        bl = BoxLayout(orientation="vertical", padding=3,spacing = 2)
        gl = GridLayout(cols=3, padding=2,spacing = 2)
        self.buttons = []
        for i in range(9):
            btn = Button(color = '#00FA9A',font_size = 25,disabled = False,on_press = self.game)  #событие клика по кнопке(вызов метода game)
            self.buttons.append(btn) #добавляем кнопки для игры
            gl.add_widget(btn) #кнопки отправляем в GridLayout 

        bl.add_widget(gl)
        bl.add_widget(Button(text = "Начать заново",color = '#00FA9A',size_hint = [1,.1], on_press = self.restart))
        return bl

#Запуск программы
if __name__ == "__main__":
    GameApp().run()
