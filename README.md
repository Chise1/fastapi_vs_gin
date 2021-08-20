python启动服务：
```
docker-compose up
```
golang启动服务：

```golang build getOne.go 
./getOne.exe
```

python启动测试：./wrk -t80 -c200 -d30s --latency http://127.0.0.1:8000/getOne
golang启动测试：./wrk -t80 -c200 -d30s --latency http://127.0.0.1:8080/getOne
wrk安装方式请自行参考wrk的github项目说明

在我自己的笔记本上的结果： python:

```shell
root@cs:~/wrk# ./wrk -t80 -c200 -d30s --latency http://127.0.0.1:8000/getOne
Running 30s test @ http://127.0.0.1:8000/getOne
  80 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    65.75ms   30.52ms 324.83ms   73.11%
    Req/Sec    30.68     12.01    90.00     80.93%
  Latency Distribution
     50%   60.80ms
     75%   82.29ms
     90%  103.94ms
     99%  160.36ms
  73394 requests in 30.10s, 8.99MB read
Requests/sec:   2437.98
Transfer/sec:    305.83KB
```

golang:

```shell
root@cs:~/wrk# ./wrk -t80 -c200 -d30s --latency http://127.0.0.1:8080/getOne
Running 30s test @ http://127.0.0.1:8080/getOne
  80 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    46.67ms   48.89ms 550.70ms   86.42%
    Req/Sec    50.43     29.29   250.00     64.74%
  Latency Distribution
     50%   36.64ms
     75%   69.47ms
     90%  108.03ms
     99%  211.33ms
  119883 requests in 30.10s, 13.72MB read
Requests/sec:   3982.66
Transfer/sec:    466.72KB
```

看起来两者差距并不大。