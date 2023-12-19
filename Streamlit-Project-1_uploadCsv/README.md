### About :
In this project,  I have learnt how to use **`Streamlit`** `Python library` for Simple UI as a webservice.
Here we can upload **`CSV`** and query on the data in the CSV. Just like we do query on table using `SQL` query.
```SQL
    SELECT * FROM table_name;
    OR SELECT * FROM table_name LIMIT 10
```
**Remark:** Here table means  `csv file name` <br>
`Source`: The CSV i have provide in this project is taken from 
Link : https://www.stats.govt.nz/large-datasets/csv-files-for-download/
## INFO: 
Scroll down, you will get to know how you can get this project and install locally in you machine and run and **HAVE FUN**

### Snippets :
## HOME:
![image](./SS_APP/1_Home_beforeUploadingFile.jpg?raw=true)

## After CSV uploaded:
![image](./SS_APP/2_Home_AfterUploadingFile.jpg?raw=true)
![image](./SS_APP/3_Home_beforeQuery.jpg?raw=true)

## After Querying:
![image](./SS_APP/4_Home_AfterQUERY.jpg?raw=true)

## Select One Column:
![image](./SS_APP/5_Home_AfterONE_Col_QUERY.jpg?raw=true)

# How to setup Locally:
- Clone the repository to your user home directory and cd into this project
> Use a virtual env
- Clone repo : $ git clone `https://github.com/THENHKHAN/StreamlitLearning.git`
cd Streamlit-Project-1_uploadCsv
- Create a virtualenv: `$ mkvirtualenv env` or `$ python -m venv env` and if its not working then go for virtualWrapper-win i.e.
`$ pip install virtualenvwrapper-win` for **window** and `pip install virtualenvwrapper` for **linux** <br>
- Then create your virtual environment **`mkvirtualenv myEnv`**. Here myEnv will be your virtual environment <br>
- Activate ENV :  RUN- `workon myEnv` <br>
- Install dependencies : `$ pip install -r requirements.txt` and set environment variables <br>
- Run project : `$ python csvUploadAndQueryFromPandaSQL.py`
