# Cotação Amigoz - API de Cotações de Moedas


## ATENÇÃO
 O projeto a seguir possui um over engineering altíssimo!
 Mas foi feito desta forma para demonstrar as habilidades gerais do programador ;P

 ---

## Sumário

- [Descrição](#descrição)  
- [Tecnologias Utilizadas](#tecnologias-utilizadas)  
- [Arquitetura do Projeto](#arquitetura-do-projeto)  
- [Como Rodar o Projeto](#como-rodar-o-projeto)  
- [Testes](#testes)  
- [Logging](#logging)  

---

## Descrição

currency_quotation é uma API RESTful desenvolvida em FastAPI que oferece cotações atualizadas para moedas como Dólar e Euro.

---

## Tecnologias Utilizadas

- Python 3.13  
- FastAPI  
- Pydantic  
- HTTPX  
- Uvicorn  
- Pytest  
- Docker e Docker Compose  

---

## Arquitetura do Projeto

```plaintext
app/
├── clients/           # Clientes para consumir APIs externas
│   ├── dollar_client.py
│   └── euro_client.py
├── config/            # Configurações da aplicação
│   └── config.py
├── entities/          # Entidades do domínio (ex: Dollar, Euro, Quotation)
│   ├── dollar.py
│   ├── euro.py
│   └── quotation.py
├── logs/              # Arquivos de log
│   ├── execution.log
│   └── service_calls.log
├── models/            # Modelos Pydantic para validação e transformação dos dados
│   ├── dollar_model.py
│   ├── euro_model.py
│   ├── quotation_model.py
│   └── response_model.py
├── services/          # Serviços de negócio (ex: dollar_service.py, quotation_service.py)
│   ├── dollar_service.py
│   └── quotation_service.py
├── utils/logs/        # Utilitários para logging
│   ├── execution_logger.py
│   ├── logger_factory.py
│   └── service_logger.py
├── container.py       # Configuração do container/injector para DI
├── di.py              # Configuração para injeção de dependências
└── main.py            # Ponto de entrada da API FastAPI

tests/
├── clients/           # Testes para clients
│   ├── test_dollar_client.py
│   └── test_euro_client.py
├── entities/          # Testes para entidades
│   ├── test_dollar_entity.py
│   └── test_euro_entity.py
└── services/          # Testes para serviços
    ├── test_dollar_service.py
    └── test_euro_service.py
```

---

# Como Rodar o Projeto

### Pré-requisitos
1. Python 3.13
2. Docker e Docker Compose

### Rodando localmente
1. git clone <URL_DO_REPOSITORIO>
2. cd currency_quotations
3.  python -m venv venv
4. source venv/bin/activate   # Linux/macOS
5. pip install -r requirements.txt
6. uvicorn app.main:app --host 0.0.0.0 --port 8000

### Rodando com Docker compsoe
docker-compose up --build

--- 

# Testes

O projeto possui testes com pytest que cobrem:

**Clients:** Testam as chamadas aos serviços externos simulando as respostas.

**Entities:** Validam os modelos e entidades de domínio.

**Services:** Validam a lógica de negócio e integração dos dados.

### Para rodar os testes:
- ./run_tests.sh
 
- pytest /tests/<CAMINHO_DO_TESTE>

--- 

# Logging
O projeto possui sistema de logs que cobre:

Execução geral da aplicação (execution.log)

Logs específicos de chamadas aos serviços externos (service_calls.log)

