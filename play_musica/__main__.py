from PySimpleGUI import PySimpleGUI as sg

from funcoes_extras import tela_play as tela
from funcoes_extras import play_acoes as acoes

def start():
    try:
        local_music = acoes.dir_music()

        while local_music == False:

            local_music = acoes.dir_music(tema=False, titulo='Erro! Caminho invalido.')

            if local_music == '-break-':
                break
        
        return local_music
        
    except Exception as erro:
        print(erro)

def start_play(caminho_pasta):
    try:

        

        #Configurações iniciais dos botoes
        aleatorio_button = play_button = loop_button = True

        tela_inicial = tela.tela_main()

        while True:
            window, events, values = sg.read_all_windows()

            if window == tela_inicial and events == sg.WIN_CLOSED:
                break

            elif window == tela_inicial and events == '-aleatorio-':
                if aleatorio_button == True:
                    window['-aleatorio-'].update(r'play_musica/img/play/aleatorio_25_cor.png')
                    aleatorio_button = False
                
                else:
                    window['-aleatorio-'].update(r'play_musica\img\play\aleatorio_25.png')
                    aleatorio_button = True
            
            elif window == tela_inicial and events == '-volta-':
                print('volta')

            elif window == tela_inicial and events == '-play-pause-':
                if play_button == True:
                    window['-play-pause-'].update(r'play_musica\img\play\pausa_25.png')
                    play_button = False
                
                else:
                    window['-play-pause-'].update(r'play_musica\img\play\botao-play_25.png')
                    play_button = True

            elif window == tela_inicial and events == '-proximo-':
                print('next')

            elif window == tela_inicial and events == '-loop-':

                if loop_button == True:
                    window['-loop-'].update(r'play_musica\img\play\replay_25_cor.png')
                    loop_button = False
                
                else:
                    window['-loop-'].update(r'play_musica\img\play\replay_25.png')
                    loop_button = True
        
    except Exception as erro:
        print(erro)


if __name__ == '__main__':
    inicia = start()

    if inicia != None and inicia != False:
        inicia_play = start_play(caminho_pasta=inicia)