curl -X POST -H 'Content-Type: application/json' \
    --data-binary '[{"project": "project1", "code": "import torch\nprint(torch.__version__)"}, {"project": "project2", "code": "import jax\nprint(jax.__version__)"}]' \
    https://justinchiu--repo-rpc-evaluate-dev.modal.run 

