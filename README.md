# Online House Checker

Pequeno projetinho que fiz quando estava a toa, para verificar se meu Raspberry Pi está online.

Ele está dividido em 2 partes: **client e server**

- O client mantém uma minúscula API Flask com um endpoint rodando, que recebe o ping de um script que roda de hora em hora no Heroku.
- O server fica no Heroku, ele possui endpoints para cadastro, visualização e exclusão de clients que ele irá verificar periodicamente

Caso o heroku não receba resposta, ele envia uma mensagem a um bot que está em um canal do Telegram, notificando que o Raspberry está offline.

## Como usar

### Client

- Crie um ambiente virtual e instale as dependências
  - `python3 -m venv .venv`
  - `source .venv/bin/activate`
  - `pip install -r requirements.txt`
- No client, basta rodar o script
  - `./start_client.sh`
- Utilize um serviço como o [ngrok](https://ngrok.com/) para expor a porta 5000 para a web
  - `./ngrok http 5000`

### Server

- Upe o projeto no Heroku, e crie as seguintes variáveis de ambiente:
  - `TELEGRAM_TOKEN`: O token do seu bot
  - `CHANNEL_ID`: O ID do canal que ele deverá enviar a mensagem, **ou** o chatID da pessoa que vc deseja que o bot envie a mensagem (nesse caso é necessário que a pessoa adicione o bot antes e envie uma mensagem para o mesmo)
- Adicione um serviço de MongoDB ao seu projeto do Heroku, eu utilizei o mLabMongoDB, é gratuito
- Adicione também o serviço se scheduler do Heroku ao seu projeto, o **Heroku Scheduler**, e faça ele rodar o seguinte comando periodicamente:
  - `curl https://<sua_url_do_heroku>.herokuapp.com/check`
- Fazer um GET no endpoint `/check`, fará com que a API verifique se todos os clients cadastrados estão online, e notifica quem não estiver.

### Adicionando um client

Após sua aplicação estiver rodando bonitinha no Heroku, utilize um Insomnia da vida ou até mesmo o `curl` para cadastrar os clients no server, no seguinte entpoint:
- URL_BASE: `<sua_url_do_heroku>.herokuapp.com/clients`
  - GET: Lista todos os clients cadastrados
  - POST: Cadastra um novo client, mande o body em json dessa forma:
    - `{"name": "<um_nome>", "url": "<url_exposta_pelo_ngrok>"}`
  - DELETE: Deleta um client cadastrado, mande o body em json dessa forma:
    - `{"name": "<nome_do_client_a_ser_deletado>"}`

## Considerações finais

Este projetinho é um pouco inútil, assim como a maioria que eu faço, mas foi útil para que eu pudesse aprender:
- MongoDB com python
- Um pouco mais de bot no telegram
- Um pouco mais em APIs com Flask
