pipeline {
//     agent { dockerfile true }
    agent any
    stages {

        stage('Test') {
            steps {

            }
        }

//         stage('Testing') {
//             steps {
//                 sh 'pytest -v --color=yes ldap_service/tests.py'
//             }
//         }

        stage('Build') {
            steps {
                script {
//                     def version = readFile encoding: 'utf-8', file: '__version__.py'
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
                    sh """
                    echo ${releaseInput}
                    sh 'echo building release v=${releaseInput}'
                    sh 'docker build -t ldap-service:${releaseInput} .'
                    sh 'echo "built"'
                    """
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


