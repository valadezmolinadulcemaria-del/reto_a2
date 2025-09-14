import flet as ft

def main(page: ft.Page):
    page.title = "Reto: Decisiones Interactivas"
    page.window_width = 420
    page.window_height = 720

    estado = {"actual": "inicio"}  # cambia con tus propios estados

    titulo = ft.Text("🌟preguntas faciles", size=22, weight="bold")
    texto  = ft.Text("", size=18)
    imagen = ft.Image(src="", width=280, height=180, fit=ft.ImageFit.CONTAIN, visible=False)

    btn_si   = ft.ElevatedButton("Sí")
    btn_no   = ft.ElevatedButton("No")
    btn_talvez   = ft.ElevatedButton("tal vez")
    btn_reset= ft.TextButton("Reiniciar", icon=ft.Icons.REFRESH)  # ✅ corregido
    botones  = ft.Row([btn_si, btn_no,btn_talvez], alignment=ft.MainAxisAlignment.CENTER, spacing=20)

    def mostrar_inicio():
        estado["actual"] = "inicio"
        page.bgcolor = None
        texto.value = "👀 ¿quiere contarme sobre tus cosas escolares?"
        imagen.visible = False
        btn_si.visible = True
        btn_no.visible = True
        btn_talvez.visible = True
        page.update()

    def a_pregunta2_si():
        estado["actual"] = "p2_si"
        texto.value = " te va bien las materias??"
        imagen.visible = False
        page.update()

    def a_pregunta3_si():
        estado["actual"] = "p3_si"
        texto.value = " crees q la carrera q escogiste te gusta??"
        imagen.visible = False
        page.update()

    def a_pregunta4_si():
        estado["actual"] = "p4_si"
        texto.value = "quiere que la escuela tenga mas hora libre?? "
        imagen.visible = False
        page.update()
        
    def a_pregunta5_si():
        estado["actual"] = "p5_si"
        texto.value = " bueno,te gusta las estalaciones de la escuela??"
        imagen.visible = False
        page.update()

    def a_pregunta6_si():
        estado["actual"] = "p6_si"
        texto.value = " te gusta la biblioteca de la escuela ??"
        imagen.visible = False
        page.update()

    def a_pregunta7_si():
        estado["actual"] = "p7_si"
        texto.value = " te gusta las computadoras de la escuela??"
        imagen.visible = False
        page.update()

    def a_pregunta8_si():
        estado["actual"] = "p8_si"
        texto.value = "te gusta la cafeteria??"
        imagen.visible = False
        page.update()

    def a_pregunta9_si():
        estado["actual"] = "p9_si"
        texto.value = " crees que necesita cambia las sillas de la escuela ??"
        imagen.visible = False
        page.update()

    def a_pregunta10_si():
        estado["actual"] = "p10_si"
        texto.value = "cree q pueda salir de la prepa??"
        imagen.visible = False
        page.update()


    def a_pregunta2_talvez():
        estado["actual"] = "p2_talvez"
        texto.value = "¿Por qué dudas sobre tus materias?"
        imagen.visible = False
        page.update()

    def a_pregunta3_talvez():
        estado["actual"] = "p3_talvez"
        texto.value = "¿Te gustaría cambiar de carrera?"
        imagen.visible = False
        page.update()

    def a_pregunta4_talvez():
        estado["actual"] = "p4_talvez"
        texto.value = "¿seguro?"
        imagen.visible = False
        page.update()

    def a_pregunta5_talvez():
        estado["actual"] = "p5_talvez"
        texto.value = "¿Por qué dudas sobre las instalaciones?"
        imagen.visible = False
        page.update()

    def a_pregunta6_talvez():
        estado["actual"] = "p6_talvez"
        texto.value = "¿Qué mejorarías de la biblioteca?"
        imagen.visible = False
        page.update()

    def a_pregunta7_talvez():
        estado["actual"] = "p7_talvez"
        texto.value = "¿Qué mejorarías de las computadoras?"
        imagen.visible = False
        page.update()

    def a_pregunta8_talvez():
        estado["actual"] = "p8_talvez"
        texto.value = "¿Qué mejorarías de la cafetería?"
        imagen.visible = False
        page.update()
        
    def a_pregunta9_talvez():
        estado["actual"] = "p9_talvez"
        texto.value = "¿Qué mejorarías de las sillas?"
        imagen.visible = False
        page.update()

    def a_pregunta10_talvez():
        estado["actual"] = "p10_talvez"
        texto.value = "¿Qué te hace dudar de salir de la prepa?"
        imagen.visible = False
        page.update()




    def final_bueno():
        estado["actual"] = "final_bueno"
        texto.value = " ¡Excelente! SIGUE ASI Y CON ANIMOS!!."
        page.bgcolor = ft.Colors.CYAN_100   # ✅ corregido
        btn_si.visible = False
        btn_no.visible = False
        btn_talvez.visible = False
        page.update()

    def final_medio():
        estado["actual"] = "final_medio"
        texto.value = "hey, estabas tan cercas ,reinicia >:C"
        page.bgcolor = ft.Colors.RED_50   # ✅ corregido
        btn_si.visible = False
        btn_no.visible = False
        btn_talvez.visible = False
        page.update()

    def final_malo():
        estado["actual"] = "final_malo"
        texto.value = " No quisites participar. okey :c"
        page.bgcolor = ft.Colors.BLUE_50     # ✅ corregido
        btn_si.visible = False
        btn_no.visible = False
        btn_talvez.visible = False
        page.update()

    # Secuencia combinada para 'tal vez'
    def a_pregunta2_talvez():
        estado["actual"] = "p2_talvez"
        texto.value = "¿A veces te va bien en las materias, pero a veces no? Cuéntame más."
        imagen.visible = False
        page.update()

    def a_pregunta3_talvez():
        estado["actual"] = "p3_talvez"
        texto.value = "¿Crees que la carrera que elegiste te gusta, pero tienes dudas?"
        imagen.visible = False
        page.update()

    def a_pregunta4_talvez():
        estado["actual"] = "p4_talvez"
        texto.value = "¿A veces estás seguro y otras no? ¿Por qué?"
        imagen.visible = False
        page.update()

    def a_pregunta5_talvez():
        estado["actual"] = "p5_talvez"
        texto.value = "¿Te gustan las instalaciones, pero hay algo que cambiarías?"
        imagen.visible = False
        page.update()

    def a_pregunta6_talvez():
        estado["actual"] = "p6_talvez"
        texto.value = "¿La biblioteca te parece útil, pero podría mejorar?"
        imagen.visible = False
        page.update()

    def a_pregunta7_talvez():
        estado["actual"] = "p7_talvez"
        texto.value = "¿Las computadoras te sirven, pero a veces fallan?"
        imagen.visible = False
        page.update()

    def a_pregunta8_talvez():
        estado["actual"] = "p8_talvez"
        texto.value = "¿La cafetería te gusta, pero no siempre?"
        imagen.visible = False
        page.update()

    def a_pregunta9_talvez():
        estado["actual"] = "p9_talvez"
        texto.value = "¿Las sillas están bien, pero podrían ser mejores?"
        imagen.visible = False
        page.update()

    def a_pregunta10_talvez():
        estado["actual"] = "p10_talvez"
        texto.value = "¿Crees que podrías salir de la prepa, pero no estás seguro?"
        imagen.visible = False
        page.update()

    def final_talvez():
        estado["actual"] = "final_talvez"
        texto.value = "¡Gracias por compartir tus dudas y opiniones!"
        page.bgcolor = ft.Colors.YELLOW_100
        btn_si.visible = False
        btn_no.visible = False
        btn_talvez.visible = False
        page.update()

    def on_si(e):
        if estado["actual"] == "inicio":
            a_pregunta2_si()
        elif estado["actual"] in ["p2_si", "p2_talvez"]:
            a_pregunta3_si()
        elif estado["actual"] in ["p3_si", "p3_talvez"]:
            a_pregunta4_si()
        elif estado["actual"] in ["p4_si", "p4_talvez"]:
            a_pregunta5_si()
        elif estado["actual"] in ["p5_si", "p5_talvez"]:
            a_pregunta6_si()
        elif estado["actual"] in ["p6_si", "p6_talvez"]:
            a_pregunta7_si()
        elif estado["actual"] in ["p7_si", "p7_talvez"]:
            a_pregunta8_si()
        elif estado["actual"] in ["p8_si", "p8_talvez"]:
            a_pregunta9_si()
        elif estado["actual"] in ["p9_si", "p9_talvez"]:
            a_pregunta10_si()
        elif estado["actual"] in ["p10_si", "p10_talvez"]:
            final_bueno()
        # agrega más elif para crecer tu historia                               








    def on_tal(e):
        if estado["actual"] == "inicio":
            a_pregunta2_talvez()
        elif estado["actual"] in ["p2_si", "p2_talvez"]:
            a_pregunta3_talvez()
        elif estado["actual"] in ["p3_si", "p3_talvez"]:
            a_pregunta4_talvez()
        elif estado["actual"] in ["p4_si", "p4_talvez"]:
            a_pregunta5_talvez()
        elif estado["actual"] in ["p5_si", "p5_talvez"]:
            a_pregunta6_talvez()
        elif estado["actual"] in ["p6_si", "p6_talvez"]:
            a_pregunta7_talvez()
        elif estado["actual"] in ["p7_si", "p7_talvez"]:
            a_pregunta8_talvez()
        elif estado["actual"] in ["p8_si", "p8_talvez"]:
            a_pregunta9_talvez()
        elif estado["actual"] in ["p9_si", "p9_talvez"]:
            a_pregunta10_talvez()
        elif estado["actual"] in ["p10_si", "p10_talvez"]:
            final_talvez()
        # Puedes seguir agregando más preguntas si lo deseas

            
        # agrega más elif para crecer tu historia
    def on_no(e):
        if estado["actual"] == "inicio":
            final_malo()
        elif estado["actual"] == "p2_si":
            final_medio()            
        elif estado["actual"] == "p3_si":
            final_medio()
        elif estado["actual"] == "p4_si":
            final_medio()
        elif estado["actual"] == "p5_si":
            final_medio()
        elif estado["actual"] == "p6_si":
            final_medio()
        elif estado["actual"] == "p7_si":
            final_medio()
        elif estado["actual"] == "p8_si":
            final_medio()
        elif estado["actual"] == "p9_si":
            final_medio()
        elif estado["actual"] == "p10_si":
            final_medio()
        
        
        # agrega más elif para crecer tu historia
    




    def on_reset(e):
        mostrar_inicio()

    btn_si.on_click = on_si
    btn_no.on_click = on_no
    btn_talvez.on_click = on_tal
    btn_reset.on_click = on_reset

    page.add(ft.Column([titulo, texto, imagen, botones, btn_reset],
                       alignment=ft.MainAxisAlignment.START,
                       horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                       spacing=16, expand=True))
    mostrar_inicio()

ft.app(target=main)



