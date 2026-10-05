# WikiInfo

A Streamlit-based Wikipedia article search application using structured Wikimedia data.

## How to Run the Project

### 1. Install Git

If Git is not installed, install Git for Windows.

After installation, open Command Prompt (CMD) and check:

```cmd
git --version
```

### 2. Clone the Project

Open CMD and run:

```cmd
git clone https://github.com/Wither134/Wiki_search.git
cd Wiki_search
```

### 3. Create a Virtual Environment

```cmd
python -m venv .venv
```

### 4. Activate the Virtual Environment

```cmd
.venv\Scripts\activate
```

You should see `(.venv)` at the beginning of the command prompt.

### 5. Install Dependencies

```cmd
pip install -r requirements.txt
```

If Streamlit is not installed, run:

```cmd
pip install streamlit
```

### 6. Run the Application

```cmd
streamlit run app.py
```

The application should open automatically in your browser.

If it does not, open:

```text
http://localhost:8501
```

## Using WikiInfo

Enter a topic or Wikipedia article in the search box.

Example searches:

- India
- Cataract
- River
- Python

Click **Search** to view the results.

The application can display:

- Article names
- Descriptions
- Summaries
- Images
- Wikipedia links

## Project Structure

```text
Wiki_search/
├── app.py
├── search.py
├── data_loader.py
├── requirements.txt
├── README.md
├── .gitignore
└── data/
```

## Troubleshooting

### Git is not recognized

If you see:

```text
'git' is not recognized as an internal or external command
```

Install Git for Windows, close CMD, open a new CMD window, and try again.

### Streamlit is not recognized

Make sure the virtual environment is activated:

```cmd
.venv\Scripts\activate
```

Then install Streamlit:

```cmd
pip install streamlit
```

Then run:

```cmd
streamlit run app.py
```
