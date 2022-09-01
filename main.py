import warnings
from pathlib import Path

import hydra
from hydra.core.config_store import ConfigStore

from config import TestConfig

warnings.simplefilter("ignore", UserWarning)

cs = ConfigStore.instance()
cs.store(name="test_config", node=TestConfig)


@hydra.main(config_path="conf", config_name="config")
def main(conf: TestConfig):
    print(conf)
    print(Path(conf.db.pwd))
    return


if __name__ == "__main__":
    main()
