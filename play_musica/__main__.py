import os
from PySimpleGUI import PySimpleGUI as sg
import pygame


from funcoes_extras import tela_play as tela
from funcoes_extras import play_acoes as acoes

def start():
    try:
        local_music = acoes.dir_music()

        while local_music == False:

            local_music = acoes.dir_music(tema=False, titulo='Erro! Caminho invalido.')

            if local_music == '-break-':
                break
        
        if local_music != '-break-':
            return local_music
        
        else:
            return False
        
    except Exception as erro:
        print(erro)

def start_play(caminho_pasta):
    try:
        
        #ajuste de mix de musica
        pygame.mixer.init()
        pygame.display.init()
        MUSIC_END_EVENT = pygame.USEREVENT + 1
        pygame.mixer.music.set_endevent(MUSIC_END_EVENT)

        lista_musicas = acoes.caminho_music(caminho_pasta)
        numero_musicas = len(lista_musicas)
        posicao_musica = 0

        #Configurações iniciais dos botoes
        aleatorio_button = play_button = loop_button = True

        tela_inicial = tela.tela_main()

        while True:
            window, events, values = sg.read_all_windows(timeout=1000)

            print(events)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    print(False)
                
                elif event.type == MUSIC_END_EVENT:
                    print(event)
                    posicao_musica += 1
                    acoes.play_music(lista_musicas[posicao_musica])
                    acoes.info_display(tela_inicial,lista_musicas,posicao_musica)

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
                
                if posicao_musica + 1 <= numero_musicas and posicao_musica > 0:

                    if play_button == True:
                        window['-play-pause-'].update(r'play_musica\img\play\pausa_25.png')
                        play_button = False

                    posicao_musica -= 1
                    acoes.play_music(lista_musicas[posicao_musica])
                    acoes.info_display(tela_inicial,lista_musicas,posicao_musica)

                else:
                    posicao_musica = numero_musicas-1
                    acoes.play_music(lista_musicas[posicao_musica])
                    acoes.info_display(tela_inicial,lista_musicas,posicao_musica)

            elif window == tela_inicial and events == '-play-pause-':

                if play_button == True:
                    window['-play-pause-'].update(r'play_musica\img\play\pausa_25.png')
                    play_button = False

                    if acoes.tocando() == False:
                        acoes.play_music(lista_musicas[posicao_musica])
                        acoes.info_display(tela_inicial,lista_musicas,posicao_musica)

                else:
                    window['-play-pause-'].update(r'play_musica\img\play\botao-play_25.png')
                    play_button = True
                    if acoes.tocando():
                        acoes.pause_music()

            elif window == tela_inicial and events == '-proximo-':
                
                if posicao_musica + 1 < numero_musicas:
                    if play_button == True:
                        window['-play-pause-'].update(r'play_musica\img\play\pausa_25.png')
                        play_button = False
                    
                    posicao_musica+= 1
                    acoes.play_music(lista_musicas[posicao_musica])
                    acoes.info_display(tela_inicial,lista_musicas,posicao_musica)
                
                else:

                    posicao_musica = 0
                    acoes.play_music(lista_musicas[posicao_musica])
                    acoes.info_display(tela_inicial,lista_musicas,posicao_musica)

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