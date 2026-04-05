# devops-demo
Repo to demo modern devops stack. 

## Prequisites
1. [Install Git](https://git-scm.com/install/linux)
2. [Install Python 3.13 in your local environment.](https://www.python.org/downloads/) 
2. [Install pip]()
## Local Environment Setup and Testing
1. Git clone the repo
    ```bash
    git clone "https://github.com/mohzim/devops-demo.git"    source venv/bin/activate
    ```

2. Activate Virtual environment and add dependencies
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Run and verify pytest test results
    ```bash
    python3 -m pytest   
    ```
4. Run local flask instance
    ```bash
    flask --app src/app.py run
    ```

5. Deactivate virtual environment
    ```bash
    deactivate   
    ```

## Kubernetes Setup

## Notes/To Do
