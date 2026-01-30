pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
                sh '. venv/bin/activate && playwright install'
            }
        }

        stage('Start Backend Server') {
            steps {
                sh '. venv/bin/activate && nohup uvicorn main:app --host 127.0.0.1 --port 8000 &'
                sleep 5
            }
        }

        stage('Run UI Automation Tests') {
            steps {
                sh '. venv/bin/activate && pytest tests/ --html=report.html --self-contained-html'
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        failure {
            echo 'Build failed — infotainment validation errors detected!'
        }
        success {
            echo 'Build passed — UI validation successful!'
        }
    }
}
