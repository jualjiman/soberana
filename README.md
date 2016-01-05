# soberana

Portal del Instituto Tecnológico de Acapulco

## Prerequisites
+ [Git](http://git-scm.com/)
+ [Virtualenv](https://virtualenv.readthedocs.org/en/latest/index.html)

## Configuring your virtual environment and project

1. Fork the repo with your GitHub's user account

2. Clone your fork

    ```bash
    $ git clone --recursive git@github.com:{ your username }/soberana.git
    ```

3. Create your virtualenv folder and use it as source
    ```bash
    virtualenv env-ita
    source env-ita/bin/activate
    ```

4. Install project requeriments
    ```bash
    pip install -r soberana/requeriments/{dev|production}
    ```

5. Load groups fixture
    ```bash
    cd soberana
    ./manage.py loaddata groups.json
    ```
6. Run django test server
    ```bash
    ./manage.py runserver
    ```
