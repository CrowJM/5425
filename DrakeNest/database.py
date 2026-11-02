
#Funcoes relacionadas apenas com a base de dados SQLite
from pathlib import Path
import sqlite3


PASTA_PROJETO = Path(__file__).resolve().parent
CAMINHO_BASE_DADOS = PASTA_PROJETO / "DrakeNestBD" / "DrakeNestPainel.db"
CAMINHO_SCHEMA = PASTA_PROJETO / "schema.sql"


#Abre uma ligacao com a base de dados local.
def obter_ligacao():
    ligacao = sqlite3.connect(CAMINHO_BASE_DADOS)
    ligacao.row_factory = sqlite3.Row
    return ligacao


#Cria a base de dados e as tabelas, se ainda nao existirem.
def DrakeNestBD():
    CAMINHO_BASE_DADOS.parent.mkdir(exist_ok=True)

    with obter_ligacao() as ligacao:
        ligacao.executescript(CAMINHO_SCHEMA.read_text(encoding="utf-8"))
