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
