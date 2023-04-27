.PHONY: setup start stop clean all-reset debug

setup:
	cd backend
	pip install -r requirements.txt
	cd ../frontend
	npm i --force

start:
	docker-compose up -d

stop:
	docker-compose stop

clean:
	docker-compose down

all-reset:
	docker-compose down --rmi all --volumes --remove-orphans

debug:
	docker commit $(CONTAINER_ID) test
	docker run --rm -it test bash
