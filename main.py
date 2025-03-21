
#titulo zapzap
#botao iniciar chat
    #popup
        #bem vindo 
        #escreva seu nome
        #entrar chat
#chat
    #usuario entrou
    #mensagens usuario
#barra de digitação
#botao enviar

import flet as ft

def main(page):
    
    imagem = ft.Image(
        src=f"5ae21cc526c97415d3213554.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,)
    
    titulo = ft.Text("Zap Zap", color='greenACCENT700',size =50, weight=ft.FontWeight.W_800, italic=True)
    

    linha_inicial = ft.Row([imagem, titulo], alignment="center")
    page.add(linha_inicial)
    
    nome_usuario = ft.TextField(label='Qual seu nome?')
    
    campo_msg = ft.TextField(label="Digite aqui")
    
    chat = ft.Column(expand=2)

    def enviar_msg_tunel(info):
        chat.controls.append(ft.Text((info),color='white',size =15, weight=ft.FontWeight.W_800))
        page.update()

    
    page.pubsub.subscribe(enviar_msg_tunel)
    
    def mensagem(evento):
        texto = f'{nome_usuario.value}: {campo_msg.value}'
        page.pubsub.send_all(texto)
        campo_msg.value = ""
        page.update()

    
    botao_msg = ft.ElevatedButton('Enviar', on_click=mensagem, bgcolor='green500', color='white')  
    
    def abrir_chat(evento):
        popup.open=False
        page.remove(linha_botao)
        page.remove(linha_inicial)
        page.add(chat)
        linha_mensagem = ft.Row([campo_msg, botao_msg], alignment='center',vertical_alignment='end')
        page.add(linha_mensagem)
        entrou = f'{nome_usuario.value} entrou no chat'
        page.pubsub.send_all(entrou)
        page.update()
        
    popup = ft.AlertDialog(
        open=False, 
        modal=True,
        title= ft.Text('Bem-vindo ao Zap Zap!', weight=ft.FontWeight.W_800),
        content=nome_usuario,
        actions=[ft.ElevatedButton('Entrar no Chat', on_click=abrir_chat, bgcolor='green500', color='white')])
    
    def iniciar_chat(evento):
        page.dialog = popup
        popup.open = True
        page.update()

        
    
    iniciar = ft.ElevatedButton('Iniciar Conversa', on_click=iniciar_chat, icon="chat", color='white', bgcolor='black',)
    linha_botao = ft.Row([iniciar], alignment='center')
    page.add(linha_botao)


#ft.app(main, view=ft.WEB_BROWSER)
ft.app(main)
