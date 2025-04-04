# 🏫❄️ Automação de Ar-Condicionado com Selenium

## 📌 Descrição
O sistema de automação de ar condicionado desenvolvido para a Faculdade de Ciências e Tecnologia da Universidade Federal de Goiás (FCT/UFG) visa otimizar o uso energético dos aparelhos de ar condicionado através de um controle efetivo e inteligente. Este projeto se destaca como pioneiro na aplicação de tecnologia de automação em climas controlados na UFG, proporcionando um modelo que pode ser replicado em outros edifícios da universidade.

### Objetivo
O principal objetivo deste sistema é implementar ações de eficiência energética que garantam um controle eficaz do funcionamento dos aparelhos de ar condicionado instalados na FCT.

O script realiza as seguintes operações:

* Acessa a interface web de controle do ar-condicionado.
* Seleciona os ambientes a serem controlados.
* Ativa ou desativa o ar-condicionado conforme o horário.
* Registra logs das operações realizadas.
* Envia notificações em caso de erro.

## 🛠️ Tecnologias Utilizadas

* Python 3
* Selenium
* WebDriver Manager
* Dotenv
* Requests
* Logging
* Cron

## 📥 Instalação

1.  Clone este repositório:

    ```bash
    git clone https://github.com/ti-fct/Automatiz-AR.git
    ```

2.  Acesse o diretório do projeto:

    ```bash
    cd seu-repositorio
    ```

3.  Crie um ambiente virtual e ative-o (opcional):

    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
    ```

4.  Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

5.  Crie um arquivo `.env` na raiz do projeto e configure as URLs do sistema:

    ```env
    URL_CHAT_TEST=https://seu-webhook-de-notificacao.com

    URL_CHAT_PROD=https://seu-webhook-de-notificacao.com

    ALA_A=https://sistema-ala-a.com

    ALA_B=https://sistema-ala-b.com
    ```

## 🚀 Como Usar

1.  Certifique-se de que o WebDriver do Chrome está instalado e configurado corretamente. Também é importante verificar a versão instalada do Google Chrome. Digite o comando no terminal:

    ```bash
    google-chrome --version
    ```

2.  Acesse o site https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json e procure o ChromeDriver compatível com a versão do seu Google Chrome.

3.  Execute o script Python:

    ```bash
    python3 automacao_ar_condicionado.py
    ```

4.  O script irá rodar automaticamente de acordo com os horários predefinidos, registrando logs e enviando notificações no Google Chat em caso de erro.

## ⏲️ Execução Automática com Cron

O sistema será executado às 11:50 nas salas de aula, quando inicia o intervalo para o almoço. Às 17:30 desligará os ares da Ala A e às 18h desligará o grupo Sala de Aulas e Administração. É importante ressaltar que o ar da sala da Microscopia não pode ser desligado.

1.  Abra o crontab:

    ```bash
    crontab -e
    ```

2.  Adicione as seguintes linhas de código:

    ```cron
    50 11 * * * root python3 /home/suporte/projeto/automatizaArCondicionado.py
    30 17 * * * root python3 /home/suporte/projeto/automatizaArCondicionado.py
    00 18 * * * root python3 /home/suporte/projeto/automatizaArCondicionado.py
    ```

3. Reinicie o Cron:

    ```bash
    sudo service cron reload
    ```

## 📂 Estrutura do Código

* As operações de clique são realizadas por `driver.find_element(By.XPATH, elemento).click()`.
* Os logs são armazenados em arquivos específicos, dependendo do horário de execução.
* O script finaliza a execução fechando o navegador com `driver.quit()`.

## ❓ Possíveis Problemas e Soluções

* **Erro ao acessar o WebDriver:** Verifique se o ChromeDriver está instalado, configurado corretamente e se a versão é a mesma do Chrome.
* **Elemento não encontrado:** Certifique-se de que a estrutura da página web não foi alterada.
* **Erro de conexão:** Verifique sua conexão com a internet e as URLs configuradas no arquivo `.env`.
