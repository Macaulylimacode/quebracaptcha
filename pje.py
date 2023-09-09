# Novo modo de ter uma automação web.
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #
from selenium.webdriver.chrome.service import Service
# Controle das demais funções.
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
from anticaptchaofficial.recaptchav3proxyless import *
#from chave import chave_api
from chave_captcha import chave_cap
import python_anticaptcha


# Número da OAB

numero_oab = 37463

# Entrada no site.

nav = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = ("https://pje.tjpe.jus.br/2g/ConsultaPublica/listView.seam")
nav.get(link)
sleep(30)

# Entrada em cada processo
#processos = driver.find_element(By.XPATH, "//b[@class='btn-block']")
#for processo in processos:
   # processos.click()
    #sleep(10)


# Digitação do numero da OAB
campo_oab = nav.find_element(By.XPATH,"//Input[@id='fPP:Decoration:numeroOAB']")
campo_oab.send_keys(numero_oab)
# Seleção do estado
dropdown_estados = nav.find_element(By.XPATH, "//select[@id='fPP:Decoration:estadoComboOAB']")
opcoes_estados = Select(dropdown_estados)
opcoes_estados.select_by_visible_text('PE')
# Click em pesquisar
botao_pesquisar = nav.find_element(By.XPATH, "//input[@id='fPP:searchProcessos']")
botao_pesquisar.click()
sleep(10)


# Configuranção do racaptch

# chave_captcha = navegador.find_element(By.ID, 'recaptcha-demo').get_attribute('data-sitekey')

solver = recaptchaV3Proxyless()
solver.set_verbose(0)
#solver.set_key(chave_api)
solver.set_website_url(link)
solver.set_website_key(chave_cap)

resposta = solver.solve_and_return_solution()

if resposta and 'g-recaptcha-response' in resposta:
    print(resposta)
    # Preencher o campo do token do captcha
    # g-recaptcha-response
    token = resposta['g-recaptcha-response']
    nav.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{token}';")
    nav.find_element(By.ID, 'recaptcha-verify-button').click()
else:
    print(solver.err_string)


# Ajuste o tempo de espera conforme necessário
time.sleep(50)



# Manter o navegador aberto

#while True:
    #time.sleep(30)

# Encerre o navegador quando terminar
nav.quit()