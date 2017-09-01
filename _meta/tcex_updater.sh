# move to the tcex docs dir (uses the `docs` alias that `cd`'s into the root directory of the documentation)
docs
cd ThreatConnect_Developer_Docs/;

# checkout dev
# git checkout dev;

# update tcex
make uptcex;

# change the variable name of the tcex version used in the tcex docs
sed -i.bak 's/|version|/|tcex_version|/g' ./docs/tcex/tcex.rst && rm ./docs/tcex/tcex.rst.bak

# stage all changes (including deletions)
git add -A;

# define a datestamp
DATE=$(date +"%B %d, %Y");

# commit
git commit -m "Auto-update TCEX docs: $DATE";

# push
git push;

# send slack notification (uses the `slack` alias which sends the given message to a slack channel)
slack "TCEX_documentation_updated";
