def gv

pipeline {
    agent any

    stages {
        stage("init") {
            steps {
                echo 'checkout app code...'
            }
        }
        stage("build") {
            steps {
                echo 'build app'
            }
        }
        stage("test") {              
            steps {
                echo 'run code test suite...'
            }
        }
        stage("deploy") {
            steps {
                echo 'deploy app to staging...'
            }
        }
        
        
    }
    post {
        always {
            //
        }
        success {

        }
        failure {
            
        }
    }   
}