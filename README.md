## How to use the Dockerfile

1. **Update requirements.txt**:
   Ensure that your `requirements.txt` file specifies compatible versions of Flask and Werkzeug:
   ```plaintext
   Flask==2.0.3
   Werkzeug==2.0.3
   ```

2. **Build the Docker image**:
   Open a terminal and navigate to the directory containing the Dockerfile. Run the following command to build the Docker image:
   ```sh
   docker build -t flask-app .
   ```

   If you encounter a permission denied error, you may need to run the command with `sudo`:
   ```sh
   sudo docker build -t flask-app .
   ```

3. **Run the Docker container**:
   After the image is built, run the container using the following command:
   ```sh
   docker run -p 5000:5000 flask-app
   ```

   If you encounter a permission denied error, you may need to run the command with `sudo`:
   ```sh
   sudo docker run -p 5000:5000 flask-app
   ```

4. **Access the Flask application**:
   Open a web browser and go to `http://localhost:5000` to see the Flask application running.

## CI Automation

The project uses GitHub Actions to automate the CI process. The CI workflow is defined in the `.github/workflows/ci.yml` file.

### CI Process for Pull Requests

1. **Trigger**: The CI process runs automatically on every pull request to any branch.
2. **Steps**:
   - **Checkout code**: The workflow checks out the code from the repository.
   - **Set up Python**: The workflow sets up Python 3.9.
   - **Install dependencies**: The workflow installs the dependencies specified in `requirements.txt`.
   - **Build Docker image**: The workflow builds the Docker image for the Flask application.
   - **Run basic tests**: The workflow runs a basic test step (`echo "Test"`).

### CI Process for Merges to Main Branch

1. **Trigger**: The CI process runs automatically on every merge to the `main` branch.
2. **Steps**:
   - **Checkout code**: The workflow checks out the code from the repository.
   - **Set up Python**: The workflow sets up Python 3.9.
   - **Install dependencies**: The workflow installs the dependencies specified in `requirements.txt`.
   - **Build Docker image**: The workflow builds the Docker image for the Flask application.
   - **Run basic tests**: The workflow runs a basic test step (`echo "Test"`).
   - **Log in to GitHub Container Registry**: The workflow logs in to the GitHub Container Registry using the provided GitHub token.
   - **Push Docker image**: The workflow tags and pushes the Docker image to the GitHub Container Registry under the user's account.
