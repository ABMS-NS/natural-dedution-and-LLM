# Exemplo de uso
premissas_e_conclusao = "P → (Q ∧ R), P ⊢ P ∧ Q"
passos = """
1. P → (Q ∧ R) (Hipótese)
2. P (Hipótese)
3. Q ∧ R MP(1,2)
4. Q SP(3)
5. P ∧ Q CJ(2,4)
"""

valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)
print("Validação bem-sucedida!" if valido else "Erro(s) encontrado(s):")
print(feedback)


premissas_e_conclusao = "(P ∧ R) → Q, ¬Q ⊢ ¬(P ∧ R)"
passos = """
1. (P ∧ R) → Q (Hipótese)
2. ¬Q (Hipótese)
3. ¬(P ∧ R) MT(1,2)
"""

valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)
print("Validação bem-sucedida!" if valido else "Erro(s) encontrado(s):")
print(feedback)


# Definindo as premissas e a conclusão
premissas_e_conclusao = "P v Q, ¬P ⊢ Q"

# Definindo os passos da dedução
passos = """
1. P v Q (Hipótese)
2. ¬P (Hipótese)
3. Q SD(1,2)
"""

# Função de validação
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)

# Exibindo o resultado
print("Validação bem-sucedida!" if valido else "Erro(s) encontrado(s):")
print(feedback)


# Definindo as premissas e a conclusão
premissas_e_conclusao = "P \\lor Q, \\negP \\vdash Q"

# Definindo os passos da dedução
passos = """
1. P \\lor Q (Hipótese)
2. \\negP (Hipótese)
3. Q SD(1,2)
"""

# Função de validação
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)

# Exibindo o resultado
print("Validação bem-sucedida!" if valido else "Erro(s) encontrado(s):")
print(feedback)


# Definindo as premissas e a conclusão
premissas_e_conclusao = "(A \\lor B) \\land (C \\lor D), \\negA, \\negC \\vdash B \\land D"

# Definindo os passos da dedução
passos = """
1. (A \\lor B) \\land (C \\lor D) (Hipótese)
2. \\negA (Hipótese)
3. \\negC (Hipótese)
4. (A \\lor B) SP(1)
5. (C \\lor D) SP(1)
6. B SD(4,2)
7. D SD(5,3)
8. B \\land D CJ(6,7)
"""

# Função de validação
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)

# Exibindo o resultado
print("Validação bem-sucedida!" if valido else "Erro(s) encontrado(s):")
print(feedback)


premissas_e_conclusao = "(A → B), (B → C), ¬¬A ⊢ A → C"
passos = """
1. A → B (Hipótese)
2. B → C (Hipótese)
3. ¬¬A (Hipótese)
4. A DN(3)
5. B MP(1,4)
6. C MP(2,5)
7. A → C SH(1,2)
"""

# Função de validação
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)

# Exibindo o resultado
print("Validação bem-sucedida!" if valido else "Erro(s) encontrado(s):")
print(feedback)


# Definindo as premissas e a conclusão
premissas_e_conclusao = "P ⊢ P v Q"

# Definindo os passos da dedução
passos = """
1. P (Hipótese)
2. P v Q AD(1)
"""

# Função de validação
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)

# Exibindo o resultado
print("Validação bem-sucedida!" if valido else "Erro(s) encontrado(s):")
print(feedback)


# Definindo as premissas e a conclusão
premissas_e_conclusao = "P → Q, Q → R, P ⊢ R v S"

# Definindo os passos da dedução
passos = """
1. P → Q (Hipótese)
2. Q → R (Hipótese)
3. P (Hipótese)
4. Q MP(1,3)
5. R MP(2,4)
6. R v S AD(5)
"""

# Função de validação
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)

# Exibindo o resultado
print("Validação bem-sucedida!" if valido else "Erro(s) encontrado(s):")
print(feedback)



# Definindo as premissas e a conclusão
premissas_e_conclusao = "(P → ¬Q) v R, (P → ¬Q) → ¬¬Q, R → ¬¬Q ⊢ ¬¬Q"

# Definindo os passos da dedução
passos = """
1. (P → ¬Q) v R (Hipótese)
2. (P → ¬Q) → ¬¬Q (Hipótese)
3. R → ¬¬Q (Hipótese)
4. ¬¬Q vE(1,2,3)
"""

# Função de validação
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)

# Exibindo o resultado
print("Validação bem-sucedida!" if valido else "Erro(s) encontrado(s):")
print(feedback)


# Definindo as premissas e a conclusão
premissas_e_conclusao = "(P ∧ ¬Q) → R, R → (P ∧ ¬Q) ⊢ (P ∧ ¬Q) ↔ R"

# Definindo os passos da dedução
passos = """
1. (P ∧ ¬Q) → R (Hipótese)
2. R → (P ∧ ¬Q) (Hipótese)
3. (P ∧ ¬Q) ↔ R ↔I(1,2)
"""

# Função de validação
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)

# Exibindo o resultado
print("Validação bem-sucedida!" if valido else "Erro(s) encontrado(s):")
print(feedback)



# Definindo as premissas e a conclusão
premissas_e_conclusao = "(P ∧ ¬Q) ↔ R ⊢ (P ∧ ¬Q) → R, R → (P ∧ ¬Q)"

# Definindo os passos da dedução
passos = """
1. (P ∧ ¬Q) ↔ R (Hipótese)
2. (P ∧ ¬Q) → R ↔E(1)
3. R → (P ∧ ¬Q) ↔E(1)
"""

# Função de validação
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)

# Exibindo o resultado
print("Validação bem-sucedida!" if valido else "Erro(s) encontrado(s):")
print(feedback)


# Definição das premissas e conclusão
premissas_e_conclusao = "A → (B v C), ¬B ⊢ A → C"

# Definição dos passos da dedução
passos = '''
1. A → (B v C) (Hipótese)
2. ¬B (Hipótese)
3. A (Hip-PC)
4. B v C MP(1,3)
5. C SD(4,2)
6. A → C PC(3-5)
'''

# Chamando o validador
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)

# Exibindo o resultado
print("Validação bem-sucedida!" if valido else "Erro(s) encontrado(s):")
print(feedback)

# Definindo as premissas e a conclusão
premissas_e_conclusao = "¬Q, P → Q ⊢ ¬P"

# Definindo os passos da dedução
passos = """
1. ¬Q (Hipótese)
2. P → Q (Hipótese)
3. P (Hip-RAA)
4. Q MP(2,3)
5. Q ∧ ¬Q CJ(1,4)
6. ¬P RAA(3-5)
"""

# Função de validação
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)

# Exibindo o resultado
print("Validação bem-sucedida!" if valido else "Erro(s) encontrado(s):")
print(feedback)


# Definindo as premissas e a conclusão
premissas_e_conclusao = "P v Q ⊢ Q v P"

# Definindo os passos da dedução
passos = """
1. P v Q (Hipótese)
2. Q v P COM(1)
"""

# Função de validação
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)

# Exibindo o resultado
print("Validação bem-sucedida!" if valido else "Erro(s) encontrado(s):")
print(feedback)

# Definindo as premissas e a conclusão
premissas_e_conclusao = "¬(P v Q) ⊢ ¬P ∧ ¬Q"

# Definindo os passos da dedução
passos = """
1. ¬(P v Q) (Hipótese)
2. ¬P ∧ ¬Q DMOR(1)
"""

# Função de validação
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)

# Exibindo o resultado
print("Validação bem-sucedida!" if valido else "Erro(s) encontrado(s):")
print(feedback)


# Definindo as premissas e a conclusão
premissas_e_conclusao = "P → Q ⊢ ¬P v Q"

# Definindo os passos da dedução
passos = """
1. P → Q (Hipótese)
2. ¬P v Q COND(1)
"""

# Função de validação
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)

# Exibindo o resultado
print("Validação bem-sucedida!" if valido else "Erro(s) encontrado(s):")
print(feedback)



# Definindo as premissas e a conclusão
premissas_e_conclusao = "¬(P → Q) ⊢ ¬(¬P v Q)"

# Definindo os passos da dedução
passos = """
1.¬(P → Q) (Hipótese)
2. ¬(¬P v Q) COND(1)
"""

# Função de validação
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)

# Exibindo o resultado
print("Validação bem-sucedida!" if valido else "Erro(s) encontrado(s):")
print(feedback)



premissas_e_conclusao = "¬(P v Q) ⊢ ¬P ∧ ¬Q"
passos = """
1. ¬(P v Q) (Hipótese)
2. ¬P ∧ ¬Q DMOR(1)
"""
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)
print(feedback)

premissas_e_conclusao = "¬(P ∧ Q) ⊢ ¬P v ¬Q"
passos = """
1. ¬(P ∧ Q) (Hipótese)
2. ¬P v ¬Q DMOR(1)
"""
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)
print(feedback)

premissas_e_conclusao = "¬(¬P v Q) ⊢ P ∧ ¬Q"  # Exemplo com negação dupla
passos = """
1. ¬(¬P v Q) (Hipótese)
2. P ∧ ¬Q DMOR(1)  
"""
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos) # A regra de De Morgan não se aplica diretamente a negações duplas.
print(feedback)


# Definindo as premissas e a conclusão
premissas_e_conclusao = "(p → q) → r, (r v s) → ¬t, t ⊢ ¬q"

# Definindo os passos da dedução
passos = """
1. (p → q) → r (Hipótese)
2. (r v s) → ¬t (Hipótese)
3. t (Hipótese)
4. q (Hip-RAA)
5. ¬(r v s) MT(2,3)
6. ¬r ∧ ¬s DMOR(5)
7. ¬r SP(6)
8. ¬(p → q) MT(1,7)
9. ¬(¬p v q) COND(8)
10. p ∧ ¬q DMOR(9)
11. ¬q SP(10)
12. q ∧ ¬q CJ(4,11)
13. ¬q RAA(4-12)
"""

# Função de validação
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)

# Exibindo o resultado
print("Validação bem-sucedida!" if valido else "Erro(s) encontrado(s):")
print(feedback)


premissas_e_conclusao = "(P ∧ R) → Q, ¬Q ⊢ ¬(P ∧ R)"
passos = """
1. (P ∧ R) → Q (Hipótese)
2. ¬Q (Hipótese)
3. ¬(P ∧ R) MT(1,2)
"""
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)
print(feedback)

premissas_e_conclusao = "(p → q) → r , ¬r ⊢ ¬(p → q)"
passos = """
1. (p → q) → r (Hipótese)
2. ¬r (Hipótese)
3. ¬(p → q) MT(1,2)
"""
valido, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)
print(feedback)
