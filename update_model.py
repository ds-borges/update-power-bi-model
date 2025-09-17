import pyautogui
import time
from win10toast import ToastNotifier

pyautogui.PAUSE = 0.7
from plyer import notification

notification.notify(
    title="Atualização do PowerBi",
    message="Iniciando a atualização dos dados do PowerBi",
    timeout=1
)

#Abrindo o site do modelo semântico
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("https://app.powerbi.com/groups/me")
time.sleep(1)
pyautogui.press("enter")

#Acessando site do semantic model 
time.sleep(10)
pyautogui.click(x=678, y=494)
notification.notify(
    title="Atualização do PowerBi",
    message="Atualizando os dados",
    timeout=10
)
time.sleep(15)

#Encerrando a atualização
pyautogui.hotkey("ctrl","w")
notification.notify(
    title="Atualização do PowerBi",
    message="Atualização concluida",
    timeout=10
)

