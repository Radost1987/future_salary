# Future salary

This script gathers information about the average salary from sites [SuperJob](https://www.superjob.ru) and [HeadHunter](https://www.hh.ru) on vacancies "Programmer" for 8 popular programming languages: JavaScript, Go, Python, Java, PHP, C++, CSS, Ruby.
Only vacancies from Moscow are considered.
Using [API HeadHunter](https://github.com/hhru/api/blob/master/docs/general.md) and [API SuperJob](https://api.superjob.ru)

### How to install

* Python3 should be already installed.

* Then create and active a virtual environment, and install all the dependencies:
```bash
pip install -r requirements.txt
```

* To use all API methods, you need to register your application[https://api.superjob.ru/info/](https://api.superjob.ru/info/) and get Secret key.

* Put SuperJob Secret key in file `.env` to folder with script like this:
```
SUPER_JOB_SECRET_KEY=v3.r.114731273.0e7f377b1b5d8e0bc
```

* Run the script in a terminal
```bash
python main.py
```

### Example
After the script run in the terminal you will see

```
+SuperJob Moscow--------+------------------+---------------------+------------------+
| Язык программирования | Вакансий найдено | Вакансий обработано | Средняя зарплата |
+-----------------------+------------------+---------------------+------------------+
| JavaScript            | 116              | 72                  | 93177            |
| Go                    | 22               | 13                  | 135192           |
| Python                | 74               | 54                  | 95500            |
| Java                  | 82               | 40                  | 106400           |
| PHP                   | 76               | 55                  | 95037            |
| C++                   | 59               | 43                  | 94465            |
| CSS                   | 70               | 47                  | 89654            |
| Ruby                  | 5                | 3                   | 55000            |
+-----------------------+------------------+---------------------+------------------+
+HeadHunter Moscow------+------------------+---------------------+------------------+
| Язык программирования | Вакансий найдено | Вакансий обработано | Средняя зарплата |
+-----------------------+------------------+---------------------+------------------+
| JavaScript            | 4569             | 899                 | 175627           |
| Go                    | 1060             | 222                 | 215187           |
| Python                | 3266             | 517                 | 186533           |
| Java                  | 3788             | 480                 | 212360           |
| PHP                   | 1850             | 850                 | 157974           |
| C++                   | 1708             | 506                 | 171304           |
| CSS                   | 2575             | 736                 | 151428           |
| Ruby                  | 303              | 94                  | 210841           |
+-----------------------+------------------+---------------------+------------------+
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
