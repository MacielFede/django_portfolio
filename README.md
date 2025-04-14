# 📂 Project Structure

```markdown
├── venv/ # Virtual environment
├── backend/ # Main Django project directory
├── frontend/ # Generated Frontend project directory
├── requirements.txt # Python dependencies
└── README.md # Project instructions (this file)
```

# ✅ Requirements

- Python 3.8+

# Setup Instructions

Follow the steps below to set up and run the project locally.

### 1. Create a Virtual Environment

From the root of the django directory (backend), run the following command to create a virtual environment:

```bash
python3 -m venv venv
```

### 2. Activate the Virtual Environment

\*\* This step should be done to enter the venv cmd
Activate the virtual environment with the following command:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

Upgrade pip (recommended):

```bash
pip install --upgrade pip
```

Install the required packages from the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 4. Run the Development Server

Start the Django development server:

```bash
python3 manage.py runserver
```

# Configurations

### Run migrations

```bash
python3 manage.py migrate
```

### Create a superuser

```bash
python3 manage.py createsuperuser
```
