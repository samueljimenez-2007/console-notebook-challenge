
from notebook import Notebook, Note


class Console:

    def __init__(self):
        self.notebook = Notebook()

    def menu(self):
        print("\n----- MENU -----")
        print("1. Agregar nota")
        print("2. Listar notas")
        print("3. Agregar etiqueta a nota")
        print("4. Listar notas importantes")
        print("5. Eliminar nota")
        print("6. Mostrar notas por etiqueta")
        print("7. Mostrar etiqueta con más notas")
        print("8. Salir")

    def run(self):

        while True:
            self.menu()
            option = input("Seleccione una opción: ")

            if option == "1":
                title = input("Título: ")
                text = input("Texto: ")
                importance = input("Importancia (HIGH, MEDIUM, LOW): ")

                code = self.notebook.add_note(title, text, importance)
                print("Nota creada con código:", code)

            elif option == "2":
                for note in self.notebook.notes:
                    print("\nCódigo:", note.code)
                    print(note)
                    print("Etiquetas:", note.tags)

            elif option == "3":
                code = int(input("Código de la nota: "))
                tag = input("Etiqueta: ")

                for note in self.notebook.notes:
                    if note.code == code:
                        note.add_tag(tag)
                        print("Etiqueta agregada.")

            elif option == "4":
                important = self.notebook.important_notes()

                for note in important:
                    print("\nCódigo:", note.code)
                    print(note)

            elif option == "5":
                code = int(input("Código a eliminar: "))
                self.notebook.delete_note(code)
                print("Nota eliminada.")

            elif option == "6":
                tag = input("Etiqueta: ")
                notes = self.notebook.notes_by_tag(tag)

                for note in notes:
                    print("\nCódigo:", note.code)
                    print(note)

            elif option == "7":
                tag = self.notebook.tag_with_most_notes()
                print("Etiqueta con más notas:", tag)

            elif option == "8":
                print("Saliendo...")
                break

            else:
                print("Opción inválida.")
