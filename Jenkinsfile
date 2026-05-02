pipeline {
    agent any

    

    environment {
        VENV = '.venv'
        
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Anubhavsikka16/catawiki_project.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv $VENV
                . $VENV/bin/activate
                pip install --upgrade pip
                pip3 install pytest-playwright
                pip install allure-pytest
                pip install pytest-html
                pip install pytest-xdist 
                pip install Faker
                pip3 install python-dotenv
                '''
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                sh '''
                . $VENV/bin/activate
                playwright install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                . $VENV/bin/activate

                mkdir -p html_reports
                mkdir -p allure-reports

                pytest -n 3 -v -s \
                
                --alluredir=allure-reports \
                --html=html_reports/test_report.html
                """
            }
        }


        stage('Archive HTML Report') {
            steps {
                archiveArtifacts artifacts: 'html_reports/*.html', fingerprint: true
            }
        }
    }

    post {
        always {
            allure(
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-reports']]
            )
        }
    }
}