up:
	docker compose up -d --build
down:
	docker compose down
restart: docker_down docker_up
run:
	 uvicorn app:app --reload
