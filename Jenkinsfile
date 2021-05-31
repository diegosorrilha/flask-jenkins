pipeline {
//     agent { dockerfile true }
    agent any
    stages {
        stage('Start') {
            steps {
                sh 'vai começar'
            }
        }

        stage('Testing') {
            steps {
                sh 'pytest -v --color=yes ldap_service/tests.py'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t ldap-service:latest .'
                sh 'echo "built"'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "deployed"'
            }
        }

    }
}


