# Projeto QR Code e Envio de E-mail

Este projeto consiste em um programa Python que gera um código QR com base nos dados inseridos pelo usuário. O programa também envia um e-mail contendo o código QR gerado como anexo.

## Funcionalidades

1. **Geração do Código QR**

   - A função `make_qrcode(dados)` cria um código QR usando a biblioteca `qrcode` com base nos dados fornecidos.
   - O arquivo do código QR é salvo no diretório do projeto.
2. **Envio de E-mail**

   - A função `make_message()` solicita ao usuário dados para gerar o código QR.
   - Em seguida, ela utiliza a função `make_qrcode` para criar o código QR com base nos dados inseridos.
   - Um e-mail é construído usando a biblioteca `smtplib` e `email`, com o código QR anexado.
   - O programa lê as informações de login (e-mail e senha) de um arquivo JSON (`password.json`).
   - O e-mail é enviado usando o servidor SMTP do Gmail.

## Como Utilizar

1. Execute o arquivo `main.py`.
2. Insira os dados quando solicitado.
3. O código QR será gerado e salvo no diretório do projeto.
4. Um e-mail será enviado com o código QR como anexo para o endereço de e-mail especificado no código.

**Observação:** Certifique-se de ter configurado corretamente as informações de login no arquivo `password.json` e permitido o acesso de aplicativos menos seguros na conta do Gmail (caso necessário).

## Requisitos

- Python 3.x
- Bibliotecas: `qrcode`, `smtplib`, `email`

```bash
pip install qrcode  # Para a biblioteca qrcode
```

## Configuração do E-mail

1. Edite o arquivo `password.json` e insira as informações de login do seu e-mail.
2. Se necessário, habilite o acesso a aplicativos menos seguros em sua conta do Gmail: [Acessar a página de segurança do Google](https://myaccount.google.com/security-checkup).

## Notas

- Este projeto foi desenvolvido como uma demonstração simples e pode precisar de ajustes para uso em ambientes de produção.
- Certifique-se de usar as informações de login e e-mail de forma segura e conforme as políticas de segurança recomendadas.
