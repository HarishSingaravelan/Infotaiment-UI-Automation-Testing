pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root:root'
        }
    }

    environment {
        BASE_URL = "http://localhost:8000"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'playwright install --with-deps'
            }
        }

        stage('Start Backend Server') {
            steps {
                sh 'nohup uvicorn main:app --host 0.0.0.0 --port 8000 &'
                sleep 8
            }
        }

        // 🚦 FAST FEEDBACK
        stage('Run Smoke Tests') {
            steps {
                sh 'pytest -m smoke --maxfail=1 --disable-warnings --html=smoke_report.html --self-contained-html'
            }
            post {
                always {
                    archiveArtifacts artifacts: 'smoke_report.html', fingerprint: true
                }
            }
        }

        // 🧪 FULL VALIDATION
        stage('Run Regression Tests') {
            steps {
                sh 'pytest -m regression --disable-warnings --html=regression_report.html --self-contained-html'
            }
            post {
                always {
                    archiveArtifacts artifacts: 'regression_report.html', fingerprint: true
                }
            }
        }
    }

    post {
        failure {
            echo '❌ Build failed — regression or smoke tests failed!'
        }
        success {
            echo '✅ Build passed — all smoke and regression tests succeeded!'
        }
    }
}
