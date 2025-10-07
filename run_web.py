#!/usr/bin/env python3
"""
Web application runner for Care Emoji Generator
"""
import os
import sys

# Add the web directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'web'))

from web.main import app

if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True, host='0.0.0.0', port=5337)