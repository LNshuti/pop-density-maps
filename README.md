## Population Density Maps 
[This](https://pop-density-maps.streamlit.app/) Streamlit Python application transforms the Colab Notebook developed by Steven Kent into an interactive tool for exploring housing density by country. Users can enter a 3-letter country code from a provided list, and the application will generate a housing density map for the selected country.

## Technology Stack 
1. [Prototype:](https://pop-density-maps.streamlit.app/) Python Streamlit 
2. Production Deployment: Modal Labs 

## How to clone and run this app on your machine

```python
# Clone this repo
git clone https://github.com/LNshuti/pop-density-maps.git
```

```python
# Step 2: Create an isolated environment to manage dependencies
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

## References 
1. **Stephen Kent**. Egypt Buildings. A Google Colab Notebook for Querying S3 Data and build a Map using Python and SQL. https://github.com/kentstephen/egypt_buildings