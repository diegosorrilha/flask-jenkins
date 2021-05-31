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
//     agent { dockerfile true }
//     agent any
    agent {
        docker { image 'python:3.9.5-slim-buster' }
    }
    stages {
        stage ("Test") {
            steps {
                sh "python -V"
                sh "echo vai?"
                sh """
                python -m venv .venv &&
                . .venv/bin/activate &&
                pip install --upgrade pip &&
                pip install -r ${env.WORKSPACE}/requirements/prod.txt &&
                sh 'pytest -v --color=yes ldap_service/tests.py'
                """
            }
        }

        stage('Build') {
            steps {
                script {
                    def message = "New version:"
                    def releaseInput = input(
                        id: 'userInput',
                        message: "${message}",
                        parameters: [
                            [
                                $class: 'TextParameterDefinition',
                                defaultValue: 'uat',
                                description: 'Release candidate',
                                name: 'rc'
                            ]
                        ]
                    )
                    sh "echo $releaseInput"
                    sh "echo building release v=${releaseInput}"
                    sh "docker build -t ldap-service:${releaseInput} ."
                    sh "echo built"
                }

            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "deployed"'
            }
        }

    }
}


