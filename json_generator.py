import json


class JSON_model:
    def __init__(self):
        self.name = None
        self.RepositoryName = None
        self.ProjectName = None
        self.ClusterName = None
        self.FileName = None
        self.ServiceName = None
        self.BucketName = None
        self.json_template = None

    def set_name(self, name):
        self.name = name

    def set_RepositoryName(self, name):
        self.RepositoryName = name

    def set_ProjectName(self, name):
        self.ProjectName = name

    def set_ClusterName(self, name):
        self.ClusterName = name

    def set_FileName(self, name):
        self.FileName = name

    def set_ServiceName(self, name):
        self.ServiceName = name

    def set_BucketName(self, name):
        self.BucketName = name

    def json_declaration(self, generation_type: str):
        # codepipeline-eu-central-1-904651582082
        # ["pipeline"]["artifactStore"]["location"] = "codepipeline-eu-central-1-904651582082"
        # ["pipeline"]["roleArn"] = "arn:aws:iam::945254933472:role/service-role/AWSCodePipelineServiceRole-eu-central-1-WaitDataExtractPipeline"


        if generation_type == "API":
            with open("json_templates/api_template.json") as jsonfile:
                self.json_template = json.load(jsonfile)
                jsonfile.close()

            self.json_template["pipeline"]["name"] = \
                self.name
            self.json_template["pipeline"]["stages"][0]["actions"][0]["configuration"]["RepositoryName"] = \
                self.RepositoryName
            self.json_template["pipeline"]["stages"][1]["actions"][0]["configuration"]["ProjectName"] = \
                self.ProjectName
            self.json_template["pipeline"]["stages"][2]["actions"][0]["configuration"]["ClusterName"] = \
                self.ClusterName
            self.json_template["pipeline"]["stages"][2]["actions"][0]["configuration"]["FileName"] = \
                self.FileName
            self.json_template["pipeline"]["stages"][2]["actions"][0]["configuration"]["ServiceName"] = \
                self.ServiceName
            # todo: remove
            self.json_template["pipeline"]["artifactStore"]["location"] = "codepipeline-eu-central-1-904651582082"
            self.json_template["pipeline"][
                "roleArn"] = "arn:aws:iam::945254933472:role/service-role/AWSCodePipelineServiceRole-eu-central-1-WaitDataExtractPipeline"

        elif generation_type == "SDK":
            with open("json_templates/sdk_template.json") as jsonfile:
                self.json_template = json.load(jsonfile)
                jsonfile.close()

            self.json_template["pipeline"]["name"] = \
                self.name
            self.json_template["pipeline"]["stages"][0]["actions"][0]["configuration"]["RepositoryName"] = \
                self.RepositoryName
            self.json_template["pipeline"]["stages"][1]["actions"][0]["configuration"]["ProjectName"] = \
                self.ProjectName
            # todo: remove
            self.json_template["pipeline"]["artifactStore"]["location"] = "codepipeline-eu-central-1-904651582082"
            self.json_template["pipeline"]["roleArn"] = "arn:aws:iam::945254933472:role/service-role/AWSCodePipelineServiceRole-eu-central-1-WaitDataExtractPipeline"

        elif generation_type == "FRONT":
            with open("json_templates/front_template.json") as jsonfile:
                self.json_template = json.load(jsonfile)
                jsonfile.close()

            self.json_template["pipeline"]["name"] = \
                self.name
            self.json_template["pipeline"]["stages"][0]["actions"][0]["configuration"]["RepositoryName"] = \
                self.RepositoryName
            self.json_template["pipeline"]["stages"][1]["actions"][0]["configuration"]["ProjectName"] = \
                self.ProjectName
            self.json_template["pipeline"]["stages"][2]["actions"][0]["configuration"]["BucketName"] = \
                self.BucketName
            # todo: remove
            self.json_template["pipeline"]["artifactStore"]["location"] = "codepipeline-eu-central-1-904651582082"
            self.json_template["pipeline"][
                "roleArn"] = "arn:aws:iam::945254933472:role/service-role/AWSCodePipelineServiceRole-eu-central-1-WaitDataExtractPipeline"
        else:
            pass

