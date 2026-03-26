SEMANA 01 - Resumo do que eu entendi sobre Protocolo HTTP:

# O Protocolo HTTP é um protocolo de resquisições.

## Dentro do protocolo de requisições nós temos o REQUEST e o RESPONSE.

- O request é a requisição feita pelo cliente.
- O response é a resposta do servidor.

Basicamente funciona: REQUEST --> RESPONSE

O servidor ele pode ser tanto 1 quanto vários funcionando ao mesmo tempo.

# Verbos e boas práticas do protocolo HTTP

# GET -> usado para ler dados, buscar informações, consultar, etc. Tudo que envolve leitura. Ele não tem corpo e os dados fica diretamente na URL.

# POST -> usado para quando quer criar algo, adicionar, etc. Ele possui corpo e sua informação fica oculta. Exemplo: senha. Se fosse uma senha em GET, ela ficaria visível, por isso necessário ir no POST.

# PUT/PATCH -> usado para atualizar informações/dados. A diferença é que o put atualiza todas as informações mesmo que não solicitadas. O Patch atualiza somente o que for solicitado.

# DELETE -> serve para deletar informações.

## DNS: é o sistema que converte o domínio em um IP, exemplo: 104.15.103..... Ele sempre vai na ida.

## API: é o contrato do servidor e define quais rotas existem, o que cada um retorna, etc.

---------------------

SEMANA 02 - Banco de Dados

# No supabase, podemos criar tabelas que vão se comunicar com nossa linguagem python (no caso desse projeto)

## As tabelas possuem nome, tipo e valor de ativação digamos assim.
## O tipo é fundamental entendermos qual tipo de informação estamos puxando para não ter erro na hora de integrar, exemplo: se é um texto, se é um int8, um float, etc. No caso do projeto de conversor-cripto, nossos valores financeiros sempre serão numericos e não flutuantes pois os flutuantes possuem problema com precisão binária, as vezes um número 100 pode ser armazenado como 999,997 e precisamos de números concretos, por isso, optamos por numeric.
# - para valores financeiros, centavos importam, por isso, float não cai bem nesse caso.

# Na data de conversão, colocamos o timestamp com now() para puxar automaticamente a data convertida.

# Dentro do supabase, o SQL editor funciona como o terminal onde executamos códigos relacionados a uma tabela.
## SQL resumidamente é o protocolo do banco de dados, assim como o HTTP é o protocolo da web.
## Query ou queries em plural é uma consulta que fazemos em um banco de dados. Exemplo: se pedimos uma query de conversões, estamos pedindo para consultar as conversões, tipo uma busca.

## Os termos do SQL levam em consideração os mesmos termos do protocolo HTTP, de get, post, patch, delete, etc.