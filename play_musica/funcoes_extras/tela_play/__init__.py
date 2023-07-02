
from PySimpleGUI import PySimpleGUI as sg


#Definindo tema geral
tema_g = 'DarkBlue2'

#Define fonte


def tela_main():
    
    sg.theme(tema_g)

    display =[
        [sg.Image(r'play_musica\img\test\pylot.png')]
    ]

    cabeca = [
        [sg.Text('PySimpleGUI Player - By RTieppo', justification='c')],
        [sg.Frame('',layout=display)],
        [sg.Text('Aperte o Play...',justification='c',key='-name_music-')]

    ]

    corpo = [
        [sg.Image(r'play_musica\img\play\aleatorio_25.png',pad=(20,10), enable_events=True,key='-aleatorio-'),sg.Image(r'play_musica\img\play\costas_25.png',pad=(20,10),enable_events=True,key='-volta-'), sg.Image(r'play_musica\img\play\botao-play_25.png',pad=(20,10),enable_events=True,key='-play-pause-'), sg.Image(r'play_musica\img\play\proximo_25.png',pad=(20,10),enable_events=True,key='-proximo-'), sg.Image(r'play_musica\img\play\replay_25.png',pad=(20,10),enable_events=True,key='-loop-')],
    ]

    main =[
        [sg.Column(layout=cabeca,element_justification='c')],
        [sg.HSep()],
        [sg.Column(layout=corpo,element_justification='c',pad=(20,20))]
    ]

    return sg.Window('MIX.PY', finalize=True, size=(400,550), layout = main,
    margins=(10,10), element_justification='c', icon= (r'play_musica\img\icon\botoes.ico'),
    text_justification='c')
