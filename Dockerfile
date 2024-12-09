# Use a base Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the app files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Streamlit will use
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "drug_disease_target_rdf_generator.py", "--server.port=8501", "--server.address=0.0.0.0"]
