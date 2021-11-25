# Training pipeline

## Dependencies
`pip install pyyaml`  
`pip install scikit-learn`  
`pip install pandas`  
`pip install arrow`  
`pip install seaborn`  
`pip install ipython`    
`pip install jinja2`  
`pip install tabulate`

## Run
The following will run the script in the background and redirect the stdout and stderr into a file called raw.txt.
` python3 src/pipeline.py config.yml > output/raw.txt 2>&1`