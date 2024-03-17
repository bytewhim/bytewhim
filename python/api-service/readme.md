# An Introduction to Python FastApi, Flask application docker deployment

## A simple Book Reviews frontend: home-web
<hr/>

`home-web` HTML frontend application

```
+------------+
|  home-web  |
+------------+
```

## APIs: login-api, add-review-api, view-api
<hr/>

`login-api` for user login

```
+------------+     +---------------+
| home-web   +---->+   login-api   |
+------------+     +---------------+

```
Login takes `username`, `password` and redirects to `add-review-api`. <br/>
user details are stored in the users.db<br/>
`users.db` `-->` `CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT, email TEXT, name TEXT)`

```
+------------+     +---------------+    +----------------+
| home-web   +---->+   login-api   +--->+ add-review-api |
+------------+     +---------------+    +----------------+

```


`add-review` stores reviews into `reviews.db` and redirects the page to view-api which shows all reviews received so far

`reviews.db` `-->` `CREATE TABLE IF NOT EXISTS reviews (id INTEGER PRIMARY KEY, book_title TEXT, author TEXT, reviews TEXT)`

```
+------------+     +---------------+    +----------------+    +-----------+
| home-web   +---->+   login-api   +--->+ add-review-api |--->+  view-api | 
+------------+     +---------------+    +----------------+    +-----------+

```
<br/>

`home-web` also offers `view-api`, full architecture of this application as follows

```
+------------+     +---------------+    +----------------+
| home-web   +---->+   login-api   +--->+ add-review-api | 
+-----+------+     +---------------+    +-------+--------+
      |                                         |
      |                                         v
      |                                 +-----------+
      +-------------------------------->+  view-api | 
                                        +-----------+

```


<hr/>
let's get started

```
git clone https://github.com/bytewhim/bytewhim.git 
cd python/api-service/home

docker build -t simple-home-web .
docker images

docker run --network=host --rm --name simple-home-web -p 8080:8080 simple-home-web

cd ../login

docker build -t simple-login-api .
docker images

cd ..

docker run --network=host --rm --name simple-login-api -p 8081:8081 -v ./database/users.db:/database/users.db simple-login-api
```
<br>
docker compose file to automate build and docker run
<br>

```
docker compose build
docker images
docker compose up
```