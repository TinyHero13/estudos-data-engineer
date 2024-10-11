# Utilizando o UV para Instalação de Bibliotecas

## Por que usar o UV em vez do pip?

O UV é um pacote desenvolvido em Rust que proporciona uma instalação rápida e eficiente de bibliotecas, superando a performance do pip em muitos casos.

## Instalando o UV

Primeiro, precisamos instalar o UV. Você pode encontrar a [documentação completa](https://github.com/astral-sh/uv). A instalação pode ser feita utilizando `curl` no macOS ou Linux, PowerShell no Windows, ou ainda pelo pip: `pip install uv`.

## Criando um Novo Projeto

Para iniciar um novo projeto com o modelo do UV, execute o seguinte comando: `uv init novo_projeto`.

Se preferir, você pode iniciar diretamente no mesmo diretório utilizando apenas: `uv init`.

Após criar um novo diretório, navegue até ele: `cd novo_projeto`.

## Adicionando Pacotes

Agora, vamos adicionar pacotes ao nosso projeto. Por exemplo, para adicionar o Pandas, utilize o seguinte comando: `uv add pandas`.

Você verá o processo de instalação do Pandas.

## Verificando a Instalação dos Pacotes

Para conferir se o pacote foi instalado corretamente, use: `uv pip list`.

## Testando a Instalação do Pandas

Vamos testar a instalação do Pandas criando um arquivo chamado `hello.py` e adicionando o seguinte código:

``` python
import pandas as pd

df = pd.read_html('https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2024_-_S%C3%A9rie_A')[3]

print(df)
```

Esse código irá pegar os dados da tabela.

Após rodar o código, upara executar o script basta escrever: `uv run hello.py`.

Se tudo estiver correto, você verá a tabela exibida no seu terminal.

## Gerenciando Dependências

Com o UV, você não precisa criar um `requirements.txt` com `pip freeze`. O UV já gerencia as dependências automaticamente, armazenando-as no `pyproject.toml`, o que torna a publicação do projeto mais limpa e fácil para outros usuários.

## Recursos do UV

- 🚀 Uma única ferramenta que substitui pip, pip-tools, pipx, poetry, pyenv, virtualenv e mais.
- ⚡️ 10-100 vezes mais rápido que o pip.
- 🐍 Instala e gerencia versões do Python.
- 🛠️ Executa e instala aplicações Python.
- ❇️ Executa scripts de arquivo único, com suporte para metadados de dependência inline.
- 🗂️ Fornece gerenciamento abrangente de projetos, com um arquivo de bloqueio universal.
- 🔩 Inclui uma interface compatível com pip para um aumento de desempenho com uma CLI familiar.
- 🏢 Suporta espaços de trabalho no estilo Cargo para projetos escaláveis.
- 💾 Eficiente em espaço em disco, com um cache global para deduplicação de dependências.
- ⏬ Instalável sem Rust ou Python via curl ou pip.
- 🖥️ Suporta macOS, Linux e Windows.
