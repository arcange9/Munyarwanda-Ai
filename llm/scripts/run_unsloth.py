"""Minimal Unsloth QLoRA launcher.

Run after dataset preparation and validation. This script targets a local or
free-notebook GPU environment and does not start any paid cloud job.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "configs" / "unsloth.yaml"
DATA = ROOT / "data" / "processed"


def main():
    try:
        from unsloth import FastLanguageModel
        from datasets import load_dataset
        from trl import SFTTrainer, SFTConfig
    except ImportError as exc:
        raise SystemExit(
            "Install Unsloth, datasets and TRL in a GPU environment before running this pilot."
        ) from exc

    import yaml

    cfg = yaml.safe_load(CONFIG.read_text())
    train_path = DATA / "train.jsonl"
    valid_path = DATA / "validation.jsonl"
    if not train_path.exists() or not valid_path.exists():
        raise SystemExit(
            "Missing prepared train/validation JSONL. Run the dataset preparation pipeline first."
        )

    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=cfg["base_model"],
        max_seq_length=cfg["max_seq_length"],
        load_in_4bit=cfg["load_in_4bit"],
    )
    model = FastLanguageModel.get_peft_model(
        model,
        r=cfg["lora_r"],
        lora_alpha=cfg["lora_alpha"],
        lora_dropout=cfg["lora_dropout"],
        bias="none",
        use_gradient_checkpointing="unsloth",
    )

    ds = load_dataset(
        "json",
        data_files={"train": str(train_path), "validation": str(valid_path)},
    )
    trainer = SFTTrainer(
        model=model,
        processing_class=tokenizer,
        train_dataset=ds["train"],
        eval_dataset=ds["validation"],
        args=SFTConfig(
            output_dir=cfg["output_dir"],
            per_device_train_batch_size=cfg["per_device_train_batch_size"],
            gradient_accumulation_steps=cfg["gradient_accumulation_steps"],
            learning_rate=cfg["learning_rate"],
            num_train_epochs=cfg["num_train_epochs"],
            seed=cfg["seed"],
            packing=cfg["packing"],
            max_length=cfg["max_seq_length"],
        ),
    )
    trainer.train()
    trainer.save_model(cfg["output_dir"])
    tokenizer.save_pretrained(cfg["output_dir"])
    print(json.dumps({"status": "completed", "output": cfg["output_dir"]}, indent=2))


if __name__ == "__main__":
    main()
