# modal-demo

first, [setup modal](https://modal.com/docs/guide)

then, you can run a small speed benchmark to compare parallel vs serial modal execution:
```
modal run src/modal_demo/app.py
```

finally, you can run a webserver with
```
modal serve src/modal_demo/app.py
```
and send an example request via
```
bash send_request.sh
```
