pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Build') {
      steps {
        echo 'Building static web application...'
      }
    }
    stage('Test') {
      steps {
        echo 'Running Selenium test script placeholder...'
        sh 'python -m pytest tests' 
      }
    }
    stage('Docker Build') {
      steps {
        script {
          dockerImage = docker.build('devops-ci-demo:latest')
        }
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deployment can be completed by running the Docker container.'
      }
    }
  }
}
