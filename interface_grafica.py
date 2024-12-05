import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLabel, QTextEdit, QPushButton, 
    QWidget, QMessageBox, QGraphicsView, QGraphicsScene, QScrollArea
)
from PyQt5.QtGui import QFont, QPainter, QPixmap  # Importa QPainter e QPixmap
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtCore import Qt
from motor_inferencia import validar  # Importação do backend
import os


class SistemaDeDeducao(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Dedução Natural")
        self.resize(1200, 800)
        self.initUI()

    def initUI(self):
        # Layout principal
        main_layout = QVBoxLayout()

        # Entrada de prompt para a API do Qwen
        self.prompt_label = QLabel("Prompt para Qwen:")
        self.prompt_label.setFont(QFont("Arial", 12))
        self.prompt_field = QTextEdit()
        self.prompt_field.setPlaceholderText("Digite o prompt aqui...")
        main_layout.addWidget(self.prompt_label)
        main_layout.addWidget(self.prompt_field)

        # Botão para gerar resposta usando Qwen
        self.generate_button = QPushButton("Gerar Resposta")
        self.generate_button.setFont(QFont("Arial", 12))
        self.generate_button.clicked.connect(self.gerar_resposta)
        main_layout.addWidget(self.generate_button)

        # Área para exibição da resposta gerada
        self.generated_response_label = QLabel("Resposta Gerada:")
        self.generated_response_label.setFont(QFont("Arial", 12))
        main_layout.addWidget(self.generated_response_label)
        self.generated_response_area = QTextEdit()
        self.generated_response_area.setReadOnly(True)
        main_layout.addWidget(self.generated_response_area)

        # Entrada de premissas e conclusão
        self.input_label = QLabel("Premissas e Conclusão:")
        self.input_label.setFont(QFont("Arial", 12))
        self.input_field = QTextEdit()
        self.input_field.setPlaceholderText("Formato: P -> Q, Q -> R ⊢ P -> R")
        main_layout.addWidget(self.input_label)
        main_layout.addWidget(self.input_field)

        # Entrada de passos de dedução
        self.steps_label = QLabel("Passos da Dedução:")
        self.steps_label.setFont(QFont("Arial", 12))
        self.steps_field = QTextEdit()
        self.steps_field.setPlaceholderText(
            "Formato:\n1. P (Hipótese)\n2. P -> Q (Premissa)\n3. Q (MP, 1, 2)"
        )
        main_layout.addWidget(self.steps_label)
        main_layout.addWidget(self.steps_field)

        # Botão de validação
        self.validate_button = QPushButton("Validar Dedução")
        self.validate_button.setFont(QFont("Arial", 12))
        self.validate_button.clicked.connect(self.validar_deducao)
        main_layout.addWidget(self.validate_button)

        # Área para exibição de mensagens de validação
        self.result_label = QLabel("Resultado:")
        self.result_label.setFont(QFont("Arial", 12))
        main_layout.addWidget(self.result_label)
        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)
        main_layout.addWidget(self.result_area)

        # Área para exibição do gráfico SVG com QGraphicsView e QScrollArea
        self.svg_area = QScrollArea()
        self.svg_view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.svg_view.setScene(self.scene)
        self.svg_area.setWidget(self.svg_view)
        self.svg_area.setWidgetResizable(True)
        main_layout.addWidget(self.svg_area) # Adiciona a área de scroll ao layout

        # Widget principal
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)
   

    def gerar_resposta(self):
        prompt = self.prompt_field.toPlainText().strip()
        max_tokens = 2048  # Define o valor máximo de tokens

        if not prompt:
            QMessageBox.warning(self, "Erro", "Por favor, insira um prompt!")
            return

        try:
            response = requests.post(
                "http://localhost:8000/generate",
                json={"prompt": prompt, "max_tokens": max_tokens}  
            )
            response.raise_for_status()
            data = response.json()

            full_answer = data['answer']
            filtered_answer = full_answer.split("Explicação:")[0].strip()
            self.generated_response_area.setText(filtered_answer)

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Erro", f"Erro ao conectar com a API: {e}")


    def validar_deducao(self):
        premissas_e_conclusao = self.input_field.toPlainText().strip()
        passos = self.steps_field.toPlainText().strip()

        if not premissas_e_conclusao or not passos:
            QMessageBox.warning(self, "Erro", "Por favor, preencha todos os campos!")
            return

        try:
            resultado, feedback, caminho_grafo = validar(premissas_e_conclusao, passos)
            self.result_area.setText(feedback)

            if caminho_grafo and os.path.exists(caminho_grafo):
                self.scene.clear()
                renderer = QSvgRenderer(caminho_grafo)
                bounds = renderer.viewBoxF()  # Obtém as dimensões da viewbox do SVG
                pixmap = QPixmap(bounds.size().toSize()) # Cria um pixmap com o tamanho correto
                pixmap.fill(Qt.transparent) # Preenche com fundo transparente
                painter = QPainter(pixmap)
                renderer.render(painter)
                painter.end()
                item = self.scene.addPixmap(pixmap)
                self.scene.setSceneRect(bounds) # Define o retângulo da cena
                self.svg_view.fitInView(bounds, Qt.KeepAspectRatio)
            elif caminho_grafo:
                QMessageBox.warning(self, "Erro", "Arquivo SVG não encontrado.")

            if resultado:
                QMessageBox.information(self, "Validação", "Dedução válida!")
            else:
                QMessageBox.warning(self, "Validação", "Dedução inválida.")

        except Exception as e:
            QMessageBox.critical(self, "Erro", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SistemaDeDeducao()
    window.show()
    sys.exit(app.exec_())
