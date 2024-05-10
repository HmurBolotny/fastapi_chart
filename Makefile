doker_up:
	docker compose up -d --build
doker_down:
	docker compose down
doker_restart:
	doker_down
	doker_up
app_run:
	 uvicorn app:app --reload
