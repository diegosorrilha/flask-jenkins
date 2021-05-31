pipeline {
//     agent { dockerfile true }
    agent any
    stages {
        stage('Docker') {
            steps {
                sh 'docker build -t ldap-service:latest .'
                sh 'python -V'
            }
        }

        stage('Testing') {
            steps {
                sh 'pytest -v ldap_service/tests.py'
            }
        }

        stage('Build') {
            steps {
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


