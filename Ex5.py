import os


def pedirNumeroEntero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Elige una opcion: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num


salir = False
opcion = 0
n = 3  # length data input

while not salir:

    print ("1. Opcion 1 : Cortar 10 segundos de video")
    print ("2. Opcion 2 : Histograma")
    print ("3. Opcion 3 : Elegir resolucion")
    print ("4. Conocer o modificar codec de audio")
    print ("5. Salir")

    # print ("Elige una opcion")

    opcion = pedirNumeroEntero()

    if opcion == 1:
        os.system('ffmpeg -i bbb_video.mp4 -ss 00:00:17.0 -t 00:00:10 bbb_10seconds.mp4')

    elif opcion == 2:
        os.system('ffmpeg -i bbb_10seconds.mp4 -vf "split=2[a][b], [b] histogram, format=yuva444p[hh], '
                  '[a][hh]overlay" bbb_histogram.mp4')

    elif opcion == 3:
        print("Resolucion:")
        print("\t 1. 720p")
        print("\t 2. 480p")
        print("\t 3. 360px240p")
        print("\t 4. 160x120p")
        resize = int(input("Selecciona una opción: "))

        if resize == 1:
            os.system('ffmpeg -i bbb_10seconds.mp4 -vf scale=-1:720 bbb_720.mp4')
        elif resize == 2:
            #os.system('ffmpeg -i bbb_10seconds.mp4 -vf scale=-480:-1 -c:v libx264 -crf 18 -preset veryslow -c:a copy bbb_480.mp4')
            os.system('ffmpeg -i bbb_10seconds.mp4 -vf scale=480:-1  bbb_480.mp4')
        elif resize == 3:
            #os.system('ffmpeg -i bbb_10seconds.mp4 -vf scale=360:240 -c:v libx264 -crf 18 -preset veryslow -c:a copy bbb_360x240.mp4')
            command = "ffmpeg -i bbb_10seconds.mp4 -vf " + '"' + "scale='min(360,iw)':'min(240,ih)'" +'"' + " bbb_360x240.mp4"
            #print(command)

            #os.system(f"ffmpeg -i bbb_10seconds.mp4 -vf "scale= '{minW}':'{min(240,ih)}'"  bbb_360x240.mp4"
            os.system(command)
        elif resize == 4:
            #os.system('ffmpeg -i bbb_10seconds.mp4 -vf scale=160:120  bbb_160x120.mp4')
            command = "ffmpeg -i bbb_10seconds.mp4 -vf " + '"' + "scale='min(160,iw)':'min(120,ih)'" + '"' + " bbb_160x120.mp4"
            os.system(command)
        else:
            print("Opción invalida")
            resize = int(input("Selecciona una opción: "))

    elif opcion == 4:
        print("Codec Menu:")
        print("\t1. Codec original del video")
        print("\t2. Conversion del audio a MP3 mono")
        codec_menu = int(input("Selecciona una opcion: "))

        if codec_menu == 1:
            #os.system('ffmpeg -i bbb_10seconds.mp4 -c codec')
            #os.system('mediainfo --Inform = Audio;%Codec% bbb_10seconds')
            os.system('ffprobe -loglevel error -show_entries stream=codec_type,codec_name -of default=nw=1 bbb_10seconds.mp4')
            #os.system('ffprobe -v error -select_streams v:1 -show_entries stream=codec_type,codec_name -of default=nw=1 bbb_10seconds.mp4')

        elif codec_menu == 2:
            os.system('ffmpeg -i bbb_10seconds.mp4 -ac 1 -acodec mp3 -vcodec copy bbb_MP3_mono.mp4')
        else:
            print("Opción inválida")

    elif opcion == 5:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 5")

print ("Fin")
