from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

# Defina as configurações do proxy
proxy_address = "https://solucoes.receita.fazenda.gov.br/servicos/cnpjreva/cnpjreva_solicitacao.asp"
proxy_port = "https://solucoes.receita.fazenda.gov.br/servicos/cnpjreva/cnpjreva_solicitacao.asp"

# Configure as opções do Chrome com o proxy
chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={proxy_address}:{proxy_port}')

# CNPJ
cnpj = "11.097.292/0001-49"

# Entrada no site.
nav = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
link = "https://solucoes.receita.fazenda.gov.br/servicos/cnpjreva/cnpjreva_solicitacao.asp"
nav.get(link)
sleep(10)

# Preencha o campo CNPJ
campo_cnpj = nav.find_element(By.XPATH, "//input[@id='cnpj']")
campo_cnpj.send_keys(cnpj)

# Aguarde para resolver o captcha
sleep(10)

# Restante do seu código para resolver o captcha com o Anticaptcha

# Ajuste o tempo de espera conforme necessário
sleep(10)

# Manter o navegador aberto ou encerrá-lo quando terminar
# nav.quit()
