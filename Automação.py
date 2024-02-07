# Entrar no sistema da Empresa
   # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Fazer o login
#  Importar a base de dados de produtos
# Cadastrar um Produto
# Repitir o cadastro para todos os produtos

import pyautogui
import time 

pyautogui.PAUSE = 0.5

 # abrir o navegador
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("Enter")

time.sleep(3)

 # acessar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("Enter")

time.sleep(3)

# fazer o login
pyautogui.click(x=484, y=366)
pyautogui.write('a')
time.sleep(2)
pyautogui.press("tab")
pyautogui.write('a')  # campo de senha
pyautogui.press("Enter")

time.sleep(3)

# importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

#index = para procurar por linhas na tabela de dados e column para procurar colunas na tabela de dados
for linha in tabela.index:

    # cadastrar um produto
    pyautogui.click(x=466, y=243)

    #preenchendo os campos
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write((str(tabela.loc[linha, "marca"])))
    pyautogui.press("tab")
    pyautogui.write((str(tabela.loc[linha, "tipo"])))
    pyautogui.press("tab")
    pyautogui.write((str(tabela.loc[linha, "categoria"])))
    pyautogui.press("tab")
    pyautogui.write((str(tabela.loc[linha, "preco_unitario"])))
    pyautogui.press("tab")
    pyautogui.write((str(tabela.loc[linha, "custo"])))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    #enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(600)







