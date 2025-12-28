1)  Import Flask,SQLAlchemy, Migrate and all other components
2)  Set env varioable for migrate to run
    $env:FLASK_APP = "app.py"
    flask db init
    flask db migrate -m "Update"
    flask db upgrade
3)  Create view:
    home : Renders HRML template
    update : Update DB
    delete : delete object
    add : add object to DB
4)  Create jinja tyemplate in HTML to write form data from object returned from home