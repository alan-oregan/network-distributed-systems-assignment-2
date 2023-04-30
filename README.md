# Network Distributed Systems Assignment 2

## Assignment outline

> In this CA, you are required to implement a cloud-based hosting solution for a Flask based Python application (Python Anywhere).
> A series of stress tests should then be performed using Locust.
> The idea is to test with a slowly increasing number of users to identify when the server will break. This will validate how many users the server can deal with at any one time.
> We are interested to see if any changes happen when more users are added to the virtual tests.
> Eventually the server will start responding with error codes telling us that it cannot take any more traffic.

## Hosted on AWS EC2 using Elastic Beanstalk and CodePipeline

### [Check it out!](http://spiderwebnet.eu-west-1.elasticbeanstalk.com/)

## How to run Locust tests

### 1. Install Locust

```bash
pip install locust
```

### 2. Start Locust

```bash
cd test
locust
```

Then navigate to <http://localhost:8089/>

You should see this page:

![Locust home page](images/locust-home.jpg)

### 3. (optional) Run the Flask app locally

Install requirements:

```bash
pip install -r requirements.txt
```

Run the Flask app:

```bash
flask run
```

## How to use

### Home

The flask application is a simple template restful application that allows you to append to the URL to customise the page.

![Application Template home](images/flask-app-template.jpg)

## Links to resources

### Virtual Environments

- <https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/>
- <https://docs.python.org/3/library/venv.html>

### Hosting on AWS

1. <https://www.red-gate.com/simple-talk/blogs/deploying-a-nodejs-application-from-github-to-aws-elastic-beanstalk-and-creating-a-ci-cd-aws-codepipeline/>

2. <https://aws.amazon.com/elasticbeanstalk/>

3. <https://aws.amazon.com/codepipeline/>

4. <https://flask.palletsprojects.com/en/2.3.x/deploying/>

5. <https://leonardqmarcq.com/posts/github-actions-cicd-elastic-beanstalk>

6. <https://cloudbytes.dev/aws-academy/run-flask-apps-on-elastic-beanstalk>

### Locust Testing

- <https://www.youtube.com/watch?v=Uai2yZWfM9g>
