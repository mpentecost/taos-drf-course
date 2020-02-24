              _______       ____   _____   _           _ _     _ _
             |__   __|/\   / __ \ / ____| | |         (_) |   | (_)
                | |  /  \ | |  | | (___   | |__  _   _ _| | __| |_ _ __   __ _
                | | / /\ \| |  | |\___ \  | '_ \| | | | | |/ _` | | '_ \ / _` |
                | |/ ____ \ |__| |____) | | |_) | |_| | | | (_| | | | | | (_| |
                |_/_/    \_\____/|_____/  |_.__/ \__,_|_|_|\__,_|_|_| |_|\__, |
                                                                          __/ |
                                                                         |___/
                  _____ _____  _____            _ _   _       _____  _____  ______
            /\   |  __ \_   _|/ ____|          (_) | | |     |  __ \|  __ \|  ____|
           /  \  | |__) || | | (___   __      ___| |_| |__   | |  | | |__) | |__
          / /\ \ |  ___/ | |  \___ \  \ \ /\ / / | __| '_ \  | |  | |  _  /|  __|
         / ____ \| |    _| |_ ____) |  \ V  V /| | |_| | | | | |__| | | \ \| |
        /_/    \_\_|   |_____|_____/    \_/\_/ |_|\__|_| |_| |_____/|_|  \_\_|


### Installation
1.  Make sure you have Docker Installed on your Desktop/Mac: [link](https://www.docker.com/products/docker-desktop)
2.  In the root directory of this repo, run `docker-compose build` to build the containers

### Starting the Test Server
1. In the root directory of this repo, run `docker-compose up`
2. To stop, type `CTL-c` or `docker-compose down`
3. Browse to `http://127.0.0.1:8000` in your browser

### Commands
**You can run the following commands to create and apply database migrations**
1. Start a shell `docker-compose run --rm web /bin/bash` on the container
2. run `python manage.py makemigrations` to create new migration files
3. run `python manage.py migrate` to apply changes to your database  
  
**To run a Django shell**
1. Start a shell `docker-compose run --rm web /bin/bash` on the container
2. Run `python manage.py shell`  

**To create a superuser for the admin** *http://127.0.0.1:8000/admin*
1. Start a shell `docker-compose run --rm web /bin/bash` on the container
2. run `python manage.py createsuperuser` and follow the prompts

**To completely prune your local Docker environment and start over**
1. `docker-compose stop`
2. `docker system prune --volumes -f`
3. `docker image prune -af`  

**Documentation Links:**  
[Django](https://docs.djangoproject.com/en/3.0/)  
[Django Rest Framework](https://www.django-rest-framework.org/)  
[FactoryBoy](https://factoryboy.readthedocs.io/en/latest/)  
