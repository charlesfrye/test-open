import wandb

with wandb.init(project="test-open"):
    wandb.log({"foo": 1})
