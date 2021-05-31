pipeline {
    agent { dockerfile true }
    stages {
        stage('Test Versnio') {
            steps {
                sh 'python -V'
            }
        }

        stage('Testing') {
            steps {
                sh 'pytest -v ldap_service/tests.py'
            }
        }

    }
}


