class Cadastro:

    def valida_email(self, email):
        if not self.email:
            raise ValueError("Você tem que escrever um email!")

        padrao_email = re.compile('(@escola.pr.gov.br)')
        match = padrao_email.match(email)
        if not match:
            raise ValueError("O email não é @escola.pr.gov.br ou não existe!.")

    @staticmethod
    def verifica_cgm(codigo_aluno_cgm):
        if len(codigo_aluno_cgm) == 8:
            return codigo_aluno_cgm
        else:
            raise ValueError("Quantidade de dígitos no seu CGM incorreta!")

    def faz_cgm_numero(self, codigo_aluno_cgm):
        if codigo_aluno_cgm.isdigit():
            return codigo_aluno_cgm
        else:
            raise ValueError("O CGM tem que ser um número!")
# Não consegui e não tive tempo para implementar as trilhas acima, mas
# resolvi deixar no código por motivos pessoais.
# Tampouco cumpri com o resto das características obrigatórias, tais quais:
# listar alunos de cada professor, alterar status, realizar trocas, entre outros.

alunos = []
professores = []

def matricula_alunos(alunos):
    print("Você está agora cadastrando um aluno: Ensira as seguintes informações: ")
    nome = input("Nome: ")
    turno = input("Qual turno: ")
    idade = int(input("Idade: "))
    email = input("Email @escola: ")
    turma = int(input("Turma (código da turma): "))
    cgm = int(input("Escreva seu CGM (código de identificação dos estudos): "))
    alunos.append((nome, turno, idade, email, turma, cgm))

def lista_alunos(alunos):
    for aluno in alunos:
        nome, turno, idade, email, turma, cgm = aluno
        print(f"Nome: {nome} /// Turno: {turno} /// Idade: {idade} /// Email: {email} /// Turma: {turma} /// CGM: {cgm}")

def matricula_professores(professores):
    print("Você está agora cadastrando um professor: Ensira as seguintes informações: ")
    nome = input("Nome: ")
    turno = input("Quais turnos: ")
    idade = int(input("Idade: "))
    email = input("Email @escola: ")
    turma = int(input("Insira suas turmas (código da turma): "))
    professores.append((nome, turno, idade, email, turma))

def lista_professores(professores):
    for professor in professores:
        nome, turno, idade, email, turma, cgm = professor
        print(f"Nome: {nome} /// Turno: {turno} /// Idade: {idade} /// Email: {email} /// Turma: {turma} /// CGM: {cgm}")

def menu_de_escolha():
    print(
        "1 - Cadastro de alunos \n"
        "2 - Cadastro de professores\n"
        "3 - Remover dados de pessoas já cadastradas\n"
        "4 - Listagem de já cadastrados\n"
    )
    escolha = int(input("Escolha uma das opções acima: "))

    if escolha == 1:
        matricula_alunos(alunos)
    elif escolha == 2:
        matricula_professores(professores)
    elif escolha == 3:
        escolhe_remover_alu_prof = int(input("1 - Alunos\n"
                                        "2 - Professores\n"
                                        "Escolha uma das opções acima: "))
        if escolhe_remover_alu_prof == 1:
            alunos.remove('')
        elif escolhe_remover_alu_prof:
            professores.remove('')

    elif escolha == 4:
        escolhe_alu_prof = int(input("1 - Alunos\n"
                                    "2 - Professores\n"
                                    "Escolha uma das opções acima: "))
        if escolhe_alu_prof == 1:
            lista_alunos(alunos)
        elif escolhe_alu_prof == 2:
            lista_professores(professores)


menu_de_escolha()
