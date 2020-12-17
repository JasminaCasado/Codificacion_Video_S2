# **S2 SCAV VIDEO**
En este repositorio se encuentras los ejercicios adjuntos del segundo seminario de codificacion de video de la asignatura para la Universidad Pompeu Fabra. 

## 1. Corta 10 segundos del BBB video
Para cortar 10 segundos del video original usamos el comando 

`ffmpeg -i bbb_video.mp4 -ss 00:17:00 -t 00:00:10 bbb_10seconds.mp4` 

## 2. Generar el histograma del recorte de video anterior 
Para generar el histograma en YUV usamos el comando siguiente. En este comando lo que hacemos es crear sobre el video una matriz en la que se muestra cada canal por separado con una resolucion de 4:4:4, lo que significa que no hay perdida de información. 

`'ffmpeg -i bbb_10seconds.mp4 -vf "split=2[a][b], [b] histogram, format=yuva444p[hh],'[a][hh]overlay" bbb_histogram.mp4'`
## 3. Reescalado del vido

Al igual que en la primera práctica para reescalar el video usamos los comandos siguientes, 

* Reescalado a 720p
`ffmpeg -i bbb_10seconds.mp4 -vf scale=-1:720 bbb_720.mp4`

* Reescalado a 480p
`ffmpeg -i bbb_10seconds.mp4 -vf scale=-480:-1 -c:v libx264 -crf 18 -preset veryslow -c:a copy bbb_480.mp4`

* Reescalado a 360x240p
`ffmpeg -i bbb_10seconds.mp4 -vf scale=360:240 -c:v libx264 -crf 18 -preset veryslow -c:a copy bbb_360x240.mp4`

* Reescalado a 160x120p
`ffmpeg -i bbb_10seconds.mp4 -vf scale=160:120  bbb_160x120.mp4`

## 4. Canvia el audio y el codec 
En este caso podemos ver cual es el codec del audio original y canviar ese audio al formato MP3 mono. 

Para visualizar el codec usamos el comando,
`ffprobe -loglevel error -show_entries stream=codec_type,codec_name -of default=nw=1 bbb_10seconds.mp4`

Para la modificación del audio usamos, 

`ffmpeg -i bbb_10seconds.mp4 -ac 1 -acodec mp3 -vcodec copy bbb_MP3_mono.mp4`

## 5. Todo en uno 
Archivo de Python que nos permite ejecutar los cuatro ejercicios del seminario. 

## Referencias 
* https://superuser.com/questions/138331/using-ffmpeg-to-cut-up-video
* https://superuser.com/questions/1514997/compressing-grayscale-8-bit-png-sequences-with-ffmpeg
* https://trac.ffmpeg.org/wiki/Scaling
* https://ffmpeg.org/ffprobe.html
