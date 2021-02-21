## Django 프로젝트 생성

- 개발환경구축(OS: Windows 10)

  - Python 설치 및 path 설정
  - pip 버전 업데이트

  - virtualenv 설치 후 실행

  - pip 버전 업데이트

  - venv에서 Django 설치



- 인터프린터 설정 오류

`Unable to import 'django.~'` 발생 시, VScode 왼쪽 하단의 Python 3.X.X클릭 후 인터프린터 변경



- 장고 기본 명령어

`django-admin startproject <프로젝트명>`: 프로젝트 생성
`python manage.py startapp <앱이름>`: 프로젝트의 앱 생성
`python manage.py runserver`: 프로젝트 실행



- DB연동 [[관련링크]](https://cjh5414.github.io/django-rest-framework/)

  - Docker설치 후 mariaDB설치

  - mariaDB에서 database생성

  - Django의 settings.py 설정

    ```python
    DATABASES = {
    	'default': {
    		'ENGINE' : 'django.db.backends.mysql',
    		'NAME' : '<database이름>',
    		...
    		'PORT' : '3306'
    	}
    }
    ```

    

- rest framework

  - `pip djangorestframework`: rest framework 설치

  - settings.py `INSTALLED_APPS`에 'rest_framework' 구문추가

  - `Django`에서 사용할 모델작성

    - `App.models.py`에 모델생성 후 직렬 변환기 생성 및 코딩
    - Django Tutorial Part 3: Using models [[관련링크]](https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Models)

  - 마이그레이터 관련 명령어

    `python manage.py makemigrations`: Model 파일을 기반으로 마이그레이션 파일 생성

    `python manage.py migrate`: 마이그레이션 파일 동기화



---

- 수정할 내용

1. models에서 정수값은 어떻게 입력했는지?
2. 라우터에 대한 내용
    ★배포는 war파일로 배포가능(https://jythonbook-ko.readthedocs.io/en/latest/JythonDjango.html) 애플리케이션 배포
    -> 자이썬

20210131 계획
0. git을 총괄 프로젝트(Release), front, back 만들기 
1. 칼럼추가하는것에 대한 정보 추가로 찾아보기



20210221 (★★★★★ 중요)

​	0. 전공필수, 전공선택 페이지부분 관련 로직으로 인해 프&백 회의 예정

