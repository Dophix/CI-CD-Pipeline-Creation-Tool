from subprocess import Popen, PIPE, STDOUT
import json


def set_project_name_refactor(name: str):
    codecommit_name = name.lower()

    return codecommit_name


def fetch_codebuild_projects():
    proc = Popen(
        ["aws", "codebuild", "list-projects"],
        stdout=PIPE, stderr=STDOUT, shell=True, text=True
    )
    output = json.loads(proc.stdout.read())

    proc.terminate()

    return output["projects"]


def fetch_cluster_list():
    cluster_name = []

    proc = Popen(
        ["aws", "ecs", "list-clusters"],
        stdout=PIPE, stderr=STDOUT, shell=True, text=True
    )
    output = json.loads(proc.stdout.read())
    for cluster_arn in output["clusterArns"]:
        a = cluster_arn.split(":")
        cluster_name.append(a[5])
    proc.terminate()

    return cluster_name
