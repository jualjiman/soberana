rom fabric.api import  *
from fabric.colors import green
import cuisine

env.app_dir = 'ford-experience.stg.interalia.net/ford-experience'
env.roledefs = {
    'avaricia': ['web@10.0.0.7'],
} 

@task
def deploy(branch="develop"):
    """
        funcion para actualizar el branch y reiniciar el proyecto
    """
    with cd(env.app_dir):
        print green("actualizando...")
        run("git pull origin %s" % branch)

        print green("recargando wsgi.py...")
        run("touch facebook_pro/facebook_pro/wsgi.py")

        print green("Listo")

@task
def install_pip_dependences():
    print green("INSTALLING PIP DEPENDENCES")
    print green("changing env")
    run("source ../ita-env/bin/activate")
    print green("installing")
    run("pip install -r requirements.txt")


