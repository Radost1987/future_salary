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

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
