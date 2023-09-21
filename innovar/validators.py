from datetime import datetime

def is_valid_age(date_of_birth):
    # Converta a data de nascimento para um objeto de data
    try:
        birth_date = datetime.strptime(date_of_birth, '%Y-%m-%d')
    except ValueError:
        return False

    # Calcule a idade com base na data de nascimento
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    # Verifique se a idade está dentro do intervalo desejado
    return 13 <= age <= 100
def is_valid_cpf(cpf):
    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcula o primeiro dígito verificador
    total = 0
    for i in range(9):
        total += int(cpf[i]) * (10 - i)
    remainder = total % 11
    if remainder < 2:
        digit = 0
    else:
        digit = 11 - remainder

    # Verifica o primeiro dígito verificador
    if int(cpf[9]) != digit:
        return False

    # Calcula o segundo dígito verificador
    total = 0
    for i in range(10):
        total += int(cpf[i]) * (11 - i)
    remainder = total % 11
    if remainder < 2:
        digit = 0
    else:
        digit = 11 - remainder

    # Verifica o segundo dígito verificador
    if int(cpf[10]) != digit:
        return False

    return True
