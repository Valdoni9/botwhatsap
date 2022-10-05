from selenium import webdriver

class Whatsappbot:
    def _init_(self):
        self.mensagem = "Bom dia"
        self.grupos = ["GRUPO"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagem(self):
        