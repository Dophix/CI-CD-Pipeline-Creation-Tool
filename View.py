from tkinter import *
from tkinter.ttk import *
from functions import view_input_output
from pubsub import pub


class GUI:
    def __init__(self, master, project):

        self.master = master
        self.master.title("Project Creation")

        self.right_frame = Frame(self.master)
        self.left_frame = Frame(self.master)

        self.left_bottom_frame = Frame(self.left_frame)
        self.left_top_frame = Frame(self.left_frame)
        self.bottom_frame = Frame(self.left_frame)

        self.label_generation_format = Label(self.left_top_frame, text="Generation Format")
        self.combo_generation_format = Combobox(self.left_top_frame, width=25,
                                                values=["JSON and commands only", "Both"])
        self.label_generation_type = Label(self.left_top_frame, text="Generation Type")
        self.combo_generation_type = Combobox(self.left_top_frame, width=25,
                                              values=["API", "SDK", "FRONT"])
        self.label_projectname = Label(self.left_top_frame, text="Project Name")
        self.entry_projectname = Entry(self.left_top_frame, width=28)
        self.label_codecommit = Label(self.left_top_frame, text="CodeCommit Repo")
        self.label_codecommit_reponame = Label(self.left_top_frame, text="")
        self.label_pipeline = Label(self.left_top_frame, text="Pipeline Name")
        self.label_pipeline_namelist = Label(self.left_top_frame, text="")
        self.label_codebuild = Label(self.left_top_frame, text="CodeBuild Builder")
        self.combo_codebuild = Combobox(self.left_top_frame, width=25,
                                        values=view_input_output.fetch_codebuild_projects())
        self.label_clusters = Label(self.left_top_frame, text="Cluster")
        self.combo_clusters = Combobox(self.left_top_frame, width=25,
                                        values=view_input_output.fetch_cluster_list())  # ["Cluster1","Cluster2","Cluster3"]
        self.bucket_name = Label(self.left_top_frame, text="Bucket Name")
        self.entry_bucket_name = Entry(self.left_top_frame, width=28)
        self.recap_name = Label(self.left_top_frame, text="Recap")
        self.recap_text = Text(self.left_bottom_frame, state='disabled', width=34, height=8)
        self.submit_button = Button(self.bottom_frame, text="Submit",
                                    command=self.__submit)
        self.console_name = Label(self.right_frame, text="Console")
        self.console_text = Text(self.right_frame, state='disabled', background="black", foreground="white", width=100,
                                 height=22)
        self.create_button = Button(self.bottom_frame, text="Create",
                                    command=self.__create)

        self.create_widgets()
        self.project = project

    def create_widgets(self):

        self.left_frame.grid(column=0, row=0, padx=10, sticky=N)

        self.right_frame.grid(column=1, row=0, padx=10, sticky=N)

        self.left_top_frame.grid(column=0, row=0, padx=10, sticky=N)

        self.left_bottom_frame.grid(column=0, row=1, padx=10, sticky=N)

        self.bottom_frame.grid(column=0, row=2, padx=10, sticky=N)

        # Label Generation Format
        self.label_generation_format.grid(column=0, row=0, pady=5, sticky=W)

        # Combobox Generation Format
        self.combo_generation_format.current(0)
        self.combo_generation_format.grid(column=1, row=0, pady=5, sticky=N + E)

        # Label Generation Type
        self.label_generation_type.grid(column=0, row=1, pady=5, sticky=W)

        # Combobox Generation Type
        self.combo_generation_type.current(0)
        self.combo_generation_type.grid(column=1, row=1, pady=5, sticky=N + E)

        # ProjectName Label
        self.label_projectname.grid(column=0, row=2, pady=5, sticky=W)

        # Textbox Projectname
        self.entry_projectname.bind("<KeyRelease>", self.__update_codecommit_and_pipeline_name)
        self.entry_projectname.grid(column=1, row=2, pady=5, sticky=E)

        # Label Codecommit Reponame
        self.label_codecommit.grid(column=0, row=3, pady=5, sticky=N + W)

        # Label Codecommit Reponame Example
        self.label_codecommit_reponame.grid(column=1, row=3, padx=10, pady=5, sticky=W + N)

        # Label Pipeline name
        self.label_pipeline.grid(column=0, row=4, pady=5, sticky=N + W)

        # Label Pipeline name Example
        self.label_pipeline_namelist.grid(column=1, row=4, padx=10, pady=5, sticky=W + N)

        # Label Codebuild Builder choice
        self.label_codebuild.grid(column=0, row=5, pady=5, sticky=W)

        # Combobox Codebuild Builder Choice
        self.combo_codebuild.current(0)
        self.combo_codebuild.grid(column=1, row=5, pady=5, sticky=N + E)

        # Label CCluster Choice
        self.label_clusters.grid(column=0, row=6, pady=5, sticky=W)

        # Combobox Cluster Choice
        self.combo_clusters.current(0)
        self.combo_clusters.grid(column=1, row=6, pady=5, sticky=N + E)

        # Bucket Label
        self.bucket_name.grid(column=0, row=7, pady=5, sticky=W)

        # Bucket Projectname
        self.entry_bucket_name.bind("<KeyRelease>", self.__update_codecommit_and_pipeline_name)
        self.entry_bucket_name.grid(column=1, row=7, pady=5, sticky=E)

        # Recap label
        self.recap_name.grid(column=0, row=8, pady=5, sticky=W)

        # Recap text
        self.recap_text.grid(column=0, row=8, pady=5)

        # Submit Button
        self.submit_button.grid(column=0, row=0, pady=5)

        # Console label
        self.console_name.grid(column=0, row=0, pady=5, sticky=W)

        # Console
        self.console_text.grid(column=0, row=1, pady=5)

    def __update_codecommit_and_pipeline_name(self, event=None):
        codecommit_name = ""
        pipeline_name = ""
        codecommit_name = codecommit_name + view_input_output.set_project_name_refactor(
            self.entry_projectname.get())
        pipeline_name = pipeline_name + view_input_output.set_project_name_refactor(
            self.entry_projectname.get())

        self.label_codecommit_reponame["text"] = codecommit_name
        self.label_pipeline_namelist["text"] = pipeline_name

    def __create(self):
        pub.sendMessage("create")

    def __submit(self):
        pub.sendMessage("submit")

    def __update_size_recap(self):
        widget_width = 34
        widget_height = float(self.recap_text.index(END))
        for line in self.recap_text.get("1.0", END).split("\n"):
            if len(line) > widget_width:
                widget_width = len(line) + 1
        self.recap_text.config(width=widget_width, height=widget_height)

    def __update_size_console(self):
        widget_width = 100
        for line in self.console_text.get("1.0", END).split("\n"):
            if len(line) > widget_width:
                widget_width = len(line) + 1
        self.console_text.config(width=widget_width)

    def set_recap(self):
        data = self.project.get_all_info()
        self.recap_text.configure(state='normal')
        self.recap_text.delete("1.0", END)
        for d in data:
            txt = d["name"] + " " + d["data"] + "\n"
            self.recap_text.insert('end', txt)
        self.__update_size_recap()
        self.recap_text.configure(state='disabled')

    def set_console(self, text):
        self.console_text.configure(state='normal')
        self.console_text.insert('end', text + "\n")
        self.__update_size_console()
        self.console_text.configure(state='disabled')

    def activate_creation_button(self):
        # Create Button
        self.create_button.grid(column=1, row=0, pady=5)

    def get_bucket_name(self):
        return self.entry_bucket_name.get()

    def get_project_name(self):
        return self.entry_projectname.get()

    def get_codecommit_name(self):
        return self.label_codecommit_reponame["text"]

    def get_selected_codebuild_builder(self):
        return self.combo_codebuild.get()

    def get_cluster_name(self):
        return self.combo_clusters.get()

    def get_pipeline_names(self):
        return self.label_pipeline_namelist["text"]

    def get_generation_type(self):
        return self.combo_generation_type.get()

    def get_generation_format(self):
        return self.combo_generation_format.get()


