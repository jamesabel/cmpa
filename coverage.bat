venv\Scripts\coverage.exe run --source dircmpa -m py.test
venv\Scripts\coverage report
venv\Scripts\coverage report -m dircmpa\*.py > coverage\coverage.txt
venv\Scripts\coverage html -d coverage\coverage_html  nocirprt\*.py
