from selenium import webdriver
import time

driver = webdriver.Firefox()
link = "https://senaiweb6.fieb.org.br/FRAMEHTML/web/app/edu/PortalEducacional/login/"
driver.get(url=link)

time.sleep(1)
user = ""
senha = ""
# Encontrar o campo de usuário e preenchê-lo
campo_usuario = driver.find_element('xpath','/html/body/div[2]/div[3]/form/div[1]/input')
campo_usuario.send_keys(user)

# Encontrar o campo de senha e preenchê-lo
campo_senha = driver.find_element('xpath','/html/body/div[2]/div[3]/form/div[2]/input')
campo_senha.send_keys(senha)
time.sleep(1)
btn = driver.find_element('xpath','/html/body/div[2]/div[3]/form/div[4]/input')
btn.click()

time.sleep(60)

driver.quit()