pipeline {
    agent { dockerfile true }
    stages {

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


