## [flask-migrate](https://flask-migrate.readthedocs.io/en/latest/)
* init : `flask db init`
* create empty migration file : `flask db revision -m "create {name} table"`
* create auto-generate migrate file : `flask db migrate -m "create {name} table"`
    * `model에 설정된대로 revision 파일을 만들어주기 때문에 편리하다.`
    * `migrations/env.py의 target_metadata에 db.Model.metadata를 넣어줘야 한다.`
* db upgrade : `flask db upgrade`
* db downgrade : `flask db downgrade`

## 서버 실행
`set FLASK_APP=flask set FLASK_ENV=development`
`flask run`
