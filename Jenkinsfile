pipeline {
    agent any

    stages {
        stage('Setup Python Environment') {
            steps {
                dir('MiniProject1') {
                    sh '''
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir('MiniProject1') {
                    sh '''
                        source venv/bin/activate
                        pytest -v -s Tests/ 
                    '''
                }
            }
        }  
    }
}
