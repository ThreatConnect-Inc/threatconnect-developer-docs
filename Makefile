help:
	@echo "uptcex 		update tcex documentation"
	@echo "clean 		clean unneeded files"
	@echo "test 		run the tests"
	@echo "upstream 	set upstream to https://github.com/ThreatConnect-Inc/threatconnect-developer-docs.git (useful when working on a fork of the TC docs)"
	@echo "doctest 	run sphinx on the documentation to view errors"

uptcex:
	# This script is to be run in the top directory of the TC Documentation (available here: https://github.com/ThreatConnect-Inc/threatconnect-developer-docs)

	rm -rf ./tcex/;

	# clone the most recent commit to the master branch of the tcex repo into the ./tcex directory
	git clone --depth 1 --branch master https://github.com/ThreatConnect-Inc/tcex.git;

	# remove the .git directory of the recently cloned tcex repo
	rm -rf ./tcex/.git/;
	rm -rf ./tcex/.gitignore;

	# remove all of the old tcex documentation files
	rm -rf ./docs/tcex/*;
	# move all of the .rst files from the tcex repo's documentation into this repo's documentation directory
	mv ./tcex/docs/src/*.rst ./docs/tcex/;
	# move all of the tcex module documentation files into this repo's documentation directory
	mv ./tcex/docs/src/tcex_docs/ ./docs/tcex/;
	# rename the landing page for the tcex docs
	mv ./docs/tcex/index.rst ./docs/tcex/tcex.rst;
	# remove the docs directory
	rm -rf ./tcex/docs;

	# remove unused files
	rm -f ./tcex/LICENSE ./tcex/README.md ./tcex/setup.cfg ./tcex/setup.py;
	# move all of the code for tcex up one level
	mv ./tcex/tcex/* ./tcex;
	# remove the empty directory
	rm -rf ./tcex/tcex;

	# change the variable name of the tcex version used in the tcex docs
	sed -i.bak 's/|version|/|tcex_version|/g' ./docs/tcex/tcex.rst && rm ./docs/tcex/tcex.rst.bak;

	# stage all changes (including deletions)
	git add -A;

	# define a datestamp
	DATE=$$(date +"%B %d, %Y");

	# commit
	git commit -m "Auto-update TCEX docs: $$(DATE)";

clean:
	# This script is to be run in the top directory of the TC Documentation (available here: https://github.com/ThreatConnect-Inc/threatconnect-developer-docs)

	rm -rf ./.cache/
	rm -rf ./tests/__pycache__/
	rm -rf ./tests/test.py
	rm -rf ./docs/_build/

test:
	# run the tests and remove the junk created by the tests
	pytest;
	rm -rf ./tests/__pycache__/;
	rm -rf ./tests/test.py;

upstream:
	# set upstream for a clone of this repo
	git remote add upstream https://github.com/ThreatConnect-Inc/threatconnect-developer-docs.git;
	git remote -v;

doctest:
	cd docs && virtualenv ~/.venv/tc_developer_docs && source ~/.venv/tc_developer_docs/bin/activate && pip install sphinx && pip install recommonmark && pip install tcex && pip install sphinx_rtd_theme && sphinx-build -T -E -d _build/doctrees-readthedocs -D language=en . _build/html
