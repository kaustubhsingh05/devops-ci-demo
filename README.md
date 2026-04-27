# DevOps CI Demo

A simple web application with a CI/CD pipeline demonstration using Git, Jenkins, Selenium, and Docker.

## Project contents

- `index.html` — simple static web page
- `styles.css` — basic styling
- `app.js` — button interaction logic
- `Dockerfile` — builds an NGINX container for deployment
- `Jenkinsfile` — declarative pipeline for checkout, test, and Docker build
- `tests/test_selenium.py` — Selenium functionality test
- `requirements.txt` — Python dependencies for Selenium testing

## Task implementation

1. **Create repository and upload application**
   - Project created in `devops-ci-demo` with HTML, CSS, JavaScript, and pipeline artifacts.
2. **Branch, commit, merge**
   - Use Git locally to create a branch, commit changes, and merge into `main`.
3. **Selenium test**
   - `tests/test_selenium.py` verifies that clicking the app button shows the expected message.
4. **Jenkins job integration**
   - `Jenkinsfile` defines a Jenkins Pipeline.
   - `jenkins-job-config.xml` contains a sample GitHub-integrated Jenkins Pipeline job configuration.
5. **Docker build and deployment**
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

## Jenkins job configuration

Use `jenkins-job-config.xml` as a sample pipeline job definition for Jenkins to track this GitHub repository.

### Example GitHub job steps

- Create a new Pipeline job in Jenkins.
- Configure SCM as Git.
- Set repository URL to the GitHub repo.
- Use the `Jenkinsfile` from repository.

## Notes

- Replace `https://github.com/<your-user>/devops-ci-demo.git` with the actual repository URL in `jenkins-job-config.xml`.
- The Jenkins pipeline in `Jenkinsfile` expects Python and Docker available on the Jenkins agent.
