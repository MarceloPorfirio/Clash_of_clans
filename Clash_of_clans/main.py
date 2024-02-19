import flet as ft

def main(page:ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_width = 500
    page.bgcolor = ft.colors.BLACK
    
    image = ft.Container(
        expand=2,
        border=ft.border_radius.vertical(top=20),
        clip_behavior=ft.ClipBehavior.NONE,
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_left,
            end=ft.alignment.top_right,
            colors=[ft.colors.BROWN,ft.colors.BLACK87],
        ),
        content=ft.Image(
            src='../assets/Barbarian-xx.png',
            scale=(1.6)
        )
    )
    info = ft.Container(
        expand=2,
        padding=ft.padding.all(30),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value='LEVEL 4',color=ft.colors.ORANGE),
                ft.Text(
                    value='Bárbaro',
                    weight=ft.FontWeight.BOLD,
                    size=40,
                    color=ft.colors.BLACK,
                ),
                ft.Text(
                    value='O bárbaro é um guerreiro escocês vestido de kilt com uma expressão raivosa e pronta para a batalha,faminto por destruição. Ele tem bigode de ferradura amarelo assassino.',
                    color=ft.colors.GREY,
                    text_align=ft.TextAlign.CENTER,
                )
            ]
        )
    )
    skills = ft.Container(
        expand=1,
        bgcolor=ft.colors.ORANGE,
        padding=ft.padding.symmetric(horizontal=20),
        border_radius=ft.border_radius.vertical(bottom=20),
        content=ft.Row(
            controls=[
                ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value='20',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=30
                        ),
                        ft.Text(
                            value='DEFESA',
                            color=ft.colors.WHITE
                        )
                    ]
                ),
                 ft.VerticalDivider(opacity=0.5),
                 ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value='16',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=30
                        ),
                        ft.Text(
                            value='VELOCIDADE',
                            color=ft.colors.WHITE
                        )
                    ]
                ),
                  ft.VerticalDivider(opacity=0.5),
                  ft.Column(
                    expand=1,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value='150',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=30
                        ),
                        ft.Text(
                            value='DANO',
                            color=ft.colors.WHITE
                        )
                    ]
                ),
            ]
        )
    )
    
    layout = ft.Container(
        height=650,
        width=400,
        shadow=ft.BoxShadow(blur_radius=100,color=ft.colors.BROWN),
        clip_behavior=ft.ClipBehavior.NONE,
        border_radius=ft.border_radius.all(30),
        bgcolor=ft.colors.WHITE,
        content=ft.Column(
            spacing=0,
            controls=[
                image,
                info,
                skills
            ]
            
        )
    )
    
    page.add(layout)
    
if __name__ == '__main__':
    ft.app(target=main,assets_dir='assets')