📄 Descrição do Projeto


Este projeto implementa uma pipeline simples em Python para extrair, transformar e unificar dados de diferentes fontes (JSON e CSV). O objetivo principal é padronizar estruturas de dados distintas de duas empresas (Empresa A e Empresa B) e combiná-las em um formato único e coeso, pronto para análise ou armazenamento posterior.

🌟 Funcionalidades


Leitura de Dados Flexível: Suporta a leitura de arquivos .json e .csv.
Padronização de Colunas: Renomeia colunas de um conjunto de dados para que correspondam a um padrão desejado (neste caso, as colunas do JSON da Empresa A).
Combinação de Dados: Une dados de diferentes fontes em uma única estrutura.
Transformação para Tabela: Converte a lista de dicionários combinada em um formato de lista de listas, ideal para escrita em CSV.
Salvamento em CSV: Salva os dados processados em um novo arquivo CSV.
🛠️ Tecnologias Utilizadas

Python 3.x
Bibliotecas Padrão do Python:
json
csv


🚀 Como Usar


Pré-requisitos
Certifique-se de ter o Python 3.x instalado em sua máquina.

Estrutura de Pastas
Para que o script funcione corretamente, seu projeto deve ter a seguinte estrutura de pastas:

seu_projeto/
├── data_raw/
│   ├── dados_empresaA.json
│   └── dados_empresaB.csv
├── data_processed/
├── scripts/
│   ├── processamento_dados.py
│   └── fusaofev.py (ou seu script principal)
└── README.md


data_raw/: Contém os arquivos de dados brutos de origem.

data_processed/: Será o destino dos arquivos CSV processados.

scripts/: Contém os scripts Python do projeto.

Instalação

Não há dependências externas a serem instaladas além das bibliotecas padrão do Python.

Clone este repositório:

Bash

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

Crie as pastas data_raw e data_processed se elas não existirem.

Coloque seus arquivos dados_empresaA.json e dados_empresaB.csv dentro de data_raw/.

Execução

Para executar a pipeline e processar os dados:

Abra um terminal na raiz do projeto.

Execute o script principal:

Bash

python scripts/fusaofev.py
Após a execução, um novo arquivo CSV (dados_combinados.csv ou o nome que você definir) será gerado na pasta data_processed/, contendo os dados unificados e padronizados.

📈 Exemplo de Uso (no código fusaofev.py)


O script fusaofev.py demonstra o fluxo completo:

Instancia objetos Dados para os arquivos JSON e CSV.
Define um key_mapping para renomear as colunas do CSV de Empresa B para o padrão do JSON de Empresa A.
Renomeia as colunas do objeto dados_empresaB.
(Opcional, mas recomendado para o fluxo completo) Combinaria os dados e os salvaria em um novo CSV.


🤝 Contribuição


Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou encontrar algum problema, sinta-se à vontade para abrir uma issue ou enviar um pull request.

📄 Licença


Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

