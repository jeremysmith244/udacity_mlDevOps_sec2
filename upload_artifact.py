import argparse
import wandb

def upload(args):

    with wandb.init(project=args.project_name) as run:
        
        artifact = wandb.Artifact(
            name=args.artifact_name, 
            type=args.artifact_type, 
            description=args.artifact_description)

        artifact.add_file(args.artifact_name)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Weights and biases upload script"
    )
    parser.add_argument(
        "--project_name", type=str, help="Project name for upload to W&B", required=True
    )
    parser.add_argument(
        "--artifact_name", type=str, help="Artifact name for upload to W&B", required=True
    )
    parser.add_argument(
        "--artifact_type", type=str, help="Artifact type for upload to W&B", required=True
    )
    parser.add_argument(
        "--artifact_description", type=str, help="Artifact description for upload to W&B", required=True
    )

    args = parser.parse_args()

    upload(args)