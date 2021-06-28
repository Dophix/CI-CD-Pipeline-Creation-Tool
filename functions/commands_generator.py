import time


def create_command_file(project_name: str):
    secondsSinceEpoch = time.time()
    timeObj = time.localtime(secondsSinceEpoch)
    name = (project_name + '_commands_%d-%d-%d_%d_%d_%d.txt' % (timeObj.tm_mday, timeObj.tm_mon, timeObj.tm_year,
                                                                timeObj.tm_hour, timeObj.tm_min, timeObj.tm_sec))

    return name


def write_codecommit_command(command_path: str, codecommit_name: str):
    log_file = open(command_path, "a")
    log_file.write("aws codecommit create-repository --repository-name " + codecommit_name + "\n")
    log_file.close()

def add_basic_files_to_codecommit_command(command_path: str, codecommit_name: str):
    log_file = open(command_path, "a")
    log_file.write("aws codecommit create-commit --repository-name " + codecommit_name +
                   "--branch-name master --put-files "
                   "filePath=README.md,fileContent='Welcome to our team repository.' "
                   "filePath=.gitignore,fileContent=''" + "\n")
    log_file.close()

def write_bucketS3_command(command_path: str, bucket_name: str):
    log_file = open(command_path, "a")
    log_file.write("aws s3api create-bucket --bucket " + bucket_name +
                   " --region eu-central-1 --create-bucket-configuration LocationConstraint=eu-central-1" + "\n")
    log_file.close()


def write_codepipeline_command(command_path: str, json_path: str):
    log_file = open(command_path, "a")
    log_file.write("aws codepipeline create-pipeline --cli-input-json file://" + json_path + "\n")
    log_file.close()