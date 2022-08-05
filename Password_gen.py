import random
import PySimpleGUI as sg


class PassGen:
    def __init__(self):
        # LAYOUT DA LANELA
        sg.theme('DarkTeal5')
        #playsound('Coldplay-Paradise.mp3', block=False)
        layout = [
            [sg.Text('Site/Software', size=(10, 1)), sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/Usuário', size=(10, 1)), sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'),sg.Combo(values=list(range(30)), key='caracteres_totais', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]
        ]
        # GERANDO A JANELA
        self.janela = sg.Window('Garador de Senha').layout(layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WIN_CLOSED or evento == 'Cancel':
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)

    # CLICANDO EM GERAR SENHA

    def gerar_senha(self, valores):
        lista_de_caracteres = 'ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvxyz1234567890!@#$%¨&*()_-+=/?'
        caracteres = random.choices(lista_de_caracteres, k=int(valores['caracteres_totais']))
        nova_senha = ''.join(caracteres)
        return nova_senha




    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(f"\nSITE: {valores['site']},\nusuario: {valores['usuario']},\nnova senha:{nova_senha}")

        print('Arquivo salvo')

gen = PassGen()
gen.Iniciar()


