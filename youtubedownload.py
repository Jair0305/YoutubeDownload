# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:30:05 2024

@author: chama
"""

from pytube import YouTube
import os
from moviepy.editor import VideoFileClip


def descargar_video(url, output_path):
    try:
        yt = YouTube(url)
        print(f'Descargando video: {yt.title}...')
        yt.streams.get_highest_resolution().download(output_path)
        print(f'{yt.title} descargado exitosamente')
    except Exception as e:
        print(f'No se puede descargar el video {str(e)}')

def descargar_video_menu():
    url = input('Introduce la url del video de youtube: ')
    
    project_directory = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(project_directory, '')
    
    print(f'El directorio del proyecto es: {project_directory}')
    print(f'Los archivos se guardaran en: {output_path}')
    
    descargar_video(url, output_path)

def convertir_a_mp3(ruta_video, ruta_salida='./'):
    video_clip = VideoFileClip(ruta_video)
    
    # Obten el nombre del archivo de video sin la extensión
    video_title = os.path.splitext(os.path.basename(ruta_video))[0]
    
    mp3_path = os.path.join(ruta_salida, f'{video_title}.mp3')
    
    print(f'Convirtiendo a MP3: {video_title}')
    video_clip.audio.write_audiofile(mp3_path)
    print(f'Conversión completada. MP3 guardado en: {mp3_path}')


def descargar_audio_menu():
    url_youtube = input('Introduce la url del video: ')

    project_directory = os.getcwd()
    output_path = os.path.join(project_directory, '')

    descargar_video(url_youtube, output_path)

    video_title = YouTube(url_youtube).title
    video_path = os.path.join(output_path, f'{video_title}.mp4')

    convertir_a_mp3(video_path, output_path)

def main():
    res = int(input('Que quieres hacer?\n 1)DescargarVideo\n2)Descargar mp3\n\nElige:'))
    if(res == 1):
        descargar_video_menu()
    if(res == 2):
        descargar_audio_menu()
        
if __name__ == "__main__":
    main()
