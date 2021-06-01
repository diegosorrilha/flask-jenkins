pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
        }
    }

    stages {

        stage ("Test") {
            steps {
                sh """
                pytest -v --color=yes ldap_service/tests.py
                """
            }
        }

        stage('Build') {
            steps {
                // sh "docker build -t ldap-service:${env.GIT_COMMIT} ."
                echo "New Version: ldap-service:${env.GIT_COMMIT}"
                echo "Job NAME: ldap-service:${env.JOB_NAME}"
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "deployed with success"'
            }
        }

    }
}