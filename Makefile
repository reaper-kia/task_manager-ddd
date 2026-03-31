DC = docker-compose
EXEC = docker exec -it
LOGS = docker logs
ENV_FILE = .env
APP_FILE = docker_compose/app.yml
APP_CONTAINER = main-app
PROJECT_DIR = .

.PHONY: app
app:
	cd $(PROJECT_DIR) && $(DC) -f $(APP_FILE) --env-file $(ENV_FILE) up --build -d

.PHONY: app-down
app-down:
	cd $(PROJECT_DIR) && $(DC) -f $(APP_FILE) --env-file $(ENV_FILE) down -v

.PHONY: app-logs
app-logs:
	$(LOGS) $(APP_CONTAINER) -f

.PHONY: app-stop
app-stop:
	cd $(PROJECT_DIR) && $(DC) -f $(APP_FILE) --env-file $(ENV_FILE) stop