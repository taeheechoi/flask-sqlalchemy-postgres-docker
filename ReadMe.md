Run

    docker-compose up --build -d
    docker-compose stop

    export FLASK_APP=app.py
    flask fun

Postman

    http://127.0.0.1:5000 
    
        [{"id": 1, "name": "Me", "title": "MyTitle", "phone": "123-234-4567"}, 
        {"id": 2, "name": "You", "title": "YourTitle", "phone": "123-234-4567"}]

    http://127.0.0.1:5000/add
        {"name": "House", "title": "House", "phone": "123-234-4567"}

request.get_json() always returning None

    changed get_json() to get_json(force=True)


PgAdmin to Postgres

    Type 0.0.0.0:8080 on browser to access to pg admin
    Enter email 'user@domain.com' and password 'password1'

    Pg admin)
        Right click on Servers
        Create Server (Server info from dabase.conf)
            General: Name: contact
            Connection: Host name: postgres
            Port: 5432
            Maintenance database: contact
            Username: user1
            Password: password1


Reference

    https://medium.com/@hmajid2301/implementing-sqlalchemy-with-docker-cb223a8296de

    https://kite.com/blog/python/flask-sqlalchemy-tutorial/

    https://github.com/dvf/blockchain/issues/105