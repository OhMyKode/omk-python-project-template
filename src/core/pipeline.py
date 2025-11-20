# -*- coding: utf-8 -*-

from loguru import logger
from omegaconf import DictConfig


def run_pipeline(cfg: DictConfig) -> None:
    """Run the main processing pipeline based on the provided configuration.

    Parameters
    ----------
    cfg : DictConfig
        Configuration object containing all settings for the pipeline.
    """
    # example how to access config values
    project_name = cfg.project.name
    logger.info("Project Name: {}", project_name)
    logger.info("Running pipeline with config: {}", cfg)
