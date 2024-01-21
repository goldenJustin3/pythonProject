from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen



class Scr_1(Screen):
    def __init__(self, name="ПЕрвый"):
        super().__init__(name=name)
        Box = BoxLayout(orientation="vertical", padding=10)
        lbr = Label(text = "Пожалуйста не переходите на слудующий слайд пока не прочитаеете что тут написона, а теперь переходите", color = (1, 0, 0, 1))
        btn = Button(text = "переход на 2",  on_press = self.next)
        Box.add_widget(lbr)
        Box.add_widget(btn)
        self.add_widget(Box)
    def next(self):
        self.manager.transition.direction = "up"
        self.manager.current = "второй!"

class Scr_2(Screen):
    def __init__(self, name="второй!"):
        super().__init__(name=name)
        lbr = Label(text = "ну тут вы сразу можете переходить вперёд", color = (0, 1, 0, 1))
        btn = Button(text = "переход на 3")
        btn.on_press = self.next
        self.add_widget(btn)
    def next(self):
        self.manager.transition.direction = "left"
        self.manager.current = "ну хотя бы третий"

class Scr_3(Screen):
    def __init__(self, name="ну хотя бы третий"):
        super().__init__(name=name)
        lbr = Label(text = "Тут остановитесь! и ПОТАНЦУЙТЕ!", color = (0, 0, 1, 1))
        btn = Button(text = "переход на 4")
        btn.on_press = self.next
        self.add_widget(btn)
    def next(self):
        self.manager.current = "аааааа было так блиско к трём"

class Scr_4(Screen):
    def __init__(self, name="аааааа было так блиско к трём"):
        super().__init__(name=name)
        lbr = Label(text = "Как прошёл ваш день? Какие у вас увличения? Знаете вы можете остаться тут и не идти дальше вас не кто не принуждает", color = (1, 1, 0, 1))
        btn = Button(text = "переход на 5")
        btn.on_press = self.next
        self.add_widget(btn)
    def next(self):
        self.manager.current = "хорошая пятёрка"

class Scr_5(Screen):
    def __init__(self, name="хорошая пятёрка"):
        super().__init__(name=name)
        lbr = Label(text = "Хорошо вы здесь но НЕ!! В КОЕ СЛУЧАЕ НЕ НАЖИМАЙТЕ КНОПКУ Я СЕРЬЁЗНО!!! НА НЕЙ БОМБА!!!, ВИРУС!!!, МЕЛОДИЯ СМЕРТИ!!!", color = (0, 1, 1, 1))
        btn = Button(text = "я ВЕСЁЛАЯ кнопка не нажимай меня пожалуйста или будет ВЕСЕЛЬЕ!.")
        btn.on_press = self.funny
        self.add_widget(btn)
    def funny(self):
        self.manager.current = "ПЕрвый"
        self.Laber(text = "Ну и что ты наделал? Рад этому? теперь начинай заново.", color = (1, 0, 0, 1))
class MyApp(App):#Главное
    def Aper(self):
        sm = ScreenManager()
        sm.add_widget(Scr_1())
        sm.add_widget(Scr_2())
        sm.add_widget(Scr_3())
        sm.add_widget(Scr_4())
        sm.add_widget(Scr_5())
        return sm

app = MyApp()
app.run()
