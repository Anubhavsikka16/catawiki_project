pipeline {
    agent any

    tools {
        // Optional: if Python is configured in Jenkins
        // python 'Python3'
    }

    environment {
        ENV = "qa"
        HEADLESS = "true"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm // Checkout code from the repository
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install --upgrade pip
                    .venv/bin/pip install -r requirements.txt
                    .venv/bin/playwright install --with-deps
                '''
            }
        }

        stage('Run Tests in Parallel') {
            steps {

                steps {
                withCredentials([usernamePassword(
                    credentialsId: 'qa-login-creds',
                    usernameVariable: 'TEST_EMAIL',
                    passwordVariable: 'TEST_PASSWORD'
                )]) {

                    catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {

                        sh '''
                            mkdir -p allure-results

                            export TEST_EMAIL=$TEST_EMAIL
                            export TEST_PASSWORD=$TEST_PASSWORD

                            .venv/bin/python -m pytest tests/ \
                                -v -s \
                                -n auto \
                                --dist=loadfile \
                                --alluredir=allure-results
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            allure results: [[path: 'allure-results']]
        }

        success {
            echo "✅ Tests Passed Successfully"
        }

        unstable {
            echo "⚠️ Some tests failed (unstable build)"
        }

        failure {
            echo "❌ Pipeline Failed"
        }

        cleanup {
            deleteDir()
        }
    }
}
