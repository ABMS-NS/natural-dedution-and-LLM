# Sistema Avaliador de Dedução Natural com Integração a LLMs

Este projeto implementa um sistema para avaliar a validade de argumentos lógicos usando dedução natural, com a opção de integrar a API de modelos de linguagem grandes (LLMs) para auxiliar na geração e verificação de passos. O projeto foi desenvolvido como um trabalho acadêmico em equipe na UFAL Instituto de Computação para a disciplina de Lógica Aplicada à Computação .

## Funcionalidades

* **Validação de Deduções:** Verifica se uma dedução lógica é válida com base nas regras de inferência fornecidas.
* **Visualização Gráfica:** Gera um grafo representando a estrutura da dedução, facilitando a compreensão dos passos e suas dependências.
* **Integração com LLMs:** Permite usar a API de modelos LLMs, como o Qwen, para auxiliar na geração de passos da dedução ou na verificação da validade dos passos fornecidos.
* **Interface Gráfica:** Uma interface gráfica intuitiva construída com PyQt5 facilita a interação com o sistema.

## Arquitetura

O projeto é composto pelos seguintes módulos:

* **`motor_inferencia.py`:** Contém a lógica principal para validar as deduções e gerar os grafos.
* **`qwen.py`:** Implementa uma API FastAPI que serve como interface para o modelo LLM Qwen. (Requer configuração adicional para funcionar).
* **`interface_grafica2.py`:** Fornece uma interface gráfica (GUI) construída com PyQt5 para interagir com o sistema. 

## Instalação

**Pré-requisitos:**

* Python 3.7+
* `pip` (gerenciador de pacotes Python)
* Graphviz (para geração de grafos)

**Passos:**

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/ABMS-NS/natural-dedution-and-LLM.git
   
Crie um ambiente virtual (recomendado):

python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows


## Instale as dependências:

pip install -r requirements.txt


## Instale o Graphviz (opcional, mas recomendado):


    Windows: Baixe o instalador MSI do site oficial do Graphviz (https://graphviz.org/download/) e execute-o. Certifique-se de adicionar o diretório bin do Graphviz à variável de ambiente PATH.

    macOS (usando Homebrew):

    brew install graphviz


## Linux (Debian/Ubuntu):

 sudo apt-get install graphviz




## Configuração da API LLM (Qwen)

Para usar a integração com o Qwen, você precisa:


    Obter um token de acesso da Hugging Face: Crie uma conta na Hugging Face e gere um token de acesso.

    Configurar a variável de ambiente HUGGING_FACE_API_TOKEN:


## Linux/macOS:

export HUGGING_FACE_API_TOKEN=seu_token


## Windows (cmd):

set HUGGING_FACE_API_TOKEN=seu_token


## Windows (PowerShell):

$env:HUGGING_FACE_API_TOKEN = "seu_token"





## Executar a API:

uvicorn qwen:app --reload



## Execução

## Sem a interface gráfica:

python motor_inferencia.py

## Com a interface gráfica:

python interface_grafica2.py


## Exemplos de Uso

Prompt para o Qween:

Dado o seguinte conjunto de premissas e uma conclusão, resolva por dedução natural e forneça os passos detalhados:

Premissas e Conclusão:
(P → Q), (Q → R), ¬¬P ⊢ P → R

Instruções:
1. Liste cada premissa como um passo inicial.
2. Use regras de inferência como Modus Ponens (MP), Dupla Negação (DN), e Silogismo Hipotético (SH) para deduzir a conclusão.
3. Formate cada passo da dedução como no exemplo abaixo:

Exemplo de Formato de Resposta:
1. P → Q (Hipótese)
2. Q → R (Hipótese)
3. ¬¬P (Hipótese)
4. P DN(3)
5. Q MP(1,4)
6. R MP(2,5)
7. P → R SH(1,2)

Por favor, forneça os passos da dedução natural de [premissas_e_conclusão]: 

Passos =
....

**Exemplo**
premissas_e_conclusao = (p → q) → r, (r v s) → ¬t, t ⊢ ¬q

Passos = 
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



* Insira as premissas e a conclusão no formato especificado.
* Insira os passos da dedução, um por linha, no formato: `Número. Proposição (Justificativa, premissas)`
* Execute o script para validar a dedução.

## Licença

Este projeto é licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Equipe

* Jean Felipe Duarte Tenório
* Alison Bruno Martires Soares
* Rian Rian Américo Brito da Silva
* Gustavo Romain Batista Carvalho
* Kalleb Felipe Melo de Oliveira
  


                
