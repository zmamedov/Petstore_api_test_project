# Проект по тестированию API Petstore

><a target="_blank" href="https://petstore.swagger.io/">Swagger Petstore</a>
> 
![main page screenshot](pictures/Petstore_API_main_page.png)

---
### Список проверок, реализованных в автотестах
1. Создание одного питомца.
2. Поиск питомца по ID.
3. Поиск несуществующего питомца.
4. Поиск всех питомцев по указанному статусу.
5. Удаление питомца.

---

### Используемые инструменты
<img title="Python" src="pictures/icons/python.svg" height="40" width="40"/> <img title="Pytest" src="pictures/icons/pytest.svg" height="40" width="40"/> <img title="Allure Report" src="pictures/icons/allure_report.png" height="40" width="40"/> <img title="GitHub" src="pictures/icons/github.svg" height="40" width="40"/> <img title="Pycharm" src="pictures/icons/pycharm-original.svg" height="40" width="40"/> <img title="Telegram" src="pictures/icons/telegram.png" height="40" width="40"/> <img title="Jenkins" src="pictures/icons/jenkins-original.svg" height="40" width="40"/> <img title="Requests" src="pictures/icons/requests.png" height="40" width="40"/>  <img title="Jira" src="pictures/icons/jira.svg" height="40" width="40"/>

---

### Запуск автотестов осуществляется с использованием Jenkins
> [Ссылка на сборку в Jenkins](https://jenkins.autotests.cloud/job/zmamedov-qa_guru_Petstore_api_test/)

#### Для запуска автотестов в Jenkins
1. Открыть [задачу в Jenkins](https://jenkins.autotests.cloud/job/zmamedov-qa_guru_Petstore_api_test/)

![jenkins job main page](pictures/Jenkins_job_main_page.png)

2. Нажать "**Build Now**".

---

### Allure отчет

![allure_report page](pictures/allure_report_page.png)

---

### Интеграция с Allure TestOps

> [Job #3989 zmamedov-qa_guru_Petstore_api_test](https://allure.autotests.cloud/project/4223/jobs)

![allure_testops job](pictures/allure_testops_job.png)

---

### Интеграция с Jira
> [Задача в Jira](https://jira.autotests.cloud/browse/HOMEWORK-1234)
 
![jira task](pictures/jira_task.png)

---

### Уведомления в Телеграм

![telegram_notification](pictures/tg_notification.png)