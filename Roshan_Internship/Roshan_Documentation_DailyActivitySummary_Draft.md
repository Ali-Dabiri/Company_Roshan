
##### تاریخ: 1 شنبه - 1404/04/22 

- Start Task: Roshan_Task01_00_00
- Create Virtual Environment 
	- `py -m venv Roshan_Task01_00_00`
- Install required packages for Task01_00_00
	- `pip install Django`
	- `pip install djangorestframework`
	- `pip install django-filter`
- Create Django Project 
	- `django-admin startproject Task01_00_00_News_Builder_API`
- `cd Task01_00_00_News_Builder_API`
- Create Django App
	- `py manage.py startapp Task01_00_00_News_Page_App`
- Open Task01_00_00 in VS Code with CMD 
	- `code .`
- Create files for Task01_00_00
	- `serializers.py`
	- `filters.py`
	- `urls.py`
- Configure Django Project ,file `settings.py`
	- Add package and App in `INSTALLED_APPS`
		- `'rest_framework',`
		- `'django_filters',`
		- `'Task01_00_00_News_Page_App',`
- Define models in file `models.py`
- Prepare Database 
	- Apply model migrations to the database:
	    - `py manage.py makemigrations Task01_00_00_News_Page_App`
	- Create tables in the database:
	    - `py manage.py migrate`
- Define serializers in file `serializers.py`
- Define filters in file `filters.py`
- Define views in file `views.py`
- Define urls 
	- Django App in file `urls.py`
	- Django Project in file `urls.py`
- Configure Django Project ,file `settings.py`
	- Add `DEFAULT_FILTER_BACKENDS` in `REST_FRAMEWORK` 
- Insert Sample Data in Database for real test
	- Use python shell for Add test News
		- `python manage.py shell`
- Create `createsuperuser` for Django Admin
	- `python manage.py createsuperuser`
- Import models in file `admin.py`
	- `admin.site.register()`
- Write test for Django App in file `tests.py`
- run file `tests.py` 
	- `py manage.py test`

--------------------------------------------

##### تاریخ: 2 شنبه - 1404/04/23 

- Start Task: Roshan_Task02_00_00
- Create Virtual Environment
	- `py -m venv Roshan_Task02_00_00`
- Install required packages for Task02_00_00
	- `pip install scrapy`
- Create Scrapy Project
	- `scrapy startproject Task02_00_00_Zoomit_Product01_00_00`
- `cd Task02_00_00_Zoomit_Product01_00_00`
- Open Task02_00_00_Zoomit_Product01_00_00 in VS Code with CMD 
	- `code .`
- `cd Task02_00_00_Zoomit_Product01_00_00`
- `cd spider`
- Create Spider for Task02_00_00_Zoomit_Product01_00_00
	- `scrapy genspider Zoomit_Product01_00_00_Zoomit_Spider zoomit.ir`
- Review `robots.txt` for zoomit.ir
	- URL: https://www.zoomit.ir/robots.txt
- write scraper program for Zoomit_Product01_00_00
- Create file json and CSV
	- `scrapy crawl Zoomit_Product01_00_00_Zoomit_Spider -o Zoomit_Product_Data.json`
	- `scrapy crawl Zoomit_Product01_00_00_Zoomit_Spider -o Zoomit_Product_Data.csv`

--------------------

##### تاریخ: 4 شنبه - 1404/04/25

- Start Task: Task02_00_00_Zoomit_News_Search01_00_00
- `cd Roshan_Task02_00_00`
- Install required packages for Task02_00_00
	- `pip install scrapy`
	- `pip install selenium`
	-  `pip install webdriver-manager`
- Create Scrapy Project
	- `scrapy startproject Task02_00_00_Zoomit_News_Search_Content01_00_00`
- `cd Task02_00_00_Zoomit_News_Search_Content01_00_00`
- Open Task02_00_00_Zoomit_News_Search_Content01_00_00 in VS Code with CMD 
	- `code .`
- `cd Task02_00_00_Zoomit_News_Search_Content01_00_00`
- `cd spider`
- Create Spider for Task02_00_00_Zoomit_News_Search_Content01_00_00
	- `scrapy genspider Zoomit_News_Search_Content01_00_00_Zoomit_Spider zoomit.ir`
- Review `robots.txt` for zoomit.ir
	- URL: https://www.zoomit.ir/robots.txt
- Configure Scrapy settings file `settings.py`
	- set `ROBOTSTXT_OBEY = False`
- write scraper program for Zoomit_News_Search_Content01_00_00
- Create file json and CSV
	- `scrapy crawl Zoomit_News_Search_Content01_00_00_Zoomit_Spider -o Zoomit_Product_Data.json`
	- `scrapy crawl Zoomit_News_Search_Content01_00_00_Zoomit_Spider -o Zoomit_Product_Data.csv`
- 
