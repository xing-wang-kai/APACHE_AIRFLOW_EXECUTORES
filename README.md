## AIRFLOW COM OUTROS EXECUTORES

POdemos usar outros executores com airflow, por padrão ele veem com o executor SequentialExecutor que uso o banco de dados SQL lite para rodar suas task o Executor Sequencial executa uma task por vez em sequencia sem travar a execução e permitindo somente continuar após uma task e outra.

Existem outros tipos de executores que podem ser usados para o processo tais como o CeleryExecutor que usa Works paralelos em suas execuçoes o que grante que ao ocorrer um problema em um work outro possa continuar o processo, esse executor usar o REDIS e outro banco de dados local para rodar as execuções.

Além disso também temos o Executor chamado de LocalExecutor que usamos um banco de dados local para rodar as task, assim com o Celery ele pode executar task em paralelo porém de modo local dependendo do banco de dados da máquina, se uma task falha por motivos computacionais tudo falhará.


#### COMO FUNCIONA O AIRFLOW

Um usuário ACESSA a INTERFACE do AIRFLOW >>
WEBSERVER
A interface analisa o BANCO DE DADOS e verifica as TASK registradas >>
schedule Monitora as DAGS e executas as TASK
EXECUTOR executa as tarefas

### LOCAL EXECUTOR

Exemplos abaixo de um executor local rodando


![EXECUTOR](IMG\Captura de tela 2024-09-16 000353.png)