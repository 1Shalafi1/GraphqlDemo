build:
	docker build -t graphql .

run:
	docker run -rm -d --name api -p 80:80 graphql

run-compose:
	docker-compose -f docker-compose.yml up --build

db-init:
	docker exec -i db pg_restore -U postgres -d graphql < ./app/_fixtures/db_dump/dvdrental.tar

db-psql:
	docker exec -it db psql -U postgres -d graphql
