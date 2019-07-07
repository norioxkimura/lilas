
help:
	@:

install:
	for f in pre-commit commit-msg pre-push; do                                             \
            ln -sf "../../devops/git/hooks/$$f" `git rev-parse --git-dir`"/hooks/$$f";          \
        done
	git config commit.template `git rev-parse --show-prefix`/commit-template

uninstall:
	rm -f `git rev-parse --git-dir`/hooks/{pre-commit,commit-msg,pre-push}

clean:
	@:

SHELL = bash

.PHONY: help clean install uninstall
