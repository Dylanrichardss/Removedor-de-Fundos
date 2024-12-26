# Removedor-de-Fundos
<b> Script Python que retira o fundo da imagem que o usuário selecionar.</b>

## Demonstração

Ao iniciar o arquivo pyw, o usuário seleciona no diretório, uma imagem que deseja retirar o fundo.

![image](https://github.com/user-attachments/assets/f0d92a19-b4c7-48ed-8de3-36387b07bcb0)


O Script processa a imagem e salva em formato png na pasta de Downloads.

<p align="center">
  <img src="https://github.com/user-attachments/assets/d99ee621-f5b3-4e87-9650-b14830289e15" alt="Imagem original" width="300"/>

  <img src="https://github.com/user-attachments/assets/e8507205-7b42-4329-b405-381856607953" alt="Teste" width="300"/>
</p>



## Código
``` bash
from rembg import remove
from PIL import Image
import tkinter as tk
from tkinter import filedialog

janela = tk.Tk()
arquivo_selecionado = filedialog.askopenfilename()
janela.destroy()

imagem_original = arquivo_selecionado
nova_imagem = r'C:\Users\seu_usuario\Downloads\teste.png'

arquivo = Image.open(imagem_original)
imagem = remove(arquivo)
imagem.save(nova_imagem)
```
