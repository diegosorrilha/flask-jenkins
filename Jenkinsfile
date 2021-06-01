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
        stage ("Install dependecies") {
            steps {
                sh "python -V"
                sh "echo vai?"
                sh """
                python -m venv .venv
                . .venv/bin/activate &&
                pip install --upgrade pip &&
                pip install -r ${env.WORKSPACE}/requirements/prod.txt
                """
            }
        }

        stage ("Test") {
            steps {
                sh "echo vai?"
                sh """
                . .venv/bin/activate
                pytest -v --color=yes ldap_service/tests.py
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
//
// ldapsearch -h vedir.srv.hcvlny.cv.net -p 389 -D uid=appuser,ou=appadm,o=entitlement -w PaBlAn0 -b ou=roles,o=entitlement "(&(Accountnumber=0783767649501)(objectClass=CVCSDPRole))" | egrep "attribute2|acctfta"
//
// ldapsearch -h vedir.srv.hcvlny.cv.net -p 389 -D uid=appuser,ou=appadm,o=entitlement -w PaBlAn0 -b ou=ocmrlineup,o=entitlement "(&(OCMRCorpFTA=7837-22)(objectClass=CVCSDPLineupMap))" | egrep OCMRLaBoxLineupID | sort -u
//
// ldapsearch -h vedir.srv.hcvlny.cv.net -p 389 -D uid=appuser,ou=appadm,o=entitlement -w PaBlAn0
//
//
// ----
//
// ldapsearch <previous_options> "(object_type)=(object_value)" <optional_attributes>
//
// Finding all objects in the directory tree
// ldapsearch -x -b <search_base> -H <ldap_host> -D <bind_dn> -W "objectclass=*"
//
// Finding user accounts using ldapsearch
// ldapsearch -x -b <search_base> -H <ldap_host> -D <bind_dn> -W "objectclass=account"
//
//
//
//
//
