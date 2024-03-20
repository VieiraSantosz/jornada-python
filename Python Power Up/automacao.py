# importar bibliotecas
import pyautogui
import pandas
import time

pyautogui.PAUSE = 0.8

# 1. abrir o navegador do chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')


# 2. acessar o site
url = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

time.sleep(1)

pyautogui.write(url)
pyautogui.press('enter')


# 3. realizar o login
time.sleep(1)

pyautogui.click(x=664, y=516)
pyautogui.write('testedeemal@gmail.com')

pyautogui.press('tab')
pyautogui.write('teste@gmail1234')

pyautogui.press('tab')
pyautogui.press('enter')


# 4. importar base de dados do arquivo csv
dados_produtos = pandas.read_csv('Python Power Up\produtos.csv')


# 5. cadastros dos produtos
for linha in dados_produtos.index:

    time.sleep(1)

    # cadastro do código
    codigo = dados_produtos.loc[linha , 'codigo']
    pyautogui.click(x=641, y=367, clicks=2)
    pyautogui.write(codigo)

    # cadastro da marca
    marca = dados_produtos.loc[linha , 'marca']
    pyautogui.press('tab')
    pyautogui.write(marca)

    # cadastro do tipo
    tipo = dados_produtos.loc[linha , 'tipo']
    pyautogui.press('tab')
    pyautogui.write(tipo)

    # cadastro da categoria
    categoria = dados_produtos.loc[linha , 'categoria']
    pyautogui.press('tab')
    pyautogui.write(str(categoria)) # uso do str para transformar um número inteiro em string

    # cadastro do preco_unitario
    preco_unitario = dados_produtos.loc[linha , 'preco_unitario']
    pyautogui.press('tab')
    pyautogui.write(str(preco_unitario)) # uso do str para transformar um número inteiro em string

    # cadastro do custo
    custo = dados_produtos.loc[linha , 'custo']
    pyautogui.press('tab')
    pyautogui.write(str(custo)) # uso do str para transformar um número inteiro em string
    pyautogui.scroll(-800)

    # cadastro da obs
    obs = dados_produtos.loc[linha , 'obs']

    if (not pandas.isna(obs)): # verifica se a coluna 'obs' contêm informação
        pyautogui.press('tab')
        pyautogui.write(obs)
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.press('enter')

    else:
        pyautogui.press('tab', presses=2)
        pyautogui.press('enter')
        pyautogui.press('enter')
        
    pyautogui.scroll(5000) # volta para o topo da tela