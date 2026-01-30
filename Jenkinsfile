pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-u root:root'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python --version'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'

                sh 'playwright install --with-deps'
            }
        }

        stage('Run API Tests') {
            steps {
                sh 'pytest -v --maxfail=1 --disable-warnings'
            }
        }
    }

    post {
        success {
            echo '✅ All infotainment system tests passed!'
        }
        failure {
            echo '❌ Build failed — infotainment validation errors detected!'
        }
    }
}
