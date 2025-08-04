Write-Host "Creating virtual environment..." -ForegroundColor Green
python -m venv venv

Write-Host "Activating virtual environment..." -ForegroundColor Green
.\venv\Scripts\Activate.ps1

Write-Host "Installing dependencies..." -ForegroundColor Green
pip install -r requirements.txt

Write-Host "Setup complete!" -ForegroundColor Green
Write-Host "To start the app, run: .\venv\Scripts\Activate.ps1 && python app.py" -ForegroundColor Yellow
Read-Host "Press Enter to continue" 