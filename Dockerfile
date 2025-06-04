FROM python:3.9-slim

# Set the working directory
WORKDIR /workspaces/mindstone-py

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /workspaces/mindstone-py

CMD ["bash"]