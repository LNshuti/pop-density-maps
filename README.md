# Population Density Maps 
[This Streamlit Python](https://pop-density-maps.streamlit.app/) application transforms the Colab Notebook developed by Steven Kent into an interactive tool for exploring housing density by country. Users can enter a 3-letter country code from a provided list, and the application will generate a housing density map for the selected country.

## How to clone and run this app on your machine

```python
# Clone this repo
git clone https://github.com/LNshuti/pop-density-maps.git
```

```python
# Step 2: Create an isolated environment to manage dependencies
cd pop-density-maps
conda env create --file=environment.yaml
```

```python
# Step 3: Install the required python packages
pip install -r requirements.txt 
```

```python 
# Step 5: Run Python Application
streamlit run app.py
```
## How to deploy the app with Docker

```python
# Clone this repo
git clone https://github.com/LNshuti/pop-density-maps.git
```

```python
# Navigate to the repo and build the docker image
cd pop-density-maps
docker build -t pop-density .
```

```python
# Run the application
docker run --rm -p 8501:8501 --name pop-density pop-density 
```

```python
# Navigate to the application by typing the following in a web browser
http://localhost:8501/
```

## References 
1. **Stephen Kent**. Egypt Buildings. A Google Colab Notebook for Querying S3 Data and build a Map using Python and SQL. https://github.com/kentstephen/egypt_buildings