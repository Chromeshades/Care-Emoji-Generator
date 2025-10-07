#!/bin/bash

# Care Emoji Generator Web App Startup Script

echo "🤗 Starting Care Emoji Generator Web App..."
echo "============================================"

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found. Please run setup first:"
    echo "   python3 -m venv .venv"
    echo "   source .venv/bin/activate"
    echo "   pip install -r requirements.txt"
    exit 1
fi

# Activate virtual environment
source .venv/bin/activate

# Check if required packages are installed
echo "📦 Checking dependencies..."
python -c "import flask, PIL, requests" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Dependencies missing. Installing..."
    pip install -r requirements.txt
fi

# Create necessary directories
mkdir -p web/app/static/tmp

echo "✅ Dependencies OK"
echo "🚀 Starting web server..."
echo ""
echo "The app will be available at:"
echo "  • http://localhost:5337"
echo "  • http://127.0.0.1:5337"
echo ""
echo "Press Ctrl+C to stop the server"
echo "============================================"

# Change to web directory and run the app
cd web
python main.py