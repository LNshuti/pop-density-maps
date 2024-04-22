# Population Density Maps 
[This Streamlit Python](https://pop-density-maps.streamlit.app/) application transforms the Colab Notebook developed by Steven Kent into an interactive tool for exploring housing density by country. Users can enter a 3-letter country code from a provided list, and the application will generate a housing density map for the selected country.

## DEMO
[Demo Video](https://www.loom.com/embed/4917be6878b5402393d43d99d91bf105?sid=5e2fbae0-0169-4aff-8644-2c3b1074ceba)

<!DOCTYPE html>
<html>
<head>
    <title>Demo 2</title>
</head>
<body>
    <div style="position: relative; padding-bottom: 56.25%; height: 0;">
        <iframe src="https://www.loom.com/embed/4917be6878b5402393d43d99d91bf105?sid=6eba42b5-75c4-4eab-839c-7247cde3fde6" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>
</body>
</html>

## How to clone and run this app on your machine

#### Step 1. Clone this repo
```python
git clone https://github.com/LNshuti/pop-density-maps.git
```
#### Step 2: Create an isolated environment to manage dependencies
```python
cd pop-density-maps
conda env create --file=environment.yaml
```
#### Step 3: Install the required python packages
```python
pip install -r requirements.txt 
```
#### Step 5: Run Python Application
```python 
streamlit run app.py
```

## How to deploy the app with Docker
#### Build the docker image
```python
docker build -t pop-density .
```
#### Run the application
```python
docker run --rm -p 8501:8501 --name pop-density-container pop-density 
```
#### Navigate to the application by typing the following in a web browser
```python
http://localhost:8501/
```

## References 
1. **Stephen Kent**. Egypt Buildings. A Google Colab Notebook for Querying S3 Data and build a Map using Python and SQL. https://github.com/kentstephen/egypt_buildings