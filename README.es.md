📝 Instrucciones
Crea un API conectada a una base de datos e implemente los siguientes endpoints (muy similares a SWAPI.dev or SWAPI.tech):

-- [GET] /people Listar todos los registros de people en la base de datos
---[GET] /people/<int:people_id> Listar la información de una sola people
---[GET] /planets Listar los registros de planets en la base de datos
---[GET] /planets/<int:planet_id> Listar la información de un solo planet
Adicionalmente necesitamos crear los siguientes endpoints para que podamos tener usuarios en nuestro blog:

---[GET] /users Listar todos los usuarios del blog
---[GET] /users/favorites Listar todos los favoritos que pertenecen al usuario actual.
--[POST] /favorite/planet/<int:planet_id> Añade un nuevo planet favorito al usuario actual con el planet id = planet_id.
--[POST] /favorite/people/<int:planet_id> Añade una nueva people favorita al usuario actual con el people.id = people_id.
--[DELETE] /favorite/planet/<int:planet_id> Elimina un planet favorito con el id = planet_id`.
--[DELETE] /favorite/people/<int:people_id> Elimina una people favorita con el id = people_id.
Tu API actual no tiene un sistema de autenticación (todavía), es por eso que la única forma de crear usuarios es directamente en la base de datos usando el flask admin.
☝️ Nota: Aquí hay un ejemplo en Postman: https://documenter.getpostman.com/view/2432393/TzRSgnTS#a4174b48-3fc8-46e3-bf82-19a08107666f

📖 Fundamentos
Este ejercicio te permitirá practicar las siguientes habilidades y conceptos:

Construcción de API's utilizando el standard REST (A.k.a: RESTful API's)
Construir una base de datos utilizando el ORM llamado SQLAlchemy o TypeORM (https://typeorm.io/).
Utilizar y entender sistemas de migraciones de bases de datos con Alembic o las migraciones nativas de TypeORM (en el caso de node.js).
😎 Te sientes con confianza?
Los siguients requerimientos no son necesarios para completar el projecto satisfactoriamente pero puedes desarrollarlos para continuar tu aprendizaje si te sientes con suficiente confianza.

+4 Crea API Endpoints para agregar (POST), modificar (PUT) y eliminar (DELETE) planets y people. De esta manera toda la base de datos va a poder ser administrada via API.

