pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-u root:root'  // run as root inside container
        }
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create virtual environment and install dependencies
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
                sh '. venv/bin/activate && pip install -r requirements.txt'
                sh '. venv/bin/activate && playwright install --with-deps'
            }
        }

        stage('Start Backend Server') {
            steps {
                // Start uvicorn in background
                sh '''
                    . venv/bin/activate
                    nohup uvicorn main:app --host 0.0.0.0 --port 8000 > server.log 2>&1 &
                '''
                // Wait for server to be ready
                sh 'sleep 5'
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
            echo '❌ Build failed — infotainment validation errors detected!'
        }
        success {
            echo '✅ Build passed — UI validation successful!'
        }
    }
}
