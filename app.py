import asyncio
import modal
import subprocess
import time

app = modal.App("repo-rpc")

project1_image = (modal.Image
    #.from_dockerfile("Dockerfile")
    .debian_slim(python_version="3.11")
    .pip_install("uv")
    .copy_local_dir("projects/project1", "/app")
    .workdir("/app")
    .run_commands("uv sync")
)
project2_image = (modal.Image
    #.from_dockerfile("Dockerfile")
    .debian_slim(python_version="3.11")
    .pip_install("uv")
    .copy_local_dir("projects/project2", "/app")
    .workdir("/app")
    .run_commands("uv sync")
)

def make_file(path, code):
    with open(path, "w") as f:
        f.write(code)

@app.function(image=project1_image)
def run_project1(code):
    path = "/app/src/project1/run.py"
    make_file(path, code)
    output = subprocess.check_output(f"uv run python {path}".split())
    return output

@app.function(image=project2_image)
def run_project2(code):
    path = "/app/src/project2/run.py"
    make_file(path, code)
    output = subprocess.check_output(f"uv run python {path}".split())
    return output

async def async_run(code1, code2):
    outputs = await asyncio.gather(
        run_project1.remote.aio(code1),
        run_project2.remote.aio(code2),
    )
    print(outputs)

@app.local_entrypoint()
def main():
    code1 = "import torch\nprint(torch.__version__)"
    code2 = "import jax\nprint(jax.__version__)"

    start = time.time()
    asyncio.run(async_run(code1, code2))
    end = time.time()
    print(end - start, "secs for parallel")

    start = time.time()
    output1 = run_project1.remote(code1)
    print(output1)
    output2 = run_project2.remote(code2)
    print(output2)
    end = time.time()
    print(end - start, "secs for serial")

    start = time.time()
    asyncio.run(async_run(code1, code2))
    end = time.time()
    print(end - start, "secs for parallel")

    start = time.time()
    output1 = run_project1.remote(code1)
    print(output1)
    output2 = run_project2.remote(code2)
    print(output2)
    end = time.time()
    print(end - start, "secs for serial")

