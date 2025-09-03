pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.9'
        VENV_NAME = 'jenkins-venv'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }
        
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                sh '''
                    python3 -m venv ${VENV_NAME}
                    . ${VENV_NAME}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Lint Code') {
            steps {
                echo 'Running code quality checks...'
                sh '''
                    . ${VENV_NAME}/bin/activate
                    pip install flake8
                    flake8 app.py test_app.py --max-line-length=100 --ignore=E501
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    . ${VENV_NAME}/bin/activate
                    pytest test_app.py -v --tb=short
                '''
            }
        }
        
        stage('Test Coverage') {
            steps {
                echo 'Generating test coverage report...'
                sh '''
                    . ${VENV_NAME}/bin/activate
                    pytest --cov=app --cov-report=xml --cov-report=html test_app.py
                '''
            }
            post {
                always {
                    // Archive coverage reports as artifacts
                    archiveArtifacts artifacts: 'coverage.xml, htmlcov/**', allowEmptyArchive: true
                    // If you have the Cobertura plugin installed, uncomment the line below:
                    // publishCoverage adapters: [coberturaAdapter('coverage.xml')], sourceFileResolver: sourceFiles('STORE_LAST_BUILD')
                }
            }
        }
        
        stage('Run Application') {
            steps {
                echo 'Testing application execution...'
                sh '''
                    . ${VENV_NAME}/bin/activate
                    python app.py
                '''
            }
        }
        
        stage('Archive Artifacts') {
            steps {
                echo 'Archiving build artifacts...'
                archiveArtifacts artifacts: '*.py, requirements.txt, htmlcov/**', fingerprint: true
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up workspace...'
            sh '''
                if [ -d "${VENV_NAME}" ]; then
                    rm -rf ${VENV_NAME}
                fi
            '''
        }
        
        success {
            echo 'Pipeline executed successfully! ✅'
        }
        
        failure {
            echo 'Pipeline failed! ❌'
            emailext (
                subject: "Jenkins Build Failed: ${env.JOB_NAME} - ${env.BUILD_NUMBER}",
                body: "Build failed. Check console output at ${env.BUILD_URL}",
                to: "${env.CHANGE_AUTHOR_EMAIL}"
            )
        }
        
        unstable {
            echo 'Pipeline is unstable! ⚠️'
        }
    }
} 