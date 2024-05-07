Some new super test

pip install --no-cache-dir -r requirements.txt
playwright install

run test - pytest tests

To get allure report on Windows: 

install JAVA somehow

in powershell run:
- Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
- Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression   
- scoop install allure  

Then:
- run tests
- allure serve report  