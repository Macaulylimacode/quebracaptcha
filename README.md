# QUEBRACAPTCHA



[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Macaulylimacode/quebracaptcha/blob/master/LICENSE) 





# Informações do Projeto:
### Project Information:

Projeto PJE, Foi solcitado uma automação no qual não parece no captcha de preteção do próprio site.
Nesse Códigp fonte contém o preenchimento automático do número da OAB além da sigla do estado
no qual ele está a origem da carteria dele. Foi usado a API ```bash anti-captcha.com/ ```
Lembre-se de acessar o arquivo CHAVE > CHAVE_API, o mesmo foi retriado do código fonte pós é de uso pessoal.
Crie sua conta no AntiCaptcha, recarregue e aproveite.

Project PJE, An automation was requested in which it does not appear in the protection captcha of the site itself.
This source Code contains the automatic completion of the OAB number in addition to the state abbreviation
in which he is the origin of his carteria. API was used ```bash anti-captcha.com/ ```
Remember to access the CHAVE > CHAVE_API file, it was retrieved from the post source code and is for personal use.
Create your AntiCaptcha account, recharge and enjoy.

# ATENÇÃO:
### ATTENTION:
```bash
Use com responsabilidade essa função de quebra captcha fica por sua responsabilidade qualquer o uso.
Responsibly use this function to break captcha, any use is your responsibility.
```
# EXTRA:
Projeto finalizou quando o captcha foi quebrado. Esse projeto da abertura para fazer muito mais ex: baixar relatório, navegar entre páginas etc.
Project ended when the captcha was broken. This project allows you to do much more, eg: download reports, navigate between pages, etc.

# Preview do projeto:
### Project preview:

![1](https://github.com/Macaulylimacode/quebracaptcha/assets/139823222/cc3e6ced-af5c-4967-97ab-5fe4d1b09033)

![Captura de tela 2023-09-09 080223](https://github.com/Macaulylimacode/quebracaptcha/assets/139823222/48d1b736-d346-456f-b512-a4ae586571e8)

![Captura de tela 2023-09-09 080258](https://github.com/Macaulylimacode/quebracaptcha/assets/139823222/39008da8-21b8-4a2e-969b-c952057a5dba)

![Captura de tela 2023-09-09 081428](https://github.com/Macaulylimacode/quebracaptcha/assets/139823222/679655ea-3e4d-46df-87d2-7bdd14b8378e)

![final](https://github.com/Macaulylimacode/quebracaptcha/assets/139823222/673ff447-a42d-4a88-b812-720f4fca1d25)


# Tecnologias utilizadas:
### Technologies used:

![PY](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Trechos do Código:
### code snippets:

```bash
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
```

```bash
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

```
# BIBLIOTECAS:
### LIBRARIES:
° Selenium
° Webdriver
° Anticapychaoffcial

# CAPTCHA QUEBRADO:
### BROKEN CAPTCHA:

°recaptchav3proxyless

## IDE

![pycharm](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)
![visual](https://img.shields.io/badge/Visual_Studio-5C2D91?style=for-the-badge&logo=visual%20studio&logoColor=white)

# Como executar o projeto

```bash
# clonar repositório
git clone https://github.com/Macaulylimacode/quebracaptcha

# entrar na pasta do projeto
cd quebracaptcha

# executar o projeto
./mvnw spring-boot:run
```

# Autor

Macauly lima

[![linkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/macauly-lima-75984a269)
