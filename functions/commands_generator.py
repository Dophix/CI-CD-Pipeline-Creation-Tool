import time


def write_codecommit_command(command_path: str, codecommit_name: str):
    log_file = open(command_path, "a")
    log_file.write("\n      Create Codecommit Repository :\n\n")
    log_file.write("aws codecommit create-repository --repository-name " + codecommit_name + "\n")
    log_file.close()


def add_basic_files_to_codecommit_command(command_path: str, codecommit_name: str):
    log_file = open(command_path, "a")
    log_file.write("\n      Fill Codecommit with .gitignore and README.md files :\n\n")
    log_file.write("aws codecommit create-commit --repository-name " + codecommit_name +
                   "--branch-name master --put-files "
                   "filePath=README.md,fileContent='Welcome to our team repository.' "
                   "filePath=.gitignore,fileContent=''" + "\n")
    log_file.close()


def write_bucketS3_command(command_path: str, bucket_name: str):
    log_file = open(command_path, "a")
    log_file.write("\n      Create S3 Bucket :\n\n")
    log_file.write("aws s3api create-bucket --bucket " + bucket_name +
                   " --region eu-central-1 --create-bucket-configuration LocationConstraint=eu-central-1" + "\n")
    log_file.close()


def write_codepipeline_command(command_path: str, json_path: str):
    log_file = open(command_path, "a")
    log_file.write("\n      Create your project pipeline :\n\n")
    log_file.write("aws codepipeline create-pipeline --cli-input-json file://" + json_path + "\n")
    log_file.close()


def write_ECS_command(command_path: str, cluster_name: str, service_name: str):
    log_file = open(command_path, "a")
    log_file.write("\n      Create ECS cluster and service :\n\n")
    log_file.write("aws ecs create-service --cluster " + cluster_name + "--service-name " + service_name + "\n")
    log_file.close()
