# Some new super test

### To run locally:

1. Install dependencies:
```
pip install --no-cache-dir -r requirments.txt
playwright install
```


2. Run test:
- To run all tests: `pytest -s -v tests`
- To run test with mark (some tests has own tag @mark.{mark_name}): `pytest -s -v -m {mark_name}`
- For parallel tests run: `pytest -s -v -n auto --dist=loadscope`
- To run parallel test suit: `pytest -s -v -m parallel -n auto`

### To get allure report on Windows:

- install JAVA somehow
- In powershell run:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression   
scoop install allure  
```
- run tests
- `allure serve allure_report ` 

### You can use docker:
First uncomment "allure docker part" in Dockerfile
```
docker build -t custom_framework .
docker run -it --rm -p 8001:8001 custom_framework
```
Observe test run Allure results at: 'http://localhost:8001/index.html'

### If all dependencies and allure are installed, you can run:
```
python runner.py
```
