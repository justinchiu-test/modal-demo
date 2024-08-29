# modal-demo

first, [setup modal](https://modal.com/docs/guide)

then, you can run a small speed benchmark to compare parallel vs serial modal execution:
```
uv run modal run src/modal_demo/app.py
```

finally, you can run a webserver with
```
uv run modal serve src/modal_demo/app.py
```
and send an example request via
```
uv run bash send_request.sh
```
note: you will have to change the URL in `send_request.sh` to whatever endpoint modal generates for you
