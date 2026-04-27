# DevOps CI Demo

A simple web application with a CI/CD pipeline demonstration using Git, Selenium, and Docker.

## Project contents

- `index.html` — simple static web page
- `styles.css` — basic styling
- `app.js` — button interaction logic
- `Dockerfile` — builds an NGINX container for deployment
- `tests/test_selenium.py` — Selenium functionality test
- `requirements.txt` — Python dependencies for Selenium testing

## Task implementation

1. **Create repository and upload application**
   - Project created in `devops-ci-demo` with HTML, CSS, JavaScript, and pipeline artifacts.
2. **Branch, commit, merge**
   - Use Git locally to create a branch, commit changes, and merge into `main`.
3. **Selenium test**
   - `tests/test_selenium.py` verifies multiple functionalities of the web application including message display, counter, text input, dark mode toggle, calculator, todo list, and random color generator.
4. **Docker build and deployment**
   - `Dockerfile` packages the static site with NGINX.

## Setup and run locally

### Serve the app locally

1. Open a terminal in `devops-ci-demo`.
2. Start a local server:
   ```powershell
   python -m http.server 8000
   ```
3. Open `http://localhost:8000` in a browser.

### Run the Selenium test

1. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
2. Start the local server from the project root.
3. Run the test:
   ```powershell
   python -m pytest tests/test_selenium.py
   ```

### Build and run Docker image

```powershell
docker build -t devops-ci-demo:latest .
docker run --rm -p 8080:80 devops-ci-demo:latest
```

Then open `http://localhost:8080`.

## Notes

- The CI pipeline uses Git for version control, Selenium for testing, and Docker for deployment.
