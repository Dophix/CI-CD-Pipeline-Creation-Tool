from subprocess import Popen, PIPE, STDOUT
import json
from functions import log_name_generator

class AWS_services:
    def __init__(self, view):
        self.view = view
        self.log_file_name = "output/" + log_name_generator.create_logfile_name()

    def create_pipeline(self, json_file_path: str):
        proc = Popen(
            ["aws", "codepipeline", "create-pipeline", "--cli-input-json", "file://{}".format(json_file_path)],
            stdout=PIPE, stderr=STDOUT, shell=True, text=True
        )

        log_file = open(self.log_file_name, "a")
        log_file.write("\n  ==========================  Pipeline  ==========================  \n")
        self.view.set_console("\nPipeline :\n")
        for line in proc.stdout:
            if line:
                self.view.set_console(line.strip())
                log_file.write(line.strip()+"\n")

        proc.terminate()
        log_file.close()

    def create_codecommit_repo(self, repository_name: str):
        proc = Popen(
            ["aws", "codecommit", "create-repository", "--repository-name", repository_name],
            stdout=PIPE, stderr=STDOUT, shell=True, text=True
        )

        log_file = open(self.log_file_name, "a")
        log_file.write("\n  =========================  CodeCommit  =========================  \n")
        self.view.set_console("\nCodeCommit :\n")
        for line in proc.stdout:
            if line:
                self.view.set_console(line.strip())
                log_file.write(line.strip()+"\n")

        proc.terminate()
        log_file.close()

        self.add_basic_files_to_codecommit(repository_name)

    def add_basic_files_to_codecommit(self, repository_name: str):
        proc = Popen(
            ["aws", "codecommit", "create-commit", "--repository-name", repository_name, "--branch-name", "master",
             "--put-files",
             "filePath=README.md,fileContent='Welcome to our team repository.'",
             "filePath=.gitignore,fileContent=''"],
            stdout=PIPE, stderr=STDOUT, shell=True, text=True
        )

        log_file = open(self.log_file_name, "a")
        log_file.write("\n  ===============  CodeCommit base file creation  ===============  \n")
        self.view.set_console("CodeCommit base file creation :\n")
        for line in proc.stdout:
            if line:
                self.view.set_console(line.strip())
                log_file.write(line.strip()+"\n")

        proc.terminate()
        log_file.close()

    def create_S3_bucket(self, name):
        proc = Popen(
            ["aws", "s3api", "create-bucket", "--bucket", name, "--region", "eu-central-1",
             "--create-bucket-configuration", "LocationConstraint=eu-central-1"],
            stdout=PIPE, stderr=STDOUT, shell=True, text=True
        )

        log_file = open(self.log_file_name, "a")
        log_file.write("\n  ===============  Bucket S3  ===============  \n")
        self.view.set_console("\nBucket S3 :\n")
        for line in proc.stdout:
            if line:
                self.view.set_console(line.strip())
                log_file.write(line.strip()+"\n")

        proc.terminate()
        log_file.close()
