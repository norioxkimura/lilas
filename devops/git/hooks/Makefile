
help:
	@:

clean:
	@:

install:
	for f in pre-commit commit-msg pre-push; do                                                       \
            ln -sf "../../`git rev-parse --show-prefix`$$f" "`git rev-parse --git-dir`/hooks/$$f";        \
        done
	git config commit.template "`git rev-parse --show-prefix`commit-template"

uninstall:
	rm -f "`git rev-parse --git-dir`/hooks/"{pre-commit,commit-msg,pre-push}
	git config --unset commit.template

SHELL = bash

.PHONY: help clean install uninstall
