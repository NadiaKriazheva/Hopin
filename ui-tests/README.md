#Instruction

1. Install Python version 
   - [download](https://www.python.org/downloads/)
   - Please tick "Add Python to PATH" when asked
1. Open CommonLine and execute followind commands:
   - **pip install pytest**
   - **pip install selenium**   
1. Install ChromeDriver:
   - download the ChromeDriver binary [download](https://chromedriver.chromium.org/downloads)  
   - include the ChromeDriver location in your PATH environment variable
1. Execute the command: **pytest -s test_customers_app.py** in **ui-tests** directory

#Project
- [conftest.py](conftest.py) contains a fixture that
  - starts and tears down browser
  - takes a screenshot at the end of each test
- [pytest.ini](pytest.ini) contains markers that can be used to run separate tests: **-m bug_1**
- [test_customer_app.py](test_customer_app.py) file with tests
- [README.md](README.md) the file you are reading now

#HTML report
I have included a [sample HTML report](report.html). 
In order to generate report an additional plugin needs to be installed
1. Open CommonLine and execute command: **pip install pytest-html**
1. Uncomment code in [conftest.py](conftest.py)
1. Execute the command: **pytest --html=report.html --self-contained-html test_customers_app.py** in **ui-tests** directory




