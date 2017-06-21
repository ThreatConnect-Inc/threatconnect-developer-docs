help:
	@echo "uptcex 		update tcex documentation"
	@echo "test 		run the tests"
	@echo "upstream 	set upstream for a fork of this repo"

uptcex:
	# This script is to be run in the top directory of the TC Documentation (available here: https://github.com/ThreatConnect-Inc/ThreatConnect_Developer_Docs)

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

test:
	# run the tests and remove the __pycache__/ directory created by the tests
	pytest;
	rm -rf ./tests/__pycache__/;

upstream:
	# set upstream for a clone of this repo
	git remote add upstream https://github.com/ThreatConnect-Inc/ThreatConnect_Developer_Docs.git;
	git remote -v;
