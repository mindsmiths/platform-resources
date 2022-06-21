clean-test:
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint:
	flake8 . \
	 --max-line-length=120 \
	 --ignore= \
	 --exclude=.svn,CVS,.bzr,.hg,.git,__pycache__,.tox,.eggs,*.egg,venv/

test:
	forge test

format:
	yapf --style setup.cfg -r -i .

type-check:
	cd .. && mypy --config-file={{cookiecutter.project_repo_name}}/setup.cfg -p {{cookiecutter.project_repo_name}}
