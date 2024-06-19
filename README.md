# Alexander Kalinov's Scrapy Task

### How to run using Docker:
```
git clone https://github.com/necrocry/task_alexander.git
cd task_alexander/task
docker build -t task:image .
docker run -d -it --name task_container -v $(pwd):/usr/src/app task:image
```
After running the commands above, task.json file will (in a few seconds) appear inside the current folder.
Execute `cat task.json` to open the generated file.
