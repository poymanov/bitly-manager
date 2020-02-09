.PHONY : run flush

.DEFAULT_GOAL := run

run:
	docker-compose run app python main.py $(args)

flush:
	docker-compose down -v --rmi all