# Chatbot Simples com Python e Gemini API

Este projeto consiste em um **chatbot em Python** que utiliza a **API do Google Gemini** para gerar respostas curtas e objetivas a partir da entrada do usuário via terminal.

## 📌 Visão Geral

O objetivo deste projeto foi criar um chatbot simples para:
- Explorar a integração entre Python e IA generativa
- Entender o funcionamento de prompts de sistema
- Controlar o formato e tamanho das respostas geradas pelo modelo

O chatbot funciona em loop no terminal e é encerrado quando o usuário digita `endchat`.

## 🛠️ Tecnologias Utilizadas

- Python
- Google Gemini API
- Modelo: `gemini-2.5-flash-lite`
- Programação em linha de comando (CLI)

## ⚙️ Funcionalidades

- [x] Entrada de texto pelo usuário via terminal
- [x] Geração de respostas com IA generativa
- [x] Uso de *system instruction* para limitar respostas
- [x] Respostas em apenas uma linha
- [x] Encerramento do chat por comando (`endchat`)

## 📂 Estrutura do Projeto

```text
📁 chatbot-gemini
 ┣ 📄 main.py
 ┗ 📄 README.md
