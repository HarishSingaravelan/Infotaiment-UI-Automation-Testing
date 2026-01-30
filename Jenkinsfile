pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root:root'   // allow installs
        }
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
                sleep 5
            }
        }

        stage('Run UI Automation Tests') {
            steps {
                sh 'pytest tests/ --html=report.html --self-contained-html'
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }
    }

    post {
        failure {
            echo '❌ Build failed — infotainment validation errors detected!'
        }
        success {
            echo '✅ Build passed — UI validation successful!'
        }
    }
}
