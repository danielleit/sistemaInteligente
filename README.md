# Analisador de Sinopse de Filmes

Este projeto utiliza uma API pré-treinada para analisar e classificar sinopses de filmes por gênero, além de medir a eficácia dessa classificação. A ferramenta permite que o usuário insira uma sinopse, receba o gênero previsto e verifique a precisão do sistema em um conjunto de dados predefinido.

## Índice
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Testes de Eficácia](#testes-de-eficácia)
- [Contribuição](#contribuição)

## Instalação

1. Clone este repositório para sua máquina local:
    ```bash
    git clone https://github.com/seu-usuario/analisador-de-sinopse.git
    cd analisador-de-sinopse
    ```

2. Instale as dependências do backend. O projeto utiliza **Python 3.7+** e o **Flask** para a integração com a API pré-treinada:
    ```bash
    pip install flask flask-cors
    ```

## Configuração

1. Certifique-se de que a API pré-treinada do GPT está disponível e configurada para receber requisições.
   
2. Defina a URL da API no código para garantir que as sinopses sejam enviadas para o endpoint correto.

3. Configure o banco de dados (se necessário) com a base de dados de sinopses de filmes para os testes de eficácia.

## Uso

1. **Inicie o servidor Flask**:
    ```bash
    python app.py
    ```

2. Abra o arquivo HTML no navegador para acessar o frontend. A interface permite inserir sinopses e visualizar o gênero previsto.

3. Insira uma sinopse de filme e clique em **Analisar** para obter o gênero previsto.

## Testes de Eficácia

Para calcular a precisão do modelo com base na base de dados:

1. Clique em **Testar Precisão do Sistema** na interface.
2. O sistema exibirá a precisão percentual com base nos resultados retornados pela API.

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para colaborar:

1. Faça um fork do repositório.
2. Crie uma nova branch com sua feature:
    ```bash
    git checkout -b minha-feature
    ```
3. Commit suas alterações:
    ```bash
    git commit -m 'Adiciona nova feature'
    ```
4. Faça o push para a branch:
    ```bash
    git push origin minha-feature
    ```
5. Abra um Pull Request.

---

Este README fornece uma visão geral completa para instalação, configuração, uso e contribuição ao projeto. Agradecemos seu interesse em melhorar o Analisador de Sinopse de Filmes!
