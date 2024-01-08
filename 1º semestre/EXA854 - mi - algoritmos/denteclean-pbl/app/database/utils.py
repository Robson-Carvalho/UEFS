import os
import json

diretorioAtual = os.path.dirname(os.path.abspath(__file__))
caminhoArquivoSessoes = os.path.join(diretorioAtual, 'sessions.json')
caminhoArquivoPacientes = os.path.join(diretorioAtual, 'patients.json')

def SalvarSessaoBancoDeDados(sessoes):
    if sessoes:
        try:
            with open(caminhoArquivoSessoes, 'w') as file:
                json.dump([sessao.__dict__ for sessao in sessoes], file)
                return 1
        except:
            return 2
    else:
        return 3

def LerSessoesBancoDeDados(Sessao):
    try:
        with open(caminhoArquivoSessoes, 'r') as file:
            sessoes = json.load(file)
        resultado = [Sessao(**sessao) for sessao in sessoes]
        return resultado
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        return []

def SalvarPacienteBancoDeDados(pacientes):
    if pacientes:
        try:
            with open(caminhoArquivoPacientes, 'w') as file:
                json.dump([paciente.__dict__ for paciente in pacientes], file)
                return 1
        except:
            return 2
    else:
        return 3

def LerPacienteBancoDeDados(Paciente):
    try:
        with open(caminhoArquivoPacientes, 'r') as file:
            pacientes = json.load(file)
        resultado = [Paciente(**paciente) for paciente in pacientes]
        return resultado
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        return []
