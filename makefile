build:
	docker build -t graphql .

run:
	docker run -rm -d --name api -p 80:80 graphql

run-compose:
	docker-compose -f -d docker-compose.yml up --build

run-compose-with-logging:
	docker-compose -f docker-compose.yml up --build

restart-services:
	docker-compose restart

logs:
	docker-compose logs -t -f --tail 30

db-init:
	docker exec -i db pg_restore -U postgres -d graphql < ./app/_fixtures/db_dump/dvdrental.tar

db-psql:
	docker exec -it db psql -U postgres -d graphql
