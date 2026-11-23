# Flask & MongoDB Assignment

## Requirements
- Python 3.10 or newer
- A MongoDB Atlas cluster and database user
- Network access from your machine to the Atlas cluster

## Run locally (macOS)
```bash
cd Flask_and_MongoDB_Riyaz
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and replace the sample `MONGO_URI` with your MongoDB Atlas connection string. Do not commit `.env` to GitHub.

Start the application:
```bash
python app.py
```
Open http://127.0.0.1:5000

## Test Task 1: JSON API
Open http://127.0.0.1:5000/api or run:
```bash
curl -i http://127.0.0.1:5000/api
```
The route reads `data.json` and returns the JSON list.

## Test Task 2: MongoDB form
1. Open http://127.0.0.1:5000
2. Enter a name, email and message.
3. Submit the form.
4. On successful insert, the browser redirects to `/success` and displays **Data submitted successfully**.
5. If MongoDB is unavailable or the insert fails, an error appears on the form page without redirecting.

## GitHub
```bash
git init
git add .
git commit -m "Build Flask and MongoDB assignment"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Flask_and_MongoDB_Riyaz.git
git push -u origin main
```
Replace `YOUR_USERNAME` with your GitHub username. If the repository already has a remote, inspect it with `git remote -v` before changing it.

## Screenshots to capture
Save genuine screenshots in the `screenshots/` folder and insert them into `Documentation.docx`:
- `01-project-files.png` — project folder in VS Code or Finder
- `02-installation.png` — dependency installation in terminal
- `03-app-running.png` — Flask server running
- `04-api-response.png` — `/api` JSON response
- `05-form.png` — frontend form
- `06-success.png` — successful submission page
- `07-mongodb-document.png` — inserted document in Atlas
- `08-github.png` — GitHub repository

Do not include database credentials, passwords, or the `.env` file in screenshots or GitHub.
