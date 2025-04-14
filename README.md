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

- Django

- Pillow

# Setup Instructions

Follow the steps below to set up and run the project locally.

### 1. Create a Virtual Environment

From the root directory of the project, run the following command to create a virtual environment:

```bash
py -m venv venv
```

### 2. Activate the Virtual Environment

Activate the virtual environment with the following command:

```bash
venv\Scripts\activate
```

> **Note for macOS/Linux users**: Use the following command instead:
>
> ```bash
> source venv/bin/activate
> ```

### 3. Install Dependencies

Install the required packages from the requirements.txt file:

```bash
pip install -r requirements.txt
```

Upgrade pip (recommended):

```bash
python -m pip install --upgrade pip
```

Install Pillow (if not already included in requirements.txt):

```bash
python -m pip install Pillow
```

### 5. Run the Development Server

Move into the main Django project directory:

```bash
cd webpersonal
```

Start the Django development server:

```bash
python manage.py runserver
```
