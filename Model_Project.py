import json
from subprocess import Popen, PIPE, STDOUT
import os

class Project:
    def __init__(self):
        self.project_name = None
        self.codecommit_repo_name = None
        self.codebuild_project_name =None
        self.pipeline_name = None
        self.S3_repo = None
        self.generation_type = None
        self.generation_format = None

    def set_project_name(self, name):
        self.project_name = name

    def set_codecommit_name(self, name):
        self.codecommit_repo_name = name

    def set_codebuild_name(self, name):
        self.codebuild_project_name = name

    def set_pipeline_name(self, name):
        self.pipeline_name = name

    def set_bucket(self, name):
        self.S3_repo = "capcod-"+name

    def set_generation_format(self, name):
        self.generation_format = name

    def set_generation_type(self, name):
        self.generation_type = name

    def get_project_name(self):
        return self.project_name

    def get_codecommit_name(self):
        return self.codecommit_repo_name

    def get_codebuild_name(self):
        return self.codebuild_project_name

    def get_pipeline_name(self):
        return self.pipeline_name

    def get_bucket_name(self):
        return self.S3_repo

    def get_generation_format(self):
        return self.generation_format

    def get_generation_type(self):
        return self.generation_type

    def get_all_info(self):
        data = [
            {
                "name": "Codecommit :",
                "data": self.codecommit_repo_name
            },
            {
                "name": "Codebuild :",
                "data": self.codebuild_project_name
            },
            {
                "name": "Pipeline :",
                "data": self.pipeline_name
            },
            {
                "name": "Generation Type :",
                "data": self.generation_type
            },
            {
                "name": "Generation Format :",
                "data": self.generation_format
            },
            {
                "name": "S3 :",
                "data": self.S3_repo
            }
        ]
        return(data)
