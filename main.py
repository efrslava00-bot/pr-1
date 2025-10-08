import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen # Импортируем ScreenManager и Screen
from kivy.properties import ObjectProperty

# --- Первый экран: Главное меню ---
class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'main_menu' # Уникальное имя для этого экрана

        main_layout = BoxLayout(orientation='vertical')

        # Кнопка 1, которая будет переключать на следующий экран
        button1 = Button(text='Кнопка 1 (Перейти на следующий экран)')
        button1.bind(on_press=self.go_to_next_screen) # Привязываем действие к кнопке
        main_layout.add_widget(button1)

        # Остальные кнопки
        button2 = Button(text='Кнопка 2')
        button3 = Button(text='Кнопка 3')
        main_layout.add_widget(button2)
        main_layout.add_widget(button3)

        self.add_widget(main_layout) # Добавляем наш BoxLayout в Screen

    def go_to_next_screen(self, instance):
        # self.manager ссылается на ScreenManager, в котором находится этот экран
        # current устанавливает, какой экран сейчас активен по его имени
        self.manager.current = 'second_screen'
        print("Переход на второй экран")

# --- Второй экран: Подменю с двумя новыми кнопками ---
class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'second_screen' # Уникальное имя для этого экрана

        second_layout = BoxLayout(orientation='vertical')

        # Две новые кнопки
        new_button1 = Button(text='Новая Кнопка A')
        new_button2 = Button(text='Новая Кнопка B')
        second_layout.add_widget(new_button1)
        second_layout.add_widget(new_button2)

        # Кнопка для возврата на главный экран
        back_button = Button(text='Вернуться в главное меню')
        back_button.bind(on_press=self.go_back_to_main_menu)
        second_layout.add_widget(back_button)

        self.add_widget(second_layout) # Добавляем наш BoxLayout в Screen

    def go_back_to_main_menu(self, instance):
        self.manager.current = 'main_menu'
        print("Возврат на главный экран")


# --- Главное Kivy приложение ---
class SimpleApp(App):
    def build(self):
        # Создаем ScreenManager
        sm = ScreenManager()

        # Добавляем наши экраны в ScreenManager
        sm.add_widget(MainMenuScreen())
        sm.add_widget(SecondScreen())

        # Устанавливаем начальный экран
        sm.current = 'main_menu' # Показываем MainMenuScreen при старте

        return sm # Возвращаем ScreenManager в качестве корневого виджета

if __name__ == '__main__':
    SimpleApp().run()
