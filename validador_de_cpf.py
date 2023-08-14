import re

################ validação do input
qtd_max_caracteres = 11
while True:
    cpf_enviado_usuario = input('Digite o seu CPF: ')

    for caracteres in cpf_enviado_usuario: 
        if caracteres == "." or caracteres == "-": # se o caracteres for "." ou "-", aumenta o maximo de caracteres possíveis 
            qtd_max_caracteres += 1
        else:
            continue

    if len(cpf_enviado_usuario) > qtd_max_caracteres or len(cpf_enviado_usuario) < 11: # validando se tem 11 digitos ou 14 (se o usuário digitou "." e/ou "-")
        print('O CPF precisa ter 11 digítos.')
        continue

    caractere_repetido = cpf_enviado_usuario[0] * 11 in cpf_enviado_usuario
    if caractere_repetido:
        print('Não pode ter dígitos repetidos.')
        continue

    
    cpf = re.sub( # substituindo tudo que não for número no cpf_enviado_usuario por espaço vazio
        r'[^0-9]',
        '',
        cpf_enviado_usuario
    )
    if cpf == '': # se não foi digitado números no cpf, é barrado aqui e volta pro começo
        print('Você deve digitar números.')
        continue
    else:
        break

################ calcular o primeiro digito do cpf
primeiro_digito_cpf = 0
contagem_regressiva_primeiro_digito = 10
cpf_9_digitos = cpf[:9]
# 746.824.890-70
for digitos in cpf_9_digitos:
    primeiro_digito_cpf += ( int(digitos) * contagem_regressiva_primeiro_digito) # multiplicando cada digito pelo número da contagem regressiva e somando todos os resultados da multiplicação
    contagem_regressiva_primeiro_digito -= 1

primeiro_digito_cpf = (primeiro_digito_cpf * 10) % 11 # multiplicando a soma da multiplicação e obtendo o resto da divisão desse número por 11
primeiro_digito_cpf = primeiro_digito_cpf if primeiro_digito_cpf <= 9 else 0

print(f'O primeiro dígito do CPF é : {primeiro_digito_cpf}')

################ calcular o segundo digito do cpf
segundo_digito_cpf = 0
contagem_regressiva_segundo_digito = 11
cpf_10_digitos = cpf_9_digitos + str(primeiro_digito_cpf)

for digitos in cpf_10_digitos:
    segundo_digito_cpf += (int(digitos) * contagem_regressiva_segundo_digito)
    contagem_regressiva_segundo_digito -= 1

segundo_digito_cpf = (segundo_digito_cpf * 10) % 11
segundo_digito_cpf = segundo_digito_cpf if segundo_digito_cpf <= 9 else 0

print(f'O segundo dígito do CPF é: {segundo_digito_cpf}')

################ validando o cpf digitado
cpf_gerado_pelo_sistema = f'{cpf[:9]}{primeiro_digito_cpf}{segundo_digito_cpf}'

if cpf == cpf_gerado_pelo_sistema:
    print(f'{cpf} é um CPF válido')
else:
    print(f'{cpf} é um CPF inválido')
    print(f'Esse seria um CPF válido com dígitos do CPF que foi digitado: {cpf_gerado_pelo_sistema}')
