.PHONY: setup start stop clean all-reset debug

setup:
	pip install -r backend/requirements.txt
	cd frontend && npm i --force

start:
	docker-compose up -d

stop:
	docker-compose stop

clean:
	make stop
	docker-compose rm plant_akinator_frontend plant_akinator_backend
	docker-compose rmi plant_akinator-backend plant_akinator-frontend

all-reset:
	docker-compose down --rmi all --volumes --remove-orphans

bash:
	docker-compose exec $(CONTAINER_NAME) /bin/bash
