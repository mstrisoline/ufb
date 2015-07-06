#UFB Micro Self Registration Blogging App 
##Installation

This installation will use some basic assumptions for its installation

###Requirements
- Python3
- PostgreSQL 9.X.X
- virtualenv
- mkvirtuelenv

###Environment Setup
This assumes you have already installed the quired system dependencies and set them up

1. `cd /path/to/virtual/envs`
1. `git clone https://github.com/mstrisoline/ufb.git .`
1. `cd ufb`
1. `mkvirtualenv -p python3 .`
1. `cp setup/postactivate bin/.
1. `workon ufb`
1. `pip install -r requirements.txt`
1. `python manage.py db init`
1. `python manage.py db migrate`
1. `python manage.py db upgrade`
1. `pyton run.py`
1. [App running on localhost](http://localhost:5000)

###Usage
The usage of this should be fairly self explanitory
- 
