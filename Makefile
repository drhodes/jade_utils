# http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk \
	'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

FORCE:

build: ## build
	echo build

test: ## test
	echo test

clean: FORCE ## clean all the things
	./clean.sh

work: ## open all files in editor
	emacs -nw *.py Makefile

add: clean ## add files to the git repo
	git add -A :/

commit: ## git commit -a
	git commit -a


