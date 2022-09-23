## Start machine learning project.

###  software and Account Requirement.

1. Github Account : https://github.com
2. Heroku Account : https://dashboard.heroku.com/apps
3. VS code IDE : https://code.visualstudio.com/download
4. GI cli : https://git-scm.com/downloads
5. [GIT Documentation] (https://git-scm.com/docs/gittutorial)


Creating conda environment

Conda create -p venv python== 3.7 -y

conda activate venv/

or

conda activate venv


pip install -r requiremnets.txt

To add files git

or

git add

or

git add <file_name>


Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status

git status

To check all version maintain by git

git log

To create version/commit all changes by git

git commit -m "message"

To send version/changes to github

git push origin main

To check remote url

git remote -v

To add files to git

git add .

or

git add file_name


 Note: To ignore file or folder from git we can write name of file/folder in .gitignore file


 To check the git status

 git status


 To all version maintained by git

 git log


 To create version/commit all changes by git


git commit -m "message"


To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = anshverma2073@gmail.com
2. HEROKU_API_KEY = 00b62293-c8bf-4545-ba9d-7594b5754e51
3. HEROKU_APP_NAME = machine-regression-app



BUILD DOCKER IMAGE

docker build -t <image_name>:<tagname> .

Note: Image name for docker muat be lowercase


To list docker image

doxker images


Run docker image

docker run -p 5000:5000 -e PORT=5000 (image id)


To check running container in docker

docker ps


to stop docker container


docker stop <container_id>




python setup.py install



Install ipykernel



pip install ipykernel