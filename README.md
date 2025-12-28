# Flask ToDo App ✅

A small Flask application to manage a To-Do list — demonstrates basic routing, templates, and database migrations using Flask-Migrate.

## Features
- Add, update and delete to-do items
- Jinja2 templates in `templates/` (currently `base.html`)
- Database migrations using Flask-Migrate

## Prerequisites
- Python 3.10+ (installed)
- Windows PowerShell (commands below use PowerShell syntax)

## Setup
1. Create and activate a virtual environment:
   - python -m venv venv
   - PowerShell: `python -m venv venv
                  venv\Scripts\activate`

2. Install dependencies:
   - `pip install -r requirements.txt`

3. Initialize and run database migrations (only if you use SQLAlchemy & Flask-Migrate):
   - ` $env:FLASK_APP = "app.py"`
   - `flask db init`
   - `flask db migrate -m "Initial migration"`
   - `flask db upgrade`

## Running the app
- Start the app directly:
```powershell
& .\venv\Scripts\python.exe app.py
```
- Or export `FLASK_APP` and use `flask run`:
```powershell
$env:FLASK_APP = "app.py"
flask run
```

By default the app runs on `http://127.0.0.1:5000/`.

> Tip: Add the usual guard in `app.py` so it only runs when executed directly:
>
> ```python
> if __name__ == "__main__":
>     app.run(debug=True)
> ```

## Routes (example)
- `/` - renders `base.html` (home page)
- Add other routes (e.g. `/add`, `/update`, `/delete`) as your app grows

## Troubleshooting
- If the page appears blank in the browser, check:
  - The Flask server is running and listening on `127.0.0.1:5000`
  - You are opening `http://127.0.0.1:5000/` (not `file://`)
  - Browser DevTools for console/network errors
  - Terminal output for Python/Flask errors

## Contributing
Contributions and improvements welcome — open a PR or issue describing the change.

## License
This project is available under the MIT License.
