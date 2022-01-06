pipeline{
    agent any
    stages{
        stage('Setup EC2'){
            steps{
                sh label: '', script: '''sudo yum update -y
                                            sudo amazon-linux-extras install docker
                                            sudo yum install docker
                                            sudo service docker start
                                            sudo usermod -a -G docker ec2-user'''

            }
        }

        stage('Launch docker container'){
            steps {
                sh 'docker build .'

            }
        }

    }
}