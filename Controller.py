import os
from tkinter import *
from tkinter.ttk import *
from Model_Project import Project
from functions import json_services, AWS_services, commands_generator
from View import GUI
from pubsub import pub
from json_generator import JSON_model


class Controller:
    def __init__(self, root):
        self.root = root
        self.project = Project()
        self.gui = GUI(self.root, self.project)
        self.aws_services = AWS_services.AWS_services(self.gui)
        self.json_model = JSON_model()
        self.json_template = None
        self.dirName = 'output'

        pub.subscribe(self.__create_btn_pressed, "create")
        pub.subscribe(self.__submit_btn_pressed, "submit")

    def __create_btn_pressed(self):

        try:
            # Create target Directory
            os.mkdir(self.dirName)
            self.gui.set_console("Output directory " + self.dirName + " Created ")
        except FileExistsError:
            self.gui.set_console("Output directory " + self.dirName + " already exist ")

        if self.project.get_generation_format() == "JSON and commands only":
            json_services.create_json_template(self.json_model.json_template, self.project.get_project_name())
            self.__commands_file_generation()

        if self.project.get_generation_format() == "Both":
            self.__creation_process()
            self.__commands_file_generation()
            
    def __creation_process(self):
        if self.project.get_generation_type() == "SDK":
            self.__sdk_creation()

        if self.project.get_generation_type() == "API":
            self.__api_creation()

        if self.project.get_generation_type() == "FRONT":
            self.__front_creation()

    def __submit_btn_pressed(self):
        self.__set_model_data()
        self.json_template = "output/" + self.project.get_project_name() + "-template.json"
        self.gui.set_recap()
        self.__set_json_data()


    def __set_model_data(self):
        self.project.set_project_name(self.gui.get_project_name())
        self.project.set_codebuild_name(self.gui.get_selected_codebuild_builder())
        self.project.set_codecommit_name(self.gui.get_codecommit_name())
        self.project.set_pipeline_name(self.gui.get_pipeline_names())
        self.project.set_bucket(self.gui.get_bucket_name())
        self.project.set_generation_format(self.gui.get_generation_format())
        self.project.set_generation_type(self.gui.get_generation_type())

    def __set_json_data(self):
        self.json_model.set_name(self.project.get_project_name())
        self.json_model.set_RepositoryName(self.project.get_codecommit_name())
        self.json_model.set_ProjectName(self.project.get_codebuild_name())
        self.json_model.set_ClusterName("")
        self.json_model.set_FileName("")
        self.json_model.set_ServiceName("")
        self.json_model.set_BucketName(self.project.get_bucket_name())
        self.json_model.json_declaration(self.project.get_generation_type())

    def __sdk_creation(self):
        self.aws_services.create_codecommit_repo(self.project.get_codecommit_name())
        json_services.create_json_template(self.json_model.json_template, self.project.get_project_name())
        self.aws_services.create_pipeline(self.json_template)

    def __front_creation(self):
        self.aws_services.create_codecommit_repo(self.project.get_codecommit_name())
        json_services.create_json_template(self.json_model.json_template, self.project.get_project_name())
        self.aws_services.create_S3_bucket(self.project.get_bucket_name())
        self.aws_services.create_pipeline(self.json_template)

    def __api_creation(self):
        pass

    def __commands_file_generation(self):
        filename = "output/"+commands_generator.create_command_file(self.project.get_project_name())
        if self.project.get_generation_type() == "SDK":
            commands_generator.write_codecommit_command(filename, self.project.get_codecommit_name())
            commands_generator.add_basic_files_to_codecommit_command(filename, self.project.get_codecommit_name())
            commands_generator.write_codepipeline_command(filename, self.json_template)
            self.gui.set_console("SDK command and JSON template created")

        if self.project.get_generation_type() == "API":
            pass

        if self.project.get_generation_type() == "FRONT":
            commands_generator.write_codecommit_command(filename, self.project.get_codecommit_name())
            commands_generator.add_basic_files_to_codecommit_command(filename, self.project.get_codecommit_name())
            commands_generator.write_bucketS3_command(filename, self.project.get_bucket_name())
            commands_generator.write_codepipeline_command(filename, self.json_template)
            self.gui.set_console("FRONT command and JSON template created")



if __name__ == '__main__':
    root = Tk()
    app = Controller(root)
    root.mainloop()