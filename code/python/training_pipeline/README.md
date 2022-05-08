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

Can also use the requirements.txt.

## Run
The following will run the script in the background and redirect the stdout and stderr into a file called raw.txt.  
`python3 src/pipeline.py config.yml > output/raw.txt 2>&1`  

The output to `stdout` is only required for debugging purposes incase the pipeline fails.

### Performance
Using the example configs with the LSST example data set, can take a while to train.
On windows using an overclocked intel I7-7700K with a Nvidia gtx1070, running a config can take up to three days.
Feature pre-engineering e.g. when using `extraction_fields` in the config uses the GPU, the bag of words method does not.



## Notes
### Pickles
Pickles are created using joblib not actual pickles since they perform better with some types of numpy arrays.
See scikit-learns [Documentation](https://scikit-learn.org/stable/modules/model_persistence.html) on model persistence.  

### LDA topic generation
When small amounts of rows are used (n < 2000), lda_topic generation might fail due to a lack of data.