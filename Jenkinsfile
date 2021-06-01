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
//         stage ("Install dependecies") {
//             steps {
//                 sh "python -V"
//                 sh "echo 'VAI CAPETAA'"
//             }
//         }

//     agent { dockerfile true }
//     agent any
//     agent {
//         docker { image 'python:3.9.5-slim-buster' }
//     }
//     stages {
//         stage ("Install dependecies") {
//             steps {
//                 sh "python -V"
//                 sh "echo vai?"
//                 sh """
//                 python -m venv .venv
//                 . .venv/bin/activate &&
//                 pip install --upgrade pip &&
//                 pip install -r ${env.WORKSPACE}/requirements/prod.txt
//                 """
//             }
//         }
//
        stage ("Test") {
            steps {
                sh """
                pytest -v --color=yes ldap_service/tests.py
                """
            }
        }

        stage('Build') {
            steps {
                sh "echo 'teste'"
//                 def customImage = docker.build("my-image:${env.BUILD_ID}")
//
//                 customImage.inside {
//                     sh 'pytest -v --color=yes ldap_service/tests.py'
//                 }
            }
        }

//         stage('Build') {
//             steps {
//                 script {
//                     def message = "New version:"
//                     def releaseInput = input(
//                         id: 'userInput',
//                         message: "${message}",
//                         parameters: [
//                             [
//                                 $class: 'TextParameterDefinition',
//                                 defaultValue: 'uat',
//                                 description: 'Release candidate',
//                                 name: 'rc'
//                             ]
//                         ]
//                     )
//                     sh "echo $releaseInput"
//                     sh "echo building release v=${releaseInput}"
//                     sh "docker build -t ldap-service:${releaseInput} ."
//                     sh "echo built"
//                 }
//
//             }
//         }
//
//         stage('Deploy') {
//             steps {
//                 sh 'echo "deployed"'
//             }
//         }

    }
}