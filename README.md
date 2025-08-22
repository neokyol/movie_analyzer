# Movie Analyzer

Python-backed movie analyzer to provide calculated suggestions.

Current implementation ingests the movie list from a CSV file.

---

## 🚀 Setup

### 1. Clone the repository
    git clone https://github.com/neokyol/movie_analyzer.git
    cd movie_analyzer

### 2. Create and activate a virtual environment
    python3 -m venv .venv
    source .venv/bin/activate   # on Linux / macOS
    .venv\Scripts\activate      # on Windows (PowerShell)

### 3. Install dependencies

    pip install -r requirements.txt


---

## ▶️ Running the Application

Run the main entrypoint:

    python main.py

---

## 🧪 Running Tests

This project uses pytest.

Run all tests from the project root:

    pytest

Run tests with verbose output:

    pytest -vv

Run only one test file:

    pytest tests/unit/my_package/test_something.py

---

## ⚙️ Notes

- Tests are configured with pytest.ini so imports from movie_analyzer work correctly.
- If you install the package in editable mode (pip install -e .), pytest will also work without extra configuration.
