# 설치 및 설정
* python 3.9 버전 사용
* poetry version 확인 `poetry -V` 없다면 poetry install `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`

* pycharm interpreter를 poetry로 설정
![img.png](img.png)
* 패키지 설치 완료 후 apply -> ok
![img_1.png](img_1.png)

* pycharm terminal 새로 켜서 명령어 실행

## migrate
config에서 mysql 계정, 비밀번호를 개인 local에 설정된대로 변경해주기
`SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{id}:{pw}@localhost:3306/wanted"`

* mysql에서 `create database wanted`
* db upgrade : `flask db upgrade`
* db downgrade : `flask db downgrade`

# test
`pytest`

# 서버 실행
환경 변수 설정 후 실행

`set FLASK_APP=flask`

`set FLASK_ENV=development`

`flask run`


## 호출
### 게시글
생성 : POST `http://127.0.0.1:5000/api/board`
```json
{
    "writer": "james",
    "title": "hello world 23",
    "contents": "1",
    "password": "password"
}
```
목록 : GET `http://127.0.0.1:5000/api/boards`
```json
{
    "id": 2,
    "title": null,
    "writer": null
}
```
갱신 : PUT `http://127.0.0.1:5000/api/board`
```json
{
    "id": 2,
    "title": "1",
    "contents": "wow",
    "password": "password"
}
```
삭제 : DELETE `http://127.0.0.1:5000/api/board`
```json
{
    "id": 2,
    "password": "password"
}
```
### 댓글
생성 : POST `http://127.0.0.1:5000/api/comment`
```json
{
    "writer": "james",
    "board_id": 2,
    "contents": "hello 3",
    "parent_id": null
}
```
목록 : GET `http://127.0.0.1:5000/api/comments`
```json
{
    "board_id": 2,
    "id": null
}
```
