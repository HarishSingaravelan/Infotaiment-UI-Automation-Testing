pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps { checkout scm }
        }

        stage('Setup Environment') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Start Backend Server') {
            steps {
                sh '. venv/bin/activate && nohup uvicorn main:app --host 127.0.0.1 --port 8000 &'
                sleep 5
            }
        }

        stage('Run Smoke Tests') {
            steps {
                sh '. venv/bin/activate && pytest tests/smoke -v --maxfail=1 --html=smoke_report.html'
            }
        }

        stage('Run Regression Tests') {
            steps {
                sh '. venv/bin/activate && pytest tests/regression -v --html=regression_report.html'
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: '*.html', fingerprint: true
            }
        }
    }

    post {
        success { echo '✅ All infotainment tests passed!' }
        failure { echo '❌ Build failed — vehicle system validation errors detected!' }
    }
}
