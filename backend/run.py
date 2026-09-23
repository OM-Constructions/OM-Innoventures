import os
import sys
import uvicorn

# Ensure the backend directory is in the python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    print(f"🚀 Starting OM Innoventures & Build AI Technologies local server on http://localhost:{port}")
    uvicorn.run("app.main:app", host=host, port=port, reload=True)
