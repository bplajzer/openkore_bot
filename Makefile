SHELL := /bin/bash
REQUIRED_COMMANDS := "scp" "docker" "docker compose"
SSH_ALIAS := izlude
SSH_PATH := /dane/bot/
FILES_TO_UPLOAD := Makefile docker-compose.yml ./data


.PHONY: all print_env clean
all: check_cmd


print_env:
	@echo "Checking shell."
	@echo "PATH: $(PATH)"
	@echo "SHELL: $(SHELL)"

check_cmd:
	@echo "Checking requirements."
	@for cmd in $(REQUIRED_COMMANDS); do \
		if ! command -v $$cmd &> /dev/null; then \
			echo "∅ Error: command [$$cmd] not found on system!"; \
			exit 1; \
		else \
			echo "→ Command [$$cmd] detected."; \
		fi \
	done

build: check_cmd Dockerfile
	@echo "Building docker image."
	@docker buildx build --platform linux/amd64 -t bot . -f Dockerfile
	@echo "Saving the image to file."
	@docker save bot -o ./bot

stop_all: check_cmd
	@ssh izlude 'cd /dane/bot && make stop1'
	@ssh izlude 'cd /dane/bot && make stop2'

upload: check_cmd stop_all
	@echo "Uploading files to server ${SSH_ALIAS}."
	@echo "Removing data folder from ${SSH_ALIAS}."
	@ssh izlude 'sudo rm -rf /dane/bot/data/*'
	@for file in $(FILES_TO_UPLOAD); do \
		echo "→ uploading $$file"; \
		scp -r $$file ${SSH_ALIAS}:${SSH_PATH}; \
	done

upload_image: check_cmd bot
	@echo "Uploading image to server."
	@scp -r ./bot ${SSH_ALIAS}:${SSH_PATH}

load: check_cmd bot
	@docker load < bot

run1: check_cmd
	@echo "Running docker compose."
	@docker compose -f docker-compose.yml up -d

stop1: check_cmd
	@echo "Stopping docker compose."
	@docker compose -f docker-compose.yml down

run2: check_cmd
	@echo "Running docker compose."
	@docker compose -f docker-compose-two.yml up -d

stop2: check_cmd
	@echo "Stopping docker compose."
	@docker compose -f docker-compose-two.yml down

reload: stop run
	@echo "Service reloaded."

attach: check_cmd
	@docker attach $(c)

clean: check_cmd bot
	@echo "Docker cleanup."
	@docker system prune -a
	@echo "Remove image."
	@rm -rf bot