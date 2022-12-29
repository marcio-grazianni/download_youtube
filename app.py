from pytube import YouTube


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path="C:/Downloads/")
        print("Download completado com sucesso.")
    except:
        print("Ocorreu um erro efetuando o download do link: " + link)


link = input("Coloque seu link do youtube aqui! URL: ")
Download(link)
