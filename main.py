import flet as ft


def main(page: ft.Page):
    # page.title = 'Calculadora IMC'
    # page.window.width = 400
    # page.window.height = 300
    # page.window.maximizable = False
    # page.window.minimizable = True
    # page.bgcolor = '#F6f6c3'
    # page.padding = 0
    # page.add(ft.Text('Teste', text_align=ft.TextAlign.RIGHT))
    # page.update()

    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)