This project is about integrating feature files with xray and import results of test execution to xray



-- create virtual environment
```
python -m venv myvirtualenv
```

-- activate that virtual environment
```
cd .\myvirtualenv\Scripts\activate
```

-- install requirements
```
pip install -r requirements.txt
```

-- run python file triggerfeaturesfromjira.py with tickets.ini to get tickets from JIRA
```
python triggerfeaturesfromjira.py tickets.ini
```

-- run behave test cases and store the result in results/cucumber.json 
```
pytest -v -s features/test_dem.py --cucumberjson=results/output.json
```

-- upload the execution results to JIRA
```
python importtojira.py
```

