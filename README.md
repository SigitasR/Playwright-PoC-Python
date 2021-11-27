
# Playwright PoC in Python

Simple proof-of-concept script in Python to run on barbora.lt

### Setup:

`pipenv shell` (to start the virtual env)

`pipenv install` (to install dependencies from Pipfile)

`playwright install` (to install Playwright browsers)

### Runing test:

(Use Git bash or Linux / Mac console)

`EMAIL='email@youremail.com' PASS='yourpass' python -m pytest -m full_flow -s --headed --video on --browser chromium --base-url https://barbora.lt --alluredir=$(pwd)/allure-results`


To generate and view Allure report:

`allure serve allure-results` (Allure binary must be installed and added to PATH env variable)
