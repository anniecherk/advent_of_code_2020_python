# ~~~~~~~~~~~~~~~~~~ Setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# initial setup:
# just install
# grab pypy with pyenv & set it as the local python for this dir
# pyenv should pick up on the version of pypy specified in .python-version    
# grab session cookie and stick it in token.txt in the rootdir (this file is gitignored)

# run once to install deps from requirements.txt
install:
    pip install -r requirements.txt

# ~~~~~~~~~~~~~~~~~~ Workflow ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#     Before aoc opens for the day:
#
# set up split screen: 
# just new-day SOMEDAY
# aoc in browser window 1, editor w/ stars.py & utils.py split paned, jupyter notebook in browser window 2
# copy utils.py into jupyter notebook, and ready the raw string
# update the day in the print statement in stars.py (for sanity check)
#
#      During aoc:
#
# as soon as the problem is ready: 
#          just pull-input DAY
# then grab the example input from the webpage, paste it into the raw string
# iterate in notebook, but then run it end-to-end with:
#          just run-example DAY
# then to run the test input, run:
#          just run-input DAY
# submit the answer manually
#
#      After submitting correctly for both stars:
#
# copy out the modified utils.py into the base dir
# clean up before committing and pushing:
#           just clean

# ~~~~~~~~~~~~~~~~~~ Game prep ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# opens a jupyter notebook
notebook:
    jupyter notebook 2> /dev/null &

# rm's old input.txt, makes a new dir named DAY, copies in templates and starts jupyter notebook
new-day DAY:
    rm input.txt
    mkdir {{DAY}}
    cp stars.py {{DAY}}/stars.py
    cp utils.py {{DAY}}/utils.py
    just notebook
    @echo "\n\nchange the hardcoded day in the print at the bottom of the template"
    @echo "copy into notebook: utils & SAMPLE"
    @echo "remember to pull-input once the day opens"


# ~~~~~~~~~~~~~~~~~~ Game time ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# uses the token saved in token.txt to pull personal puzzle input, and saves it to input.txt from the invoked dir
# info on getting the token: https://github.com/wimglenn/advent-of-code-wim/issues/1
# won't pull if there's an exiting input.txt file
# inputs are ephemeral, ie, not committed, and need to be regen'd before running the solution
pull-input DAY:
    python downloader.py {{DAY}} 2020

# here the argument "DAY" is the dir name, so needs to be 01 rather than 1
run-example DAY:
    python {{DAY}}/stars.py
 
# here the argument "DAY" is the dir name, so needs to be 01 rather than 1
run-input DAY:
    echo "you pull-input'd right?"
    python {{DAY}}/stars.py real

# ~~~~~~~~~~~~~~~~~~ Clean up ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# lints & formats any python file
lint-format PYTHON-FILE:
    isort {{PYTHON-FILE}}
    docformatter {{PYTHON-FILE}}
    black {{PYTHON-FILE}}
    pylint {{PYTHON-FILE}}

# lints & formats, and copies out any changes from DAY/utils.py. DAY is dirname.
clean DAY:
    just lint-format {{DAY}}/stars.py ; \
    just lint-format {{DAY}}/utils.py ; \
    cp {{DAY}}/utils.py utils.py
    @echo "\n\nreminder: kill jupyter"
