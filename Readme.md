# Week 08

## Homework

1. 使用 redis benchmark 工具, 测试 10 20 50 100 200 1k 5k 字节 value 大小，redis get set 性能。
2. 写入一定量的 kv 数据, 根据数据大小 1w-50w 自己评估, 结合写入前后的 info memory 信息 , 分析上述不同 value 大小下，平均每个 key 的占用内存空间。

## 思路

### 第一题

#### value=10

```bash
redis-benchmark -h 127.0.0.1 -p 55000 -t set,get -d 10 -n 100000 -c 100

====== SET ======
  10000 requests completed in 0.71 seconds
  50 parallel clients
  10 bytes payload
  keep alive: 1

0.14% <= 1 milliseconds
14.16% <= 2 milliseconds
48.99% <= 3 milliseconds
73.85% <= 4 milliseconds
87.30% <= 5 milliseconds
94.18% <= 6 milliseconds
97.55% <= 7 milliseconds
99.07% <= 8 milliseconds
99.64% <= 9 milliseconds
99.88% <= 10 milliseconds
99.92% <= 11 milliseconds
99.96% <= 14 milliseconds
99.99% <= 15 milliseconds
100.00% <= 15 milliseconds
14144.27 requests per second

====== GET ======
  10000 requests completed in 0.69 seconds
  50 parallel clients
  10 bytes payload
  keep alive: 1

0.33% <= 1 milliseconds
16.01% <= 2 milliseconds
52.41% <= 3 milliseconds
75.94% <= 4 milliseconds
88.47% <= 5 milliseconds
94.88% <= 6 milliseconds
98.32% <= 7 milliseconds
99.11% <= 8 milliseconds
99.61% <= 9 milliseconds
99.77% <= 10 milliseconds
99.92% <= 11 milliseconds
99.95% <= 12 milliseconds
99.97% <= 13 milliseconds
99.99% <= 14 milliseconds
100.00% <= 19 milliseconds
14471.78 requests per second
```

#### value=20

```bash
redis-benchmark -h 127.0.0.1 -p 55000 -t set,get -d 20 -n 10000 -c 50

====== SET ======
  10000 requests completed in 0.62 seconds
  50 parallel clients
  20 bytes payload
  keep alive: 1

0.14% <= 1 milliseconds
18.03% <= 2 milliseconds
60.86% <= 3 milliseconds
87.62% <= 4 milliseconds
97.29% <= 5 milliseconds
99.01% <= 6 milliseconds
99.46% <= 7 milliseconds
99.67% <= 8 milliseconds
99.91% <= 9 milliseconds
100.00% <= 9 milliseconds
16260.16 requests per second

====== GET ======
  10000 requests completed in 0.65 seconds
  50 parallel clients
  20 bytes payload
  keep alive: 1

0.24% <= 1 milliseconds
17.91% <= 2 milliseconds
56.84% <= 3 milliseconds
82.36% <= 4 milliseconds
93.94% <= 5 milliseconds
98.22% <= 6 milliseconds
99.34% <= 7 milliseconds
99.66% <= 8 milliseconds
99.92% <= 9 milliseconds
99.99% <= 11 milliseconds
100.00% <= 12 milliseconds
15337.42 requests per second
```

#### value=50

```bash
redis-benchmark -h 127.0.0.1 -p 55000 -t set,get -d 50 -n 10000 -c 50

====== SET ======
  10000 requests completed in 0.73 seconds
  50 parallel clients
  50 bytes payload
  keep alive: 1

0.14% <= 1 milliseconds
13.17% <= 2 milliseconds
49.26% <= 3 milliseconds
76.02% <= 4 milliseconds
89.87% <= 5 milliseconds
95.45% <= 6 milliseconds
97.68% <= 7 milliseconds
98.79% <= 8 milliseconds
99.04% <= 9 milliseconds
99.20% <= 10 milliseconds
99.50% <= 12 milliseconds
99.51% <= 31 milliseconds
99.64% <= 33 milliseconds
99.75% <= 34 milliseconds
99.80% <= 36 milliseconds
99.83% <= 37 milliseconds
99.84% <= 38 milliseconds
99.91% <= 39 milliseconds
99.97% <= 40 milliseconds
99.98% <= 41 milliseconds
100.00% <= 41 milliseconds
13736.26 requests per second

====== GET ======
  10000 requests completed in 0.64 seconds
  50 parallel clients
  50 bytes payload
  keep alive: 1

0.15% <= 1 milliseconds
16.12% <= 2 milliseconds
59.93% <= 3 milliseconds
84.40% <= 4 milliseconds
95.49% <= 5 milliseconds
98.48% <= 6 milliseconds
99.31% <= 7 milliseconds
99.60% <= 8 milliseconds
99.64% <= 9 milliseconds
99.65% <= 10 milliseconds
100.00% <= 11 milliseconds
15552.10 requests per second
```

#### value=100

```bash
redis-benchmark -h 127.0.0.1 -p 55000 -t set,get -d 100 -n 10000 -c 50

====== SET ======
  10000 requests completed in 0.67 seconds
  50 parallel clients
  100 bytes payload
  keep alive: 1

0.16% <= 1 milliseconds
18.29% <= 2 milliseconds
55.63% <= 3 milliseconds
78.35% <= 4 milliseconds
90.37% <= 5 milliseconds
95.71% <= 6 milliseconds
97.85% <= 7 milliseconds
99.03% <= 8 milliseconds
99.51% <= 9 milliseconds
99.82% <= 10 milliseconds
99.86% <= 11 milliseconds
99.93% <= 12 milliseconds
100.00% <= 12 milliseconds
14858.84 requests per second

====== GET ======
  10000 requests completed in 0.61 seconds
  50 parallel clients
  100 bytes payload
  keep alive: 1

0.33% <= 1 milliseconds
22.77% <= 2 milliseconds
66.01% <= 3 milliseconds
87.71% <= 4 milliseconds
96.19% <= 5 milliseconds
99.03% <= 6 milliseconds
99.52% <= 7 milliseconds
99.56% <= 8 milliseconds
99.62% <= 9 milliseconds
99.77% <= 10 milliseconds
99.98% <= 11 milliseconds
100.00% <= 11 milliseconds
16474.46 requests per second
```

#### value=200

```bash
redis-benchmark -h 127.0.0.1 -p 55000 -t set,get -d 200 -n 10000 -c 50

====== SET ======
  10000 requests completed in 0.78 seconds
  50 parallel clients
  200 bytes payload
  keep alive: 1

0.17% <= 1 milliseconds
11.26% <= 2 milliseconds
44.46% <= 3 milliseconds
69.63% <= 4 milliseconds
83.89% <= 5 milliseconds
90.80% <= 6 milliseconds
93.72% <= 7 milliseconds
96.27% <= 8 milliseconds
97.73% <= 9 milliseconds
98.75% <= 10 milliseconds
99.28% <= 11 milliseconds
99.54% <= 12 milliseconds
99.81% <= 13 milliseconds
99.99% <= 14 milliseconds
100.00% <= 14 milliseconds
12886.60 requests per second

====== GET ======
  10000 requests completed in 0.81 seconds
  50 parallel clients
  200 bytes payload
  keep alive: 1

0.19% <= 1 milliseconds
10.30% <= 2 milliseconds
39.92% <= 3 milliseconds
64.85% <= 4 milliseconds
81.34% <= 5 milliseconds
90.19% <= 6 milliseconds
95.28% <= 7 milliseconds
97.24% <= 8 milliseconds
97.85% <= 9 milliseconds
98.42% <= 10 milliseconds
99.02% <= 11 milliseconds
99.25% <= 12 milliseconds
99.38% <= 13 milliseconds
99.40% <= 14 milliseconds
99.44% <= 15 milliseconds
99.55% <= 16 milliseconds
99.68% <= 17 milliseconds
99.77% <= 18 milliseconds
99.84% <= 20 milliseconds
99.92% <= 21 milliseconds
99.95% <= 22 milliseconds
99.96% <= 23 milliseconds
99.97% <= 26 milliseconds
100.00% <= 27 milliseconds
12269.94 requests per second
```

#### value=1000

```bash
redis-benchmark -h 127.0.0.1 -p 55000 -t set,get -d 1000 -n 10000 -c 50

====== SET ======
  10000 requests completed in 0.85 seconds
  50 parallel clients
  1000 bytes payload
  keep alive: 1

0.07% <= 1 milliseconds
6.40% <= 2 milliseconds
31.74% <= 3 milliseconds
56.75% <= 4 milliseconds
75.29% <= 5 milliseconds
86.19% <= 6 milliseconds
93.39% <= 7 milliseconds
96.60% <= 8 milliseconds
98.37% <= 9 milliseconds
99.27% <= 10 milliseconds
99.65% <= 11 milliseconds
99.87% <= 12 milliseconds
99.98% <= 13 milliseconds
100.00% <= 14 milliseconds
11778.56 requests per second

====== GET ======
  10000 requests completed in 0.63 seconds
  50 parallel clients
  1000 bytes payload
  keep alive: 1

0.28% <= 1 milliseconds
19.58% <= 2 milliseconds
61.50% <= 3 milliseconds
85.38% <= 4 milliseconds
93.85% <= 5 milliseconds
97.65% <= 6 milliseconds
98.30% <= 7 milliseconds
99.06% <= 8 milliseconds
99.32% <= 9 milliseconds
99.47% <= 10 milliseconds
99.61% <= 11 milliseconds
99.81% <= 12 milliseconds
99.83% <= 13 milliseconds
99.87% <= 14 milliseconds
99.91% <= 15 milliseconds
100.00% <= 15 milliseconds
15797.79 requests per second
```

#### value=5000

```bash
redis-benchmark -h 127.0.0.1 -p 55000 -t set,get -d 5000 -n 10000 -c 50

====== SET ======
  10000 requests completed in 1.17 seconds
  50 parallel clients
  5000 bytes payload
  keep alive: 1

0.01% <= 1 milliseconds
1.00% <= 2 milliseconds
6.17% <= 3 milliseconds
20.03% <= 4 milliseconds
43.37% <= 5 milliseconds
64.50% <= 6 milliseconds
80.58% <= 7 milliseconds
89.93% <= 8 milliseconds
95.13% <= 9 milliseconds
97.18% <= 10 milliseconds
98.68% <= 11 milliseconds
99.10% <= 12 milliseconds
99.33% <= 13 milliseconds
99.43% <= 14 milliseconds
99.49% <= 15 milliseconds
99.51% <= 34 milliseconds
99.53% <= 35 milliseconds
99.62% <= 36 milliseconds
99.71% <= 37 milliseconds
99.74% <= 39 milliseconds
99.79% <= 40 milliseconds
99.93% <= 41 milliseconds
100.00% <= 41 milliseconds
8576.33 requests per second

====== GET ======
  10000 requests completed in 0.67 seconds
  50 parallel clients
  5000 bytes payload
  keep alive: 1

0.32% <= 1 milliseconds
18.53% <= 2 milliseconds
57.38% <= 3 milliseconds
82.02% <= 4 milliseconds
93.12% <= 5 milliseconds
97.02% <= 6 milliseconds
98.58% <= 7 milliseconds
99.17% <= 8 milliseconds
99.39% <= 9 milliseconds
99.50% <= 11 milliseconds
99.51% <= 13 milliseconds
99.53% <= 14 milliseconds
99.65% <= 15 milliseconds
99.85% <= 16 milliseconds
100.00% <= 16 milliseconds
14903.13 requests per second
```

#### 结果

多次测试下来，redis 的 set 能力随着 value 大小的增加会有一定量的减小，而 get 能力相对比较稳定

### 第二题

1. 批量写入使用 python 脚本生成协议数据

    ```python
    import argparse


    def set_value(index, length):
        value = str('a'*length)
        key_length = 3 + len(str(index))
        keyname = "key{}".format(str(index))
        proto = "*3\r\n$3\r\nSET\r\n${}\r\n{}\r\n${}\r\n{}\r\n".format(key_length, keyname, length, value)
        print(proto)


    parser = argparse.ArgumentParser()
    # 必选参数
    parser.add_argument('-l', '--length', dest='length', required=True, type=int, help='value length')
    parser.add_argument('-c', '--count', dest='count', required=True, type=int, help='value count')

    # 提取命令参数
    args = parser.parse_args()
    # string
    length = args.length
    count = args.count

    for i in range(0, count):
        set_value(i, length)
    ```

2. 使用 redis-cli --pipe 写入

    ```bash
    python3 redis_add_value.py -l 10 -c 10000 | redis-cli -h localhost -p 55000 -a redispw --pipe
    ```

3. 结果分析

    1. 写入数据前的内存占用 used_memory_dataset = 337328, 平均一条是 33.73

        ```bash
        redis-cli -h localhost -p 55001 -a redispw info memory
        # Memory
        used_memory:1769328
        used_memory_human:1.69M
        used_memory_rss:9474048
        used_memory_rss_human:9.04M
        used_memory_peak:1769328
        used_memory_peak_human:1.69M
        used_memory_peak_perc:100.01%
        used_memory_overhead:1432000
        used_memory_startup:863040
        used_memory_dataset:337328
        used_memory_dataset_perc:37.22%
        allocator_allocated:1744272
        allocator_active:2011136
        allocator_resident:4882432
        total_system_memory:8242126848
        total_system_memory_human:7.68G
        used_memory_lua:31744
        used_memory_vm_eval:31744
        used_memory_lua_human:31.00K
        used_memory_scripts_eval:0
        number_of_cached_scripts:0
        number_of_functions:0
        number_of_libraries:0
        used_memory_vm_functions:32768
        used_memory_vm_total:64512
        used_memory_vm_total_human:63.00K
        used_memory_functions:184
        used_memory_scripts:184
        used_memory_scripts_human:184B
        maxmemory:0
        maxmemory_human:0B
        maxmemory_policy:noeviction
        allocator_frag_ratio:1.15
        allocator_frag_bytes:266864
        allocator_rss_ratio:2.43
        allocator_rss_bytes:2871296
        rss_overhead_ratio:1.94
        rss_overhead_bytes:4591616
        mem_fragmentation_ratio:5.55
        mem_fragmentation_bytes:7767696
        mem_not_counted_for_evict:0
        mem_replication_backlog:0
        mem_total_replication_buffers:0
        mem_clients_slaves:0
        mem_clients_normal:37632
        mem_cluster_links:0
        mem_aof_buffer:0
        mem_allocator:jemalloc-5.2.1
        active_defrag_running:0
        lazyfree_pending_objects:0
        lazyfreed_objects:0
        ```

    2. 写入 1w 条 10 字节数据内存占用 used_memory_dataset = 411392， 平均一条是 41.14

        ```bash
        redis-cli -h localhost -p 55001 -a redispw info memory

        # Memory

        used_memory:1843392
        used_memory_human:1.76M
        used_memory_rss:9936896
        used_memory_rss_human:9.48M
        used_memory_peak:1843392
        used_memory_peak_human:1.76M
        used_memory_peak_perc:100.01%
        used_memory_overhead:1432000
        used_memory_startup:863040
        used_memory_dataset:411392
        used_memory_dataset_perc:41.96%
        allocator_allocated:1883280
        allocator_active:2179072
        allocator_resident:7208960
        total_system_memory:8242126848
        total_system_memory_human:7.68G
        used_memory_lua:31744
        used_memory_vm_eval:31744
        used_memory_lua_human:31.00K
        used_memory_scripts_eval:0
        number_of_cached_scripts:0
        number_of_functions:0
        number_of_libraries:0
        used_memory_vm_functions:32768
        used_memory_vm_total:64512
        used_memory_vm_total_human:63.00K
        used_memory_functions:184
        used_memory_scripts:184
        used_memory_scripts_human:184B
        maxmemory:0
        maxmemory_human:0B
        maxmemory_policy:noeviction
        allocator_frag_ratio:1.16
        allocator_frag_bytes:295792
        allocator_rss_ratio:3.31
        allocator_rss_bytes:5029888
        rss_overhead_ratio:1.38
        rss_overhead_bytes:2727936
        mem_fragmentation_ratio:5.50
        mem_fragmentation_bytes:8131776
        mem_not_counted_for_evict:0
        mem_replication_backlog:0
        mem_total_replication_buffers:0
        mem_clients_slaves:0
        mem_clients_normal:37632
        mem_cluster_links:0
        mem_aof_buffer:0
        mem_allocator:jemalloc-5.2.1
        active_defrag_running:0
        lazyfree_pending_objects:0
        lazyfreed_objects:0
        ```

    3. 写入 1w 条 20 字节数据内存占用:1.81M used_memory_dataset = 466704， 平均一条是 46.67

        ```bash
        redis-cli -h localhost -p 55002 -a redispw info memory

        # Memory

        used_memory:1898544
        used_memory_human:1.81M
        used_memory_rss:10158080
        used_memory_rss_human:9.69M
        used_memory_peak:1898544
        used_memory_peak_human:1.81M
        used_memory_peak_perc:100.01%
        used_memory_overhead:1431840
        used_memory_startup:862880
        used_memory_dataset:466704
        used_memory_dataset_perc:45.06%
        allocator_allocated:1938888
        allocator_active:2449408
        allocator_resident:5324800
        total_system_memory:8242126848
        total_system_memory_human:7.68G
        used_memory_lua:31744
        used_memory_vm_eval:31744
        used_memory_lua_human:31.00K
        used_memory_scripts_eval:0
        number_of_cached_scripts:0
        number_of_functions:0
        number_of_libraries:0
        used_memory_vm_functions:32768
        used_memory_vm_total:64512
        used_memory_vm_total_human:63.00K
        used_memory_functions:184
        used_memory_scripts:184
        used_memory_scripts_human:184B
        maxmemory:0
        maxmemory_human:0B
        maxmemory_policy:noeviction
        allocator_frag_ratio:1.26
        allocator_frag_bytes:510520
        allocator_rss_ratio:2.17
        allocator_rss_bytes:2875392
        rss_overhead_ratio:1.91
        rss_overhead_bytes:4833280
        mem_fragmentation_ratio:5.46
        mem_fragmentation_bytes:8297808
        mem_not_counted_for_evict:0
        mem_replication_backlog:0
        mem_total_replication_buffers:0
        mem_clients_slaves:0
        mem_clients_normal:37632
        mem_cluster_links:0
        mem_aof_buffer:0
        mem_allocator:jemalloc-5.2.1
        active_defrag_running:0
        lazyfree_pending_objects:0
        lazyfreed_objects:0
        ```

    4. 写入 1w 条 50 字节数据内存占用:2.12M used_memory_dataset = 786704 平均一条是 78.67

        ```bash
        redis-cli -h localhost -p 55003 -a redispw info memory

        # Memory

        used_memory:2218512
        used_memory_human:2.12M
        used_memory_rss:10412032
        used_memory_rss_human:9.93M
        used_memory_peak:2218512
        used_memory_peak_human:2.12M
        used_memory_peak_perc:100.00%
        used_memory_overhead:1431808
        used_memory_startup:862848
        used_memory_dataset:786704
        used_memory_dataset_perc:58.03%
        allocator_allocated:2257768
        allocator_active:2916352
        allocator_resident:5787648
        total_system_memory:8242126848
        total_system_memory_human:7.68G
        used_memory_lua:31744
        used_memory_vm_eval:31744
        used_memory_lua_human:31.00K
        used_memory_scripts_eval:0
        number_of_cached_scripts:0
        number_of_functions:0
        number_of_libraries:0
        used_memory_vm_functions:32768
        used_memory_vm_total:64512
        used_memory_vm_total_human:63.00K
        used_memory_functions:184
        used_memory_scripts:184
        used_memory_scripts_human:184B
        maxmemory:0
        maxmemory_human:0B
        maxmemory_policy:noeviction
        allocator_frag_ratio:1.29
        allocator_frag_bytes:658584
        allocator_rss_ratio:1.98
        allocator_rss_bytes:2871296
        rss_overhead_ratio:1.80
        rss_overhead_bytes:4624384
        mem_fragmentation_ratio:4.78
        mem_fragmentation_bytes:8231792
        mem_not_counted_for_evict:0
        mem_replication_backlog:0
        mem_total_replication_buffers:0
        mem_clients_slaves:0
        mem_clients_normal:37632
        mem_cluster_links:0
        mem_aof_buffer:0
        mem_allocator:jemalloc-5.2.1
        active_defrag_running:0
        lazyfree_pending_objects:0
        lazyfreed_objects:0
        ```

    5. 写入 1w 条 100 字节数据内存占用:2.65M used_memory_dataset = 1346704 平均一条是 134.67

        ```bash
        redis-cli -h localhost -p 55004 -a redispw info memory

        # Memory

        used_memory:2778448
        used_memory_human:2.65M
        used_memory_rss:11329536
        used_memory_rss_human:10.80M
        used_memory_peak:2778448
        used_memory_peak_human:2.65M
        used_memory_peak_perc:100.00%
        used_memory_overhead:1431744
        used_memory_startup:862784
        used_memory_dataset:1346704
        used_memory_dataset_perc:70.30%
        allocator_allocated:2820808
        allocator_active:3645440
        allocator_resident:6520832
        total_system_memory:8242126848
        total_system_memory_human:7.68G
        used_memory_lua:31744
        used_memory_vm_eval:31744
        used_memory_lua_human:31.00K
        used_memory_scripts_eval:0
        number_of_cached_scripts:0
        number_of_functions:0
        number_of_libraries:0
        used_memory_vm_functions:32768
        used_memory_vm_total:64512
        used_memory_vm_total_human:63.00K
        used_memory_functions:184
        used_memory_scripts:184
        used_memory_scripts_human:184B
        maxmemory:0
        maxmemory_human:0B
        maxmemory_policy:noeviction
        allocator_frag_ratio:1.29
        allocator_frag_bytes:824632
        allocator_rss_ratio:1.79
        allocator_rss_bytes:2875392
        rss_overhead_ratio:1.74
        rss_overhead_bytes:4808704
        mem_fragmentation_ratio:4.13
        mem_fragmentation_bytes:8589360
        mem_not_counted_for_evict:0
        mem_replication_backlog:0
        mem_total_replication_buffers:0
        mem_clients_slaves:0
        mem_clients_normal:37632
        mem_cluster_links:0
        mem_aof_buffer:0
        mem_allocator:jemalloc-5.2.1
        active_defrag_running:0
        lazyfree_pending_objects:0
        lazyfreed_objects:0
        ```

    6. 写入 1w 条 200 字节数据内存占用:3.72M used_memory_dataset = 2466704 平均一条是 246.67

        ```bash
        redis-cli -h localhost -p 55005 -a redispw info memory

        # Memory

        used_memory:3898576
        used_memory_human:3.72M
        used_memory_rss:12955648
        used_memory_rss_human:12.36M
        used_memory_peak:3898576
        used_memory_peak_human:3.72M
        used_memory_peak_perc:100.00%
        used_memory_overhead:1431872
        used_memory_startup:862912
        used_memory_dataset:2466704
        used_memory_dataset_perc:81.26%
        allocator_allocated:3968600
        allocator_active:5308416
        allocator_resident:8187904
        total_system_memory:8242126848
        total_system_memory_human:7.68G
        used_memory_lua:31744
        used_memory_vm_eval:31744
        used_memory_lua_human:31.00K
        used_memory_scripts_eval:0
        number_of_cached_scripts:0
        number_of_functions:0
        number_of_libraries:0
        used_memory_vm_functions:32768
        used_memory_vm_total:64512
        used_memory_vm_total_human:63.00K
        used_memory_functions:184
        used_memory_scripts:184
        used_memory_scripts_human:184B
        maxmemory:0
        maxmemory_human:0B
        maxmemory_policy:noeviction
        allocator_frag_ratio:1.34
        allocator_frag_bytes:1339816
        allocator_rss_ratio:1.54
        allocator_rss_bytes:2879488
        rss_overhead_ratio:1.58
        rss_overhead_bytes:4767744
        mem_fragmentation_ratio:3.36
        mem_fragmentation_bytes:9095344
        mem_not_counted_for_evict:0
        mem_replication_backlog:0
        mem_total_replication_buffers:0
        mem_clients_slaves:0
        mem_clients_normal:37632
        mem_cluster_links:0
        mem_aof_buffer:0
        mem_allocator:jemalloc-5.2.1
        active_defrag_running:0
        lazyfree_pending_objects:0
        lazyfreed_objects:0
        ```

    7. 写入 1w 条 1000 字节数据内存占用:11.35M used_memory_dataset = 10466704 平均一条是 1046.67

        ```bash
        redis-cli -h localhost -p 55006 -a redispw info memory

        # Memory

        used_memory:11898544
        used_memory_human:11.35M
        used_memory_rss:22560768
        used_memory_rss_human:21.52M
        used_memory_peak:11898544
        used_memory_peak_human:11.35M
        used_memory_peak_perc:100.00%
        used_memory_overhead:1431840
        used_memory_startup:862880
        used_memory_dataset:10466704
        used_memory_dataset_perc:94.84%
        allocator_allocated:11949032
        allocator_active:14131200
        allocator_resident:17420288
        total_system_memory:8242126848
        total_system_memory_human:7.68G
        used_memory_lua:31744
        used_memory_vm_eval:31744
        used_memory_lua_human:31.00K
        used_memory_scripts_eval:0
        number_of_cached_scripts:0
        number_of_functions:0
        number_of_libraries:0
        used_memory_vm_functions:32768
        used_memory_vm_total:64512
        used_memory_vm_total_human:63.00K
        used_memory_functions:184
        used_memory_scripts:184
        used_memory_scripts_human:184B
        maxmemory:0
        maxmemory_human:0B
        maxmemory_policy:noeviction
        allocator_frag_ratio:1.18
        allocator_frag_bytes:2182168
        allocator_rss_ratio:1.23
        allocator_rss_bytes:3289088
        rss_overhead_ratio:1.30
        rss_overhead_bytes:5140480
        mem_fragmentation_ratio:1.90
        mem_fragmentation_bytes:10700496
        mem_not_counted_for_evict:0
        mem_replication_backlog:0
        mem_total_replication_buffers:0
        mem_clients_slaves:0
        mem_clients_normal:37632
        mem_cluster_links:0
        mem_aof_buffer:0
        mem_allocator:jemalloc-5.2.1
        active_defrag_running:0
        lazyfree_pending_objects:0
        lazyfreed_objects:0
        ```

    8. 写入 1w 条 5000 字节数据内存占用:50.41M used_memory_dataset = 51426704 平均一条是 5142.67

        ```bash
        redis-cli -h localhost -p 55007 -a redispw info memory

        # Memory

        used_memory:52858576
        used_memory_human:50.41M
        used_memory_rss:64802816
        used_memory_rss_human:61.80M
        used_memory_peak:52871792
        used_memory_peak_human:50.42M
        used_memory_peak_perc:99.98%
        used_memory_overhead:1431872
        used_memory_startup:862912
        used_memory_dataset:51426704
        used_memory_dataset_perc:98.91%
        allocator_allocated:52875368
        allocator_active:53219328
        allocator_resident:59781120
        total_system_memory:8242126848
        total_system_memory_human:7.68G
        used_memory_lua:31744
        used_memory_vm_eval:31744
        used_memory_lua_human:31.00K
        used_memory_scripts_eval:0
        number_of_cached_scripts:0
        number_of_functions:0
        number_of_libraries:0
        used_memory_vm_functions:32768
        used_memory_vm_total:64512
        used_memory_vm_total_human:63.00K
        used_memory_functions:184
        used_memory_scripts:184
        used_memory_scripts_human:184B
        maxmemory:0
        maxmemory_human:0B
        maxmemory_policy:noeviction
        allocator_frag_ratio:1.01
        allocator_frag_bytes:343960
        allocator_rss_ratio:1.12
        allocator_rss_bytes:6561792
        rss_overhead_ratio:1.08
        rss_overhead_bytes:5021696
        mem_fragmentation_ratio:1.23
        mem_fragmentation_bytes:11982512
        mem_not_counted_for_evict:0
        mem_replication_backlog:0
        mem_total_replication_buffers:0
        mem_clients_slaves:0
        mem_clients_normal:37632
        mem_cluster_links:0
        mem_aof_buffer:0
        mem_allocator:jemalloc-5.2.1
        active_defrag_running:0
        lazyfree_pending_objects:0
        lazyfreed_objects:0
        ```

    9. 随着单条数据大小增大，冗余的内存占比会减小