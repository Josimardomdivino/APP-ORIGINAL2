import gspread
import json
import os
from google.oauth2.service_account import Credentials

SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS = Credentials.from_service_account_info(
    json.loads(os.environ["credenciais.json"]), scopes=SCOPE
)

def get_sheet():
    try:
        cliente = gspread.authorize(CREDS)
        planilha = cliente.open("cadastro_socios")
        return planilha.sheet1
    except Exception as e:
        print("Erro ao acessar a planilha:", e)
        return None

def add_dado(nome, cpf, nascimento, comunidade, telefone, categoria):
    sheet = get_sheet()
    if sheet:
        dados_existentes = sheet.get_all_records()
        for linha in dados_existentes:
            if linha.get("cpf") == cpf:
                return  # evita duplicatas por CPF
        sheet.append_row([nome, cpf, nascimento, comunidade, telefone, categoria])

def listar_dados():
    sheet = get_sheet()
    if sheet:
        return sheet.get_all_records()
    return []