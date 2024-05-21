from pathlib import Path
import os

excel = ['XLSM', 'XLSX', 'XLS', 'CSV', 'XLAM', 'XLA']
fotos = ['JPG', 'JPEG', 'PNG', 'GIF', 'SVG', 'BMP']
music = ['MP3', 'WAV', 'FLAC']
video = ['MP4', 'AVI', 'MOV']
python = ['PY', 'PYTHON', 'IPYNB']
pdf = ['PDF']
zip_files = ['ZIP', 'RAR', '7Z']
powerpoint = ['PPT', 'PPTX', 'ODP']
text = ['TXT']
apps = ['EXE']
html = ['HTML']
word = ['DOC', 'DOCX']
secure = ['CER', 'KEY', 'REN', 'REQ']

# 'all' is a list of all file types
all = excel + fotos + music + video + python + pdf + zip_files + powerpoint + text + apps + html + word + secure

user = os.getlogin()

folders = [
    rf"/Users/{user}/Download/"
]

print(folders)

def organize(folder_name, file_type_list):
    for folder in folders:  # itera através de todas as pastas para organizar
        folder = Path(folder)  # converte string para path
        for file in folder.rglob('*'):  # itera através de todos os arquivos na pasta
            if file.is_file():  # verifica se o arquivo é um arquivo
                suffix = file.suffix.replace('.', '').upper()  # remove o ponto do tipo de arquivo e transforma em maiúsculas
                if any(suffix == ftype for ftype in all):  # verifica se o tipo de arquivo está na lista de todos os tipos de arquivo
                    if any(suffix == ftype for ftype in file_type_list):  # verifica o tipo de arquivo específico
                        if not Path(f'{folder}/{folder_name}').exists():  # verifica se a pasta ainda não existe
                            new_folder = Path(f'{folder}/{folder_name}')  # cria nova pasta
                            new_folder.mkdir()
                        try:
                            file.rename(f'{folder}/{folder_name}/{file.name}')  # tenta mover o arquivo para a nova pasta
                        except FileExistsError:
                            file.unlink()  # exclui o arquivo se já existir na nova pasta
                else:
                    if not Path(folder / suffix).exists():  # verifica se a pasta ainda não existe
                        new_folder = Path(folder / suffix)
                        new_folder.mkdir()  # cria pasta com novo nome
                    try:
                        file.rename(folder / suffix / file.name)  # tenta mover o arquivo para a nova pasta
                    except FileExistsError:  # se o arquivo já existe na nova pasta
                        file.unlink()  # exclui o arquivo


def delete_empty_folders():
    for folder in folders:
        folder = Path(folder)
        for x in range(10):
            for file in folder.rglob('*/'):  # itera através de todos os arquivos na pasta
                if file.is_dir():  # verifica se o arquivo é um diretório
                    try:
                        file.rmdir()  # tenta deletar o diretório
                    except:
                        pass  # se o diretório não estiver vazio, não será deletado

organize('EXCEL', excel)
organize('FOTOS', fotos)
organize('MUSIC', music)
organize('VIDEO', video)
organize('PYTHON', python)
organize('PDF', pdf)
organize('ZIP', zip_files)
organize('POWERPOINT', powerpoint)
organize('TEXT', text)
organize('APPS', apps)
organize('HTML', html)
organize('WORD', word)
organize('PDF', pdf)
organize('SECURE', secure)
delete_empty_folders()