// node {
//     checkout scm
//
//     def customImage = docker.build("my-image:${env.BUILD_ID}")
//
//     customImage.inside {
//         sh 'pytest -v --color=yes ldap_service/tests.py'
//     }
//     sh "echo ${c.id}"
//
// }
// sh "docker logs ${c.id}"
//
pipeline {
    agent {
        // Equivalent to "docker build -f Dockerfile.build --build-arg version=1.0.2 ./build/
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
                echo "New Version: ${env.GIT_COMMIT} "
                sh "docker build -t ldap-service:${env.GIT_COMMIT} ."
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "deployed"'
            }
        }

    }
}