import aluno

a1 = aluno.Aluno()
a1.set_nome(input("Qual seu nome?: "))
a1.set_n1(float((input("Qual foi sua primeira nota?: "))))
a1.set_n2(float((input("Qual foi sua segunda nota?: "))))

print(a1.show())
