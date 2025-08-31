from datetime import date

def calcular_idade(data_nascimento):
    if data_nascimento:
        hoje = date.today()
        return hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return None
