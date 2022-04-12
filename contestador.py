from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Edge() 
url = 'https://encuestasregresoseguro.com/'
sleeper = 4
sleepminus = sleeper / sleeper
deepsleep = sleeper * sleeper

def iniciar():
    #Entrar a la pagina
    driver.get(url)

def login():
    #Login
    #Tipo universidad
    unitype = Select(driver.find_element_by_id('tipoEscuela_id'))
    unitype.select_by_visible_text('Universidad Tecnológica')
    sleep(sleepminus)
    #Nombre universidad
    uniname = Select(driver.find_element_by_name('universidad'))
    uniname.select_by_visible_text('Universidad Tecnológica del Valle de Toluca')
    #Matricula
    matricula = driver.find_element_by_id('DNI')
    matricula.send_keys('222010638')
    #Contraseña
    password = driver.find_element_by_name('password')
    password.send_keys('Ismaken1612')
    #Intro
    entrar = driver.find_element_by_id('botonEnviar')
    entrar.click()

def encuesta():
    #Encuesta
    #Alteraciones Diarias
    #RadioDanger Par -> No; Inpar -> Si
    #Pregunta 1 de 17 (1, 2)
    pregunta1 = driver.find_element_by_xpath("//label[@for='radioDanger2']")
    pregunta1.click()
    #Pregunta 2 de 17 (3, 4)
    pregunta2 = driver.find_element_by_xpath("//label[@for='radioDanger4']")
    pregunta2.click()
    #Pregunta 3 de 17 (5, 6)
    pregunta3 = driver.find_element_by_xpath("//label[@for='radioDanger6']")
    pregunta3.click()
    #Pregunta 4 de 17 (7, 8)
    pregunta4 = driver.find_element_by_xpath("//label[@for='radioDanger8']")
    pregunta4.click()
    #Pregunta 5 de 17 (9, 10)
    pregunta5 = driver.find_element_by_xpath("//label[@for='radioDanger10']")
    pregunta5.click()
    #Pregunta 6 de 17 (11, 12)
    pregunta6 = driver.find_element_by_xpath("//label[@for='radioDanger12']")
    pregunta6.click()
    #Pregunta 7 de 17 (13, 14)
    pregunta7 = driver.find_element_by_xpath("//label[@for='radioDanger14']")
    pregunta7.click()
    #Pregunta 8 de 17 (15, 16)
    pregunta8 = driver.find_element_by_xpath("//label[@for='radioDanger16']")
    pregunta8.click()
    #Pregunta 9 de 17 (17, 18)
    pregunta9 = driver.find_element_by_xpath("//label[@for='radioDanger18']")
    pregunta9.click()
    #Pregunta 10 de 17 (19, 20)
    pregunta10 = driver.find_element_by_xpath("//label[@for='radioDanger20']")
    pregunta10.click()
    #Pregunta 11 de 17 (21, 22)
    pregunta11 = driver.find_element_by_xpath("//label[@for='radioDanger22']")
    pregunta11.click()
    #Pregunta 12 de 17 (23, 24)
    pregunta12 = driver.find_element_by_xpath("//label[@for='radioDanger24']")
    pregunta12.click()
    #Pregunta 13 de 17 (25, 26)
    pregunta13 = driver.find_element_by_xpath("//label[@for='radioDanger26']")
    pregunta13.click()
    #Pregunta 14 de 17 (27, 28)
    pregunta14 = driver.find_element_by_xpath("//label[@for='radioDanger28']")
    pregunta14.click()
    #Pregunta 15 de 17 (29, 30)
    pregunta15 = driver.find_element_by_xpath("//label[@for='radioDanger30']")
    pregunta15.click()
    #Pregunta 16 de 17 (31, 32)
    pregunta16 = driver.find_element_by_xpath("//label[@for='radioDanger32']")
    pregunta16.click()
    #Pregunta 17 de 17 (33, 34)
    pregunta17 = driver.find_element_by_xpath("//label[@for='radioDanger34']")
    pregunta17.click()
    #Siguiente
    siguiente = driver.find_element_by_link_text('Siguiente')
    siguiente.click()

    sleep(sleeper)

    #Informacion Estadistica
    #Enviar
    enviar = driver.find_element_by_css_selector('.btn.btn-info.float-right.send')
    enviar.click()

    sleep(sleeper)

    #Codigo
    #Ok
    ok = driver.find_element_by_css_selector('.swal2-confirm.swal2-styled')
    ok.click()

def codigo():
    #Ficha
    ficha = driver.find_element_by_css_selector('.btn.btn-success.d-none.d-md-inline-block.d-lg-inline-block.impficha')
    ficha.click()

def fin():
    driver.close()


iniciar()
sleep(sleeper)
login()
sleep(sleeper)
encuesta()
sleep(sleeper)
codigo()
sleep(deepsleep)
fin()