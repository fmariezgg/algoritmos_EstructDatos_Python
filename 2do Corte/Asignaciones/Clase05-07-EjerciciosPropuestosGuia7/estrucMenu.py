import os

class MenuOption:
    def __init__(self, key, description, action):
        self.key = key
        self.description = description
        self.action = action  # una función que se ejecuta

class Menu:
    def __init__(self, title, options, exit_key="5", clear_screen=True):
        self.title = title
        self.options = {opt.key: opt for opt in options}
        self.exit_key = exit_key
        self.clear_screen = clear_screen

    def show(self):
        while True:
            if self.clear_screen:
                print("\033c", end="")  # limpia la pantalla (en consola Unix/macOS; en Windows usar os.system('cls'))

            print(f"==== {self.title} ====\n")
            for key, opt in self.options.items():
                print(f"{key}. {opt.description}")
            print(f"{self.exit_key}. Salir")

            choice = input("\nSelecciona una opción: ").strip()

            if choice == self.exit_key:
                print("Saliendo del programa...")
                break
            elif choice in self.options:
                try:
                    self.options[choice].action()
                except Exception as e:
                    print(f"Error ejecutando opción: {e}")
            else:
                print("Opción inválida. Intenta de nuevo.")