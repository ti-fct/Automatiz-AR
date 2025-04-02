# 🏫❄️Automação de Ar-Condicionado com Selenium

## 📌Descrição

Este sistema automatiza o controle de ar-condicionado em diferentes salas da Faculdade de Ciência e Tecnologia, utilizando a biblioteca Selenium para interagir com uma interface web. O sistema verifica o horário atual e, com base nisso, liga ou desliga os aparelhos conforme regras predefinidas.

O script realiza as seguintes operações:

Acessa a interface web de controle do ar-condicionado.

Seleciona os ambientes a serem controlados.

Ativa ou desativa o ar-condicionado conforme o horário.

Registra logs de operações realizadas.

Envia notificações em caso de erro.

## 🛠️Tecnologias Utilizadas

- Python 3

- Selenium

- WebDriver Manager

- Dotenv

- Requests

- Logging

- Cron

## 📥Instalação

1. Clone este repositório:
   
   `git clone https://github.com/seu-usuario/seu-repositorio.git`

2. Acesse o diretório do projeto:
   
   `cd seu-repositorio`

4. Crie um ambiente virtual e ative-o (opcional):
   
   ```
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```


4. Instale as dependências:
   
   `pip install -r requirements.txt`

5. Crie um arquivo .env na raiz do projeto e configure as URLs do sistema:
   
   ```
   URL_CHAT_TEST=https://seu-webhook-de-notificacao.com
   
   URL_CHAT_PROD=https://seu-webhook-de-notificacao.com
   
   ALA_A=https://sistema-ala-a.com
   
   ALA_B=https://sistema-ala-b.com
   ```

## 🚀Como Usar

1. Certifique-se de que o WebDriver do Chrome esta instalado e configurado corretamente.

2. Execute o script Python:
   
   `python3 automacao_ar_condicionado.py`

3. O script ira rodar automaticamente de acordo com os horários predefinidos, registrando logs e enviando notificações em caso de erro.

## ⏲️ Execução Automatica com Cron

1. Abra o crontab
   
   `crontab -e`
   
2.  Adicione a seguinte linha de código:
   
   ```
   50 11  * * *  root python3 /home/suporte/projeto/automatizaArCondicionado_ala-B.py
   
   30 17  * * *  root python3 /home/suporte/projeto/automatizaArCondicionado_ala-A.py
   
   00 18  * * *  root python3 /home/suporte/projeto/automatizaArCondicionado_ala-B.py
```
   

## 📂Estrutura do Código

- As operações de clique são realizadas por driver.find_element(By.XPATH, elemento).click().

- Os logs são armazenados em arquivos específicos dependendo do horário de execução.

- O script termina a execução fechando o navegador com driver.quit().

## ❓Possíveis Problemas e Soluções

- Erro ao acessar o WebDriver: Verifique se o chromedriver esta instalado, configurado corretamente e a versão é a mesma do Chrome.

- Elemento não encontrado: Certifique-se de que a estrutura da pagina web não foi alterada.

- Erro de conexão: Verifique sua conexão com a internet e as URLs configuradas no .env.
