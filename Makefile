# -------------------------------------
# Project Commands
# -------------------------------------

.DEFAULT_GOAL := help
BUILD_DIR := ./build

.PHONY: build
build: ## Create a build for testing
	mkdir -p ${BUILD_DIR}
	cookiecutter -o ${BUILD_DIR} ./

.PHONY: build.clean
build.clean: ## Clean all files from ./build
	rm -rf ${BUILD_DIR}/*

# -------------------------------------
# Makefile Documentation
# -------------------------------------
# See: http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

.PHONY: help
help: help-commands help-usage ## This help dialog

.PHONY: help-commands
help-commands:
	@echo "\nCommands:"
	@grep -E '^[a-zA-Z._-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


# Update this target to add additional usage
.PHONY: help-usage
help-usage:
	@echo "\nUsage:"
	@echo "make <command> [Options...]"

# Update this target to add additinoal examples
.PHONY: help-examples
help-examples:
	@echo "\nExamples:"
	@echo ""

# -------------------------------------
# Prompts
# -------------------------------------
# See: http://stackoverflow.com/a/14316012 (user confirmation snippet)

# Usage Example:
#
# .PHONY ask-message
# ask-messages:
# 	@echo "About to do a thing."
#
# .PHONY ask
# ask: ask-message confirm
# 	@echo "Did a thing!"
#

.PHONY: confirm
confirm:
	@while [ -z "$$CONTINUE" ]; do \
		read -r -p "Continue? [y/N] " CONTINUE; \
	done ; \
	if [ ! $$CONTINUE == "y" ]; then \
	if [ ! $$CONTINUE == "Y" ]; then \
		echo "Exiting." ; exit 1 ; \
	fi \
	fi
