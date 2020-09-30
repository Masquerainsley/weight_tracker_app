resource "aws_elastic_beanstalk_application" "weight_tracker_app" {
  name        = "weight_tracker_app_1"
  description = "an app to track your weight"
}

resource "aws_elastic_beanstalk_environment" "weight_tracker_env" {
  name                = "weight-tracker-env-1"
  application         = aws_elastic_beanstalk_application.weight_tracker_app.name
  solution_stack_name = "64bit Amazon Linux 2 v3.1.1 running Python 3.7"
  setting {
      namespace = "aws:autoscaling:launchconfiguration"
      name = "IamInstanceProfile"
      value = "aws-elasticbeanstalk-ec2-role"
  }
}

resource "aws_s3_bucket" "b" {
  bucket = "weight_tracker_app_bucket"
  acl    = "private"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}

