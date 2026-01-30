pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 --version'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -v'
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
