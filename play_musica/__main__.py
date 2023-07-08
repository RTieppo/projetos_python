from random import shuffle
from time import sleep
from PySimpleGUI import PySimpleGUI as sg
from pygame import mixer, display ,USEREVENT, event



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
        mixer.init()
        display.init()
        MUSIC_END_EVENT = USEREVENT + 1
        mixer.music.set_endevent(MUSIC_END_EVENT)

        lista_musicas = acoes.caminho_music(caminho_pasta)
        lista_base = acoes.caminho_music(caminho_pasta)
        numero_musicas = len(lista_musicas)
        posicao_musica = 0

        #Configurações iniciais dos botoes
        aleatorio_button = play_button = loop_button = True

        #config loop musica
        loop = ''

        #leitura de musica
        duracao_musica =  tempo_atual_musica = 0

        tela_inicial = tela.tela_main()

        while True:
            window, events, values = sg.read_all_windows(timeout=900)
            if mixer.music.get_busy():
                tempo_atual_musica += 1
            
            minuto = tempo_atual_musica//60
            segundos = tempo_atual_musica%60

            if segundos < 10:
                segundos = f'0{segundos}'

            tela_inicial['-tempo_corrido-'].update(f'{minuto}:{segundos}')

            for evento in event.get():
                if evento.type == MUSIC_END_EVENT:

                    if loop == '-inicia-':
                        acoes.play_music(replay)
                        acoes.info_display(tela_inicial,lista_musicas,posicao_musica)
                        musica = mixer.Sound(lista_musicas[posicao_musica])
                        duracao_musica = musica.get_length()
                        musica = mixer.Sound(lista_musicas[posicao_musica])
                        duracao_musica = musica.get_length()
                        ajusta = f'{duracao_musica/60:.2f}'

                        tela_inicial['-tempo_total-'].update(f'{ajusta.replace(".",":")}')
                    
                    elif posicao_musica + 1 < numero_musicas:

                        replay = lista_musicas[posicao_musica]
                        posicao_musica += 1
                        acoes.play_music(lista_musicas[posicao_musica])
                        acoes.info_display(tela_inicial,lista_musicas,posicao_musica)
                        musica = mixer.Sound(lista_musicas[posicao_musica])
                        duracao_musica = int(musica.get_length())
                    
                        tela_inicial['-tempo_total-'].update(f'{duracao_musica//60}:{duracao_musica%60}')

                        tempo_atual_musica = 0
                    
                    else:
                        posicao_musica = 0
                        replay = lista_musicas[posicao_musica]
                        acoes.play_music(lista_musicas[posicao_musica])
                        acoes.info_display(tela_inicial,lista_musicas,posicao_musica)
                        musica = mixer.Sound(lista_musicas[posicao_musica])
                        duracao_musica = int(musica.get_length())
                    
                        tela_inicial['-tempo_total-'].update(f'{duracao_musica//60}:{duracao_musica%60}')

                        tempo_atual_musica = 0

            if window == tela_inicial and events == sg.WIN_CLOSED:
                break

            elif window == tela_inicial and events == '-aleatorio-':

                if aleatorio_button == True:
                    window['-aleatorio-'].update(r'play_musica/img/play/aleatorio_25_cor.png')
                    aleatorio_button = False
                    shuffle(lista_musicas)
                
                else:
                    window['-aleatorio-'].update(r'play_musica\img\play\aleatorio_25.png')
                    aleatorio_button = True
                    lista_musicas = lista_base
            
            elif window == tela_inicial and events == '-volta-':
                
                if posicao_musica + 1 <= numero_musicas and posicao_musica > 0:

                    if play_button == True:
                        window['-play-pause-'].update(r'play_musica\img\play\pausa_25.png')
                        play_button = False

                    posicao_musica -= 1
                    replay = lista_musicas[posicao_musica]
                    acoes.play_music(lista_musicas[posicao_musica])
                    acoes.info_display(tela_inicial,lista_musicas,posicao_musica)
                    musica = mixer.Sound(lista_musicas[posicao_musica])
                    duracao_musica = int(musica.get_length())
                    
                    tela_inicial['-tempo_total-'].update(f'{duracao_musica//60}:{duracao_musica%60}')

                    tempo_atual_musica = 0

                else:
                    posicao_musica = numero_musicas-1
                    replay = lista_musicas[posicao_musica]
                    acoes.play_music(lista_musicas[posicao_musica])
                    acoes.info_display(tela_inicial,lista_musicas,posicao_musica)

                    musica = mixer.Sound(lista_musicas[posicao_musica])
                    duracao_musica = int(musica.get_length())

                    tela_inicial['-tempo_total-'].update(f'{duracao_musica//60}:{duracao_musica%60}')

                    tempo_atual_musica = 0

            elif window == tela_inicial and events == '-play-pause-':

                if play_button == True:
                    window['-play-pause-'].update(r'play_musica\img\play\pausa_25.png')
                    play_button = False

                    if acoes.tocando() == False:
                        musica = mixer.Sound(lista_musicas[posicao_musica])
                        duracao_musica = int(musica.get_length())
                        window['-tempo_total-'].update(f'{duracao_musica//60}:{duracao_musica%60}')
                        acoes.play_music(lista_musicas[posicao_musica])
                        acoes.info_display(tela_inicial,lista_musicas,posicao_musica)
                        tempo_atual_musica = 0

                else:
                    window['-play-pause-'].update(r'play_musica\img\play\botao-play_25.png')
                    play_button = True
                    if acoes.tocando():
                        acoes.pause_music()
                        tempo_atual_musica = 0

            elif window == tela_inicial and events == '-proximo-':
                
                if posicao_musica + 1 < numero_musicas:
                    if play_button == True:
                        window['-play-pause-'].update(r'play_musica\img\play\pausa_25.png')
                        play_button = False

                    posicao_musica+= 1
                    replay = lista_musicas[posicao_musica]
                    acoes.play_music(lista_musicas[posicao_musica])
                    acoes.info_display(tela_inicial,lista_musicas,posicao_musica)

                    musica = mixer.Sound(lista_musicas[posicao_musica])
                    duracao_musica = int(musica.get_length())
                    
                    tela_inicial['-tempo_total-'].update(f'{duracao_musica//60}:{duracao_musica%60}')

                    tempo_atual_musica = 0

                else:

                    posicao_musica = 0
                    replay = lista_musicas[posicao_musica]
                    acoes.play_music(lista_musicas[posicao_musica])
                    acoes.info_display(tela_inicial,lista_musicas,posicao_musica)

                    musica = mixer.Sound(lista_musicas[posicao_musica])
                    duracao_musica = int(musica.get_length())
                    
                    tela_inicial['-tempo_total-'].update(f'{duracao_musica//60}:{duracao_musica%60}')

                    tempo_atual_musica = 0

            elif window == tela_inicial and events == '-loop-':

                if loop_button == True:
                    window['-loop-'].update(r'play_musica\img\play\replay_25_cor.png')
                    loop_button = False
                    loop = '-inicia-'
                    replay = lista_musicas[posicao_musica]
                
                else:
                    window['-loop-'].update(r'play_musica\img\play\replay_25.png')
                    loop_button = True
                    loop = '-cancela-'
        
    except Exception as erro:
        print(erro)


if __name__ == '__main__':
    inicia = start()

    if inicia != None and inicia != False:
        inicia_play = start_play(caminho_pasta=inicia)