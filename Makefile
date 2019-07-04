TEST_ARGS ?=
TEST_ENVS ?=
TEST_REBUILD ?= yes

# target: help - Display callable targets.
.PHONY: help
help:
	@echo "Reference card for usual actions in development environment."
	@echo "Here are available targets:"
	@egrep -o "^# target: (.+)" [Mm]akefile  | sed 's/# target: / * /'

# target: install - Install workalendar in your current env
.PHONY: install
install:
	pip install -e ./


# target: tox_install - Install tox in your current env
.PHONY: tox_install
tox_install:
	pip install tox --upgrade

# target: test - run tox tests.
# target:        Use TEST_ENVS and TEST_ARGS to target your tests more precisely.
# target:        WARNING: tox should be installed in your current env.
# shall we rebuild the env or not?
ifeq (${TEST_REBUILD},"yes")
TOX_COMMAND=tox -r
else
TOX_COMMAND=tox
endif
.PHONY: test
test:
ifneq (${TEST_ENVS},)
	${TOX_COMMAND} -e ${TEST_ENVS}  -- ${TEST_ARGS}
else
	${TOX_COMMAND}  -- ${TEST_ARGS}
endif

# target: package - build packages for further upload
.PHONY: package
package:
	rm -Rf build/
	python setup.py sdist bdist_wheel
