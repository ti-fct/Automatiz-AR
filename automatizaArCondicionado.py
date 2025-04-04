from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime
from dotenv import load_dotenv
import requests
import urllib3
import logging
import time
import os

urllib3.disable_warnings()

load_dotenv()
url = os.getenv("URL_CHAT_TEST")  # ambiente de teste
#url = os.getenv("URL_CHAT_PROD") #ambiente de produção

driver_options = webdriver.ChromeOptions()
driver_options.add_argument('--headless') # Não abre a janela do navegador
driver_options.add_argument('--no-sandbox')
driver_options.add_argument('--disable-dev-shm-usage') # Desativa o uso do sistema de arquivos de memória compartilhada
service = ChromeService('/home/suporte/projeto/chromedriver-linux64/chromedriver')
driver = webdriver.Chrome(service=service, options=driver_options)

hora_atual = datetime.now().time()
hora_inicio = datetime.strptime('17:25', '%H:%M').time()
hora_fim = datetime.strptime('17:35', '%H:%M').time()

if hora_inicio <= hora_atual <= hora_fim:
    logging.basicConfig(filename='/home/suporte/projeto/log_ar_condicionado_ala-A.txt', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
else:
    logging.basicConfig(filename='/home/suporte/projeto/log_ar_condicionado_ala-B.txt', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

def enviar_mensagem_erro(mensagem):
    json_erro = {'text': mensagem}
    requests.post(url=url, json=json_erro, stream=True, verify=False)

def clicar_elemento(elemento):
    try:
        time.sleep(2) # Aguarda 2 segundos

        driver.find_element(By.XPATH, elemento).click()

        if elemento == "//td[@onclick='javascript:operate(1);']":
            elemento = 'All-Ctrl'
        elif elemento == '//*[@id="set"]/table/tbody/tr[2]/td/table/tbody/tr[14]/td/table/tbody/tr/td[3]':
            elemento = 'Turn Off'
        elif elemento == "//td[@onclick='sel_room(2)']":
            elemento = 'Sala de aula'
        elif elemento == "//td[@onclick='sel_room(3)']":
            elemento = 'Sala de aula'
        elif elemento == '//*[@id="ac_2"]':
            elemento = 'Sala TI'
        else:
            elemento = 'Outros'
        
        print(f'Cliquei no elemento {elemento}')
        logging.info(f'Cliquei no elemento {elemento}')

    except NoSuchElementException as erro:
        mensagem_erro = f'Não encontrei o elemento {elemento}'
        print(str(datetime.now()) + mensagem_erro, erro)
        logging.error(mensagem_erro, exc_info=True)
        enviar_mensagem_erro(mensagem_erro)
        driver.quit()
        exit()

    except ElementNotInteractableException as erro:
        mensagem_erro = f'O Elemento não é interativo: {elemento}'
        print(str(datetime.now()) + mensagem_erro, erro)
        logging.error(mensagem_erro, exc_info=True)
        enviar_mensagem_erro(mensagem_erro)
        driver.quit()
        exit()

# Acessa o sistema Ala-A se o horario for 17:30
try:
    if hora_inicio <= hora_atual <= hora_fim:
        driver.get(os.getenv("ALA_A"))
    else:
        driver.get(os.getenv("ALA_B"))

    time.sleep(2)
    relatorio = driver.find_element(By.ID, 'msg').text
    status = relatorio.replace("OFF","DESLIGADO").replace("COOL","LIGADO")
    logging.info('\n'+status)

except WebDriverException as erro:
    mensagem_erro = 'Erro ao acessar o sistema do ar condicionado, verifique a conexão com a internet'
    print(str(datetime.now()) + mensagem_erro, erro)
    logging.error(mensagem_erro, exc_info=True)
    enviar_mensagem_erro(mensagem_erro)
    driver.quit()
    exit()

sala_de_aula = "//td[@onclick='sel_room(2)']"
administracao = "//td[@onclick='sel_room(3)']"
todos = "//td[@onclick='javascript:operate(1);']" # All-Ctrl
allOff = '//*[@id="tbl"]/table/tbody/tr[2]/td/table[1]/tbody/tr/td[2]' #botão all-Off que desliga todo o grupo

grupos = []

# Adiciona administracao se estiver dentro do horário especificado
if hora_inicio <= hora_atual <= hora_fim:
    grupos.append(todos)
    logging.info(f'Horário atual: {hora_atual.strftime("%H:%M")} - Adicionando administração à lista de grupos')
else:
    grupos.append(sala_de_aula)
    grupos.append(administracao)

for grupo in grupos:

    # Clica no ar condicionado
    clicar_elemento(grupo)

    # Clica no Turn Off
    clicar_elemento('//*[@id="set"]/table/tbody/tr[2]/td/table/tbody/tr[14]/td/table/tbody/tr/td[3]')

driver.quit()
logging.info('\n'+'________________________________________________'+'\n')
print('Finalizado')
exit()