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

### 1. Move into the main Django project directory:

```bash
cd backend
```

### 2. Create a Virtual Environment

From the root of the django directory (backend), run the following command to create a virtual environment:

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

\*\* This step should be done everytime we want to do something with python
Activate the virtual environment with the following command:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

Upgrade pip (recommended):

```bash
pip install --upgrade pip
```

Install the required packages from the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 6. Run the Development Server

Start the Django development server:

```bash
python3 manage.py runserver
```
