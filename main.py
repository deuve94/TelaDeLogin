from typing import Any, List
import flet as ft

class Campo(ft.UserControl):
    def __init__(self, largura, altura, texto, icone, senha=False):
        super().__init__()
        self.body = ft.Container(
            ft.Row([
                ft.TextField(
                    hint_text= texto,
                    border= ft.InputBorder.NONE,
                    color= 'white',
                    hint_style= ft.TextStyle(color='white'),
                    height=altura,
                    width=largura/5*4,
                    bgcolor='transparent',
                    text_style=ft.TextStyle(size=18, weight='w400'),
                    password=senha),
                    ft.Icon(icone, color='white')          
            ]),
            border=ft.border.all(1, '#44f4f4f4'),
            border_radius=18,
            bgcolor='transparent',
            alignment=ft.alignment.center,
            width=largura
        )
    
    def build(self):
        return self.body
    

body = ft.Stack(
    [ft.Image(
        src='assets/background.jpg'
    ),
    ft.Container(
        alignment=ft.alignment.center,
        content=ft.Container(
            ft.Column([
                ft.Row([ft.Text("AikaSystems", color='white', weight='w700', size=32, text_align='center')], alignment= ft.MainAxisAlignment.CENTER),
                ft.Row([Campo(largura=320, altura=50, texto="Usuário", icone=ft.icons.PERSON_ROUNDED)], alignment= ft.MainAxisAlignment.CENTER),
                ft.Row([Campo(largura=320, altura=50, texto="Senha", icone=ft.icons.LOCK_ROUNDED, senha=True)], alignment= ft.MainAxisAlignment.CENTER),
                ft.Row([ft.Row([ft.Checkbox(value=False), ft.Text("Lembrar usuário", color='white', size=14)]), ft.Text("Esqueceu a senha?", color='white', size=14)], alignment= ft.MainAxisAlignment.SPACE_AROUND),
                ft.Row([ft.ElevatedButton("ENTRAR", color='black', bgcolor='white', width=250, height=50)], alignment= ft.MainAxisAlignment.CENTER),
                ft.Row([ft.Text("Não tem uma conta?", color='white', size=14), ft.Text("Registre-se", weight='w500', color='white', size=14)], alignment= ft.MainAxisAlignment.CENTER, spacing=2),
                ft.Row(controls=[ft.Divider(height=2, color='transparent')]),
                ft.Row([ft.ElevatedButton("SAIR", color='black', bgcolor='white', width=160, height=30)], alignment= ft.MainAxisAlignment.CENTER),
            ], 
            alignment= ft.MainAxisAlignment.CENTER), 
            width=400, 
            height=400, 
            margin= ft.margin.only(top=150),
            border_radius=18,
            blur=ft.Blur(10,12,ft.BlurTileMode.MIRROR),
            border=ft.border.all(1, '#44f4f4f4'),
            bgcolor='#10f4f4f4',
            alignment=ft.alignment.center
        ) 
    )
    ])

def main(page: ft.Page):
    page.title = "Tela de Login"
    page.padding = 0
    page.window_resizable = False
    page.window_center()
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    
    page.add(
        body
    )
    
ft.app(target=main)
