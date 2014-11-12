from fabric.api import  *
from fabric.colors import green,red

env.webapps_dir = '/webapps/'
env.app_dir = '/webapps/ITA/site'
env.env_dir = '/webapps/ITA/ita-env'

env.roledefs = {
    'hitman': ['root@191.101.13.47'],
} 

@task
def supervisor_restart():
    """
        restart project with supervisor
    """
    print red("---SUPERVISOR RESTART---")
    sudo("supervisorctl restart ITA")
    print green("Restarted")

@task
def supervisor_stop():
    """
        stop project with supervisor
    """
    print red("---SUPERVISOR STOP---")
    sudo("supervisorctl stop ITA")
    print green("Stoped")

@task
def supervisor_status():
    """
        get project supervisor status
    """
    print red("---SUPERVISOR STATUS---")
    sudo("supervisorctl status ITA")
    print green("Done")


############################################################################################

# fab deploy:<branch> -R hitman
@task
def git_pull(branch="master"):
    """
        funcion para actualizar el branch y reiniciar el proyecto
    """
    print red("---GIT PULL---")
    with cd(env.app_dir):
        print green("actualizando...")
        run("git pull origin %s" % branch)

        supervisor_restart()

        print green("Listo")

@task
def git_push(branch="master"):
    """
        funcion para hacer push de los cambios del proyecto    
    """
    print red("---GIT PUSH---")
    with cd(env.app_dir):
        print green("actualizando...")
        run("git status")
        run("git add -A")
        run("git commit -m 'subiendo cambios server'")
        run("git push origin %s" % branch)

        print green("Listo")

############################################################################################

#fab create -R hitman
@task
def create():
    """
        creates files, download dependences and download master's branch project
    """
    with cd(env.webapps_dir):
        print red("---CREATE PROJECT---")

        print green("---creating root file---")
        run("mkdir ITA")

        print green("---creating project file and virtualenv---")
        with cd("ITA"):
            run("mkdir logs/")
            run("mkdir run/")
            run("touch logs/gunicorn_supervisor.log")
            run("mkdir site")
            run("virtualenv ita-env")

            print green("---initializing git, adding remote and downloading master---")    
            with cd("site"):
                run("git init")
                run("git remote add origin git@github.com:jualjiman/soberana.git")
                run("git pull origin master")

            print green("---installing pip requeriments---")
            run("source ita-env/bin/activate && pip install -r site/requeriments.txt")


            


###########################################################################################

@task
def django_syncdb():
    """
        funcion para hacer push de los cambios del proyecto    
    """
    print red("---DJANGO SYNCDB---")
    with cd(env.app_dir):
        print green("actualizando...")
        run("source ../ita-env/bin/activate && ./manage.py syncdb")

        print green("Listo")

@task
def pip_install(package="master"):
    """
        instalar un paquete con pip
    """
    print red("---PIP INSTALL---")
    with cd(env.env_dir):
        print green("installing...")
        run("source bin/activate && pip install %s" % package)

        print green("Listo")

#######################################LOCALES############################################
# env.webapps_dir_local = '/home/alberto/git/'
# env.app_dir_local = '/webapps/ITA/site'
# env.env_dir_local = '/webapps/ITA/ita-env'

env.webapps_dir_local = '/home/alberto/git/'
env.app_dir_local = '/home/alberto/git/django/ita/ita/ita-website/'
env.env_dir_local = '/webapps/ITA/ita-env'

@task
def git_push_local(description="subiendo localmente"):
    """
        subir los avances del sitio localmente
    """
    print red("---GIT PUSH LOCAL---")
    with cd(env.app_dir_local):
        print green("actualizando...")
        local("git status")
        local("git add -A")
        local("git commit -m '%s'" % description)
        local("git push origin master")

        print green("Listo")