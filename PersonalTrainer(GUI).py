import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome},faça 3-5 séries com 10-15 repetições,com um descanso de 30 segundos a 1 minuto e meio,utilize cargas médias  {os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome},faça 6-10 séries com 5-6 repetições,com um descanso de 2 a 5 minutos,utilize cargas altas {os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome},faça 3-10 séries com 1-10 repetições,com um descanso de 2 a 3 minutos,utilize cargas medio-baixas,faça os movimentos de flexão rapidamente e de relaxamento lentamente {os.linesep}')    
    elif resposta == '4':
        print(f'{os.linesep}{nome},faça 2-5 séries de 15-45 repetições,com um descanso de 30 segundos até 2 minutos,utilize cargas baixas {os.linesep}')
    elif resposta == '5':
        print(f'{os.linesep}{nome},pouco mais de 10 minutos de cario na esteira,bicileta ou escada é o suficiente para afastar o sedentarismo,dependendo da intensidade das sessões e do nível de treino e resistência de cada indivíduo podem ir de 30 minutos até 1 hora{os.linesep}') 
    if resposta == '6':
        print(f'Segundo os profissionais, essa resposta depende de diversos fatores: Sua meta, alimentação, frequência e intensidade dos treinos. De acordo com a ciência, em um intervalo de 8 a 12 semanas já é possível ter um resultado expressivo quando o assunto é o físico{os.linesep}')
    else:
        print('Digite apenas as opções 1, 2, 3 ,4 ou 5')    


def start():

    print('Olá,Bem vindo(a)!,sou Gui,seu Personal-Trainer virtual')

    
    nome = input('Digite seu nome: ')
    
    while True:

        
        resposta = input(
            f'O que gostaria de saber hoje?{os.linesep}[1] - Como montar um treino de hipertrofia?{os.linesep}[2] - Como aumentar a força atravéz da musculação?{os.linesep}[3] - Como melhorar a potência muscular?{os.linesep}{os.linesep}[4] - Como mantar um treino de definição e resistência muscular?{os.linesep}[5] - Quanto tempo ficar no cardio?{os.linesep}[6] - Em quanto tempo os resultados dos treinos costumam aparecer?{os.linesep}')
        
        
        processar_resposta(resposta, nome)


if __name__ =='__main__':
    start()