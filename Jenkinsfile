pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-u root:root'
        }
    }

    environment {
        VENV = ".venv"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh 'python -m venv $VENV'
                sh ". $VENV/bin/activate && pip install --upgrade pip"
                sh ". $VENV/bin/activate && pip install -r requirements.txt"
                sh ". $VENV/bin/activate && playwright install --with-deps"
            }
        }

        stage('Start Backend Server') {
            steps {
                sh ". $VENV/bin/activate && nohup uvicorn main:app --host 127.0.0.1 --port 8000 &"
                sh 'sleep 5' // wait for server to be ready
            }
        }

        stage('Smoke Tests') {
            steps {
                sh ". $VENV/bin/activate && pytest tests/smoke --maxfail=1 --disable-warnings --html=smoke_report.html --self-contained-html"
            }
        }

        stage('Regression Tests') {
            steps {
                sh ". $VENV/bin/activate && pytest tests/regression --disable-warnings --html=regression_report.html --self-contained-html"
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: '*.html', fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        failure {
            echo '❌ Build failed — infotainment validation errors detected!'
        }
        success {
            echo '✅ Build passed — UI & API validation successful!'
        }
    }
}
