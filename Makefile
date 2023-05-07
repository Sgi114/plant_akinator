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
	docker rm plant_akinator-backend-1 plant_akinator-frontend-1
	docker rmi plant_akinator-backend plant_akinator-frontend

all-reset:
	docker-compose down --rmi all --volumes --remove-orphans

debug:
	docker commit $(CONTAINER_ID) test
	docker run --rm -it test bash
