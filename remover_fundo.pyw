
from rembg import remove
from PIL import Image
import tkinter as tk
from tkinter import filedialog

janela = tk.Tk()
arquivo_selecionado = filedialog.askopenfilename()
janela.destroy()

imagem_original = arquivo_selecionado
nova_imagem = r'C:\Users\dylan\Downloads\teste.png'

arquivo = Image.open(imagem_original)
imagem = remove(arquivo)
imagem.save(nova_imagem)