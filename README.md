### Instructions for running the code
1. Executable file is src/main.py
2. For execution run with the environment variable `RESOURCES_FOLDER` as following:
    ```
    RESOURCES_FOLDER="/path/to folder" python src/main.py
    ```
        - Inside the `RESOURCES_FOLDER` create the file *'data_source.csv'* file. This is the CSV file used as the input for this program.
3. For running the code from the VS Code, create `.env` file with the following:
    ```
    RESOURCES_FOLDER="/path/to folder"
    ```
4. The output of this program will be the list of CSV files created within the `RESOURCES_FOLDER/out`
        - The main file is the `driver.csv` with the main level of language - count histogram
        - Other `csv` files are Components distribution within a language