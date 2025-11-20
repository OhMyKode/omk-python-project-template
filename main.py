# -*- coding: utf-8 -*-

import hydra
from omegaconf import DictConfig

from src.core.pipeline import run_pipeline


@hydra.main(config_path="conf", config_name="config", version_base="1.3")
def main(cfg: DictConfig) -> None:
    run_pipeline(cfg)


if __name__ == "__main__":
    main()
