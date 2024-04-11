#Fazer uma altomação para o questionario de crenças de transtonor de personalidade de forma reduzida 
#para ter o resultado é preciso Somar as respostas de X questões por personalidade 
#cada personalidade é subtraido por um numero e depois subtraido por outro
# EVITATIVO SÃO AS PERGUNTAS (1, 2, 5, 31, 33, 39, 43) - 10,86/ 6,46 =
# DEPENDENTE SÃO AS PERGUNTAS (15, 18, 44, 45, 56, 62, 63) - 9,26 /6,12 =
# PERSONALIDADE PASSIVO AGRESSIVO SÃO AS PERGUNTAS (4, 7, 20, 21, 41, 47, 51) - 8,90/ 5,97
# OBSESSIVO COMPULSIVO SÃO AS PERGUNTAS (6, 9, 11, 19, 30, 40, 57) - 10,56 /7,20
# ANTISSOCIAL SÃO AS PERGUNTAS (23, 32, 35, 38, 42, 59, 61) - 4,25 /4,30
# NARCISISTA SÃO AS PERGUNTAS (10, 16, 26, 27, 46, 58, 60) - 3,42 /4,23
# ESQUIZOIDE SÃO AS PERGUNTAS (12, 25, 28 ,29, 36, 50, 53) - 8,99 /5,60
# PARANOIDE SÃO AS PERGUNTAS (3, 13, 14, 17, 24, 28, 49) - 6,99 /6,22
# BODERLINE SÃO AS PERGUNTAS (31, 44, 45, 49, 56, 64, 65) - 8,07 /6,05

def fazer_questionario():
    respostas = []
    perguntas = [
        "Ser exposto como inferior é algo intolerável para mim.",
        "Eu deveria evitar situações desagradáveis a todo custo.",
        "Se as pessoas agem de maneira amistosa talvez estejam tentando me usar ou me explorar.",
        "Tenho que resistir a dominação das autoridades mas, ao mesmo tempo manter sua aprovação e atenção.",
        "Não consigo tolerar sentimentos desagradáveis.",
        "Falhas, defeitos ou erros são intoleráveis.",
        "Outras pessoas são frequentemente muito exigentes.",
        "Eu deveria ser o centro das atenções.",
        "Se eu não tiver sistematização, tudo irá ruir.",
        "É intolerável que eu não receba respeito que me é devido ou que me é direito.",
        "É importante fazer tudo perfeito.",
        "Gosto mais de fazer as coisas sozinho do que com outras pessoas.",
        "As pessoas tentaram me usar ou me manipular se eu não tomar cuidado.",
        "As pessoas possuem motivos escusos.",
        "A pior coisa que poderia me acontecer é ser abandonado.",
        "As outras pessoas devem saber que eu sou especial.",
        "Os outros vão deliberadamente querer me prejudicar.",
        "Preciso de outras pessoas para tomar decisões ou dizer o que devo fazer.",
        "Os detalhes são extremamente importantes.",
        "O fato de eu achar que alguém é muito autoritário me dá o direito de desrespeitar suas ordens.",
        "Figuras de autoridades tendem a ser intrusivas, exigentes, intrometidas e controladoras.",
        "A maneira para conseguir o que eu quero é fascinar ou divertir as pessoas.",
        "Devo fazer tudo o que puder para não ser descoberto.",
        "Se os outros descobrirem coisas a meu respeito, eles poderão usar isso contra mim.",
        "Relacionamentos são confusos e complicados e interferem na liberdade.",
        "Como sou uma pessoa superior, mereço tratamento e privilégios especiais.",
        "É importante para mim me sentir livre e independente de outras pessoas.",
        "Em muitas situações, prefiro ficar sozinho.",
        "É necessário fixar sempre o padrão mais elevado ou as coisas vão ruir.",
        "Sentimentos desagradáveis podem aumentar e fugir do meu controle.",
        "Vivemos em uma selva e sobrevive quem for mais forte.",
        "Eu deveria evitar situações nas quais poderia atrair atenção ou ser o mais imperceptível possível.",
        "Se eu não mantiver os outros envolvidos comigo, eles não vão gostar de mim.",
        "Quando quero alguma coisa, devo fazer o que for necessário para consegui-la.",
        "É melhor se sentir sozinho do que preso às outras pessoas.",
        "Não sou nada, a menos que eu entretenha ou impressione as pessoas.",
        "As pessoas vão me atacar se eu não as atacar primeiro.",
        "Qualquer sinal de tensão em um relacionamento indica que a relação vai mal e que eu deveria encerrá-la.",
        "Se eu não tiver um desempenho no mais alto nível, falharei.",
        "Cumprir prazos, ceder às exigências e me enquadrar ferem diretamente meu orgulho e minha autossuficiência.",
        "Fui injustiçado e me sinto autorizado a cobrar meus direitos, não importando a maneira que eu faça isso.",
        "Se as pessoas se aproximarem de mim, descobriram quem realmente sou e me rejeitarão.",
        "Sou carente e frágil.",
        "Sou indefeso quando sou deixado por conta própria.",
        "As outras pessoas devem satisfazer minhas necessidades.",
        "Se eu seguir as regras da maneira que as pessoas esperam, isso inibirá minha liberdade de ação.",
        "Pessoas irão me explorar se eu der a elas a chance.",
        "Tenho que estar atento na defensiva, a todo instante.",
        "Minha privacidade é mais importante para mim do que estar com as pessoas.",
        "Regras são arbitrárias e me paralisam.",
        "É horrível quando as pessoas me ignoram.",
        "O que as pessoas pensam não importa.",
        "Para ser feliz, preciso que as outras pessoas prestem atenção em mim.",
        "Se entretenho as pessoas, elas não irão perceber minhas fraquezas.",
        "Preciso de alguém ao meu redor disponível a todo momento para me ajudar.",
        "Qualquer defeito ou falha no desempenho pode levar a uma catástrofe.",
        "Como sou muito talentoso, as pessoas deveriam fazer de tudo para promover minha carreira.",
        "Se eu não explorar os outros, eles me explorarão.",
        "Não preciso seguir as mesmas regras que são aplicadas às outras pessoas.",
        "A melhor maneira de conseguir as coisas é por meio da força e da esperteza.",
        "Devo me manter acessível para meu/minha companheiro/a o tempo todo.",
        "Sou preferencialmente uma pessoa só a menos que eu possa me ligar a alguém mais forte.",
        "Não posso confiar nas pessoas.",
        "Não consigo enfrentar situações com outras pessoas."
    ]
    for i, pergunta in enumerate(perguntas, start=1):
        resposta = input(f"Digite a resposta (0 a 4) para a pergunta {i}: {pergunta} ")
        while not resposta.isdigit() or int(resposta) < 0 or int(resposta) > 4:
            resposta = input("Por favor, digite um número entre 0 e 4: ")
        respostas.append(int(resposta))
    return respostas

def calcular_personalidade(respostas):
    evitativo = (sum([respostas[i] for i in [0, 1, 4, 30, 32, 38, 42]]) - 10.86) / 6.46
    dependente = (sum([respostas[i] for i in [14, 17, 32, 35, 43, 49, 50]]) - 9.26) / 6.12
    passivo_agressivo = (sum([respostas[i] for i in [3, 6, 18, 19, 39, 45, 47]]) - 8.90) / 5.97
    obsessivo_compulsivo = (sum([respostas[i] for i in [5, 8, 9, 16, 27, 37, 44]]) - 10.56) / 7.20
    antissocial = (sum([respostas[i] for i in [21, 29, 34, 36, 40, 54, 56]]) - 4.25) / 4.30
    narcisista = (sum([respostas[i] for i in [7, 15, 24, 25, 46, 53, 55]]) - 3.42) / 4.23
    esquizoide = (sum([respostas[i] for i in [11, 23, 26, 28, 33, 48, 51]]) - 8.99) / 5.60
    paranoide = (sum([respostas[i] for i in [2, 12, 13, 20, 22, 31, 41]]) - 6.99) / 6.22
    borderline = (sum([respostas[i] for i in [10, 47, 52, 57, 58, 59, 60]]) - 8.07) / 6.05
    
    personalidades = {
        "Evitativo": evitativo,
        "Dependente": dependente,
        "Passivo Agressivo": passivo_agressivo,
        "Obsessivo Compulsivo": obsessivo_compulsivo,
        "Antissocial": antissocial,
        "Narcisista": narcisista,
        "Esquizoide": esquizoide,
        "Paranoide": paranoide,
        "Borderline": borderline
    }
    
    return personalidades

def main():
    print("Bem-vindo ao questionário de personalidade reduzido!")
    print("Por favor, responda às seguintes perguntas de 0 a 4.")
    print("0 - Discordo totalmente, 1 - Discordo, 2 - Neutro, 3 - Concordo, 4 - Concordo totalmente")
    respostas = fazer_questionario()
    personalidades = calcular_personalidade(respostas)
    
    print("\nResultados:")
    for personalidade, valor in personalidades.items():
        print(f"{personalidade}: {valor:.2f}")

if __name__ == "__main__":
    main()


