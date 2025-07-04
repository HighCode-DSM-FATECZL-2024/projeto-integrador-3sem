SHELL := /bin/bash
.PHONY: "help build dev start alo"


help:
	@echo " Available Commands:"
	@echo " build        - Build the front-end to /frontend/dist"
	@echo " dev          - Run the backend and frontend in dev mode"
	@echo " start        - Start the project (build and run)"
	@echo " help         - Show this help message"

UNAME := $(shell uname -s)
PNPM_EXIST := $(shell command -v pnpm 2>/dev/null) # Adicionei o $(shell) aqui, pois faltava
MENU_OPTS := "npm"
CUR_DIR := $(shell pwd)

ifeq ($(PNPM_EXIST),)
else
	MENU_OPTS += "pnpm"
endif

MENU_OPTS += "Exit"

ifeq ($(UNAME),Linux)
	OS_NAME := Linux
	RUN_PARALLEL_CMD := &  # Operador para rodar em background no Linux
	CLEAN_SCREEN_CMD := clear
else ifeq ($(UNAME),Darwin) # macOS
	OS_NAME := macOS
	RUN_PARALLEL_CMD := &  # Operador para rodar em background no macOS
	CLEAN_SCREEN_CMD := clear
else 
	OS_NAME := Windows
	RUN_PARALLEL_CMD := start /b
	CLEAN_SCREEN_CMD := cls
endif

build:
	@echo "Choose an option to build"
	@select choice in $(MENU_OPTS); do \
			case $$choice in \
				"npm") $(MAKE) -s build_npm; break;; \
				"pnpm") $(MAKE) -s build_pnpm; break;; \
				"Exit") echo "Exiting..."; break;; \
				*) echo "Invalid option. Please choose the number of option ";; \
			esac; \
		done

build_npm:
	$(CLEAN_SCREEN_CMD)
	@echo "Building with NPM (Node Package Manager)"
	cd frontend && npm run build
	@echo "Build finished found in $(CUR_DIR)/frontend/dist"

build_pnpm:
	$(CLEAN_SCREEN_CMD)
	@echo "Building with PNPM (Perfomant Node Package Manager)"
	cd frontend && pnpm build
	@echo "Build finished found in $(CUR_DIR)/frontend/dist"

dev:
	@echo "Starting project in DevMode"
	@select choice in $(MENU_OPTS); do \
		case $$choice in \
			"npm") $(MAKE) -s dev_npm;; \
			"pnpm") $(MAKE) -s dev_pnpm; break;; \
			"Exit") echo "Exiting..."; break;; \
			*) echo "Invalid option. Please choose the number of option ";; \
		esac; \
	done

dev_npm:
	$(CLEAN_SCREEN_CMD)
	@echo "Devmode with npm"
	cd frontend && npm run dev --silent $(RUN_PARALLEL_CMD)  \
	cd backend && cd src && $(MAKE) -s venv && $(MAKE) -s run
	@echo "Project started in Devmode"

dev_pnpm:
	$(CLEAN_SCREEN_CMD)
	@echo "Devmode with npm"
	cd frontend && pnpm --silent dev $(RUN_PARALLEL_CMD)  \
	cd backend && cd src && $(MAKE) -s venv && $(MAKE) -s run
	@echo "Project started in Devmode"