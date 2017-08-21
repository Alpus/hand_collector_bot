##### How to start:
Add line `API_TOKEN = '<TELEGRAM_TOKEN>'` in `hadjob_bot/app/settings/private.py`

and

```
# In root repo dir:

docker-compose build
docker-compose up -d # do not use -d if you want to stay in interactive session
```

##### Note:
If you need to save images in some other directory (not `./images`), you need to replace `./images:/images` in `docker-compose.yml` file to `<your_images_dir>:/images`.
