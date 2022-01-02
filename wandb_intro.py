import wandb

run = wandb.init(
    project="my_project",
    job_type="data_cleaning",
    group="experiment_1"
)