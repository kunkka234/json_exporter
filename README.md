example json 1:

{"votingEnabled":true,"watchingEnabled":true,"unassignedIssuesAllowed":true,"subTasksEnabled":true,"issueLinkingEnabled":true,"timeTrackingEnabled":true,"attachmentsEnabled":true,"timeTrackingConfiguration":{"workingHoursPerDay":8.0,"workingDaysPerWeek":5.0,"timeFormat":"pretty","defaultUnit":"minute"}}

example json 2:

{"id":5373954,"key":"TEST","name":"Project: test","type":"global","status":"current","_expandable":{"settings":"/rest/api/space/TEST/settings","metadata":"","operations":"","lookAndFeel":"/rest/api/settings/lookandfeel?spaceKey=TEST","identifiers":"","permissions":"","icon":"","description":"","theme":"/rest/api/space/TEST/theme","history":"","homepage":"/rest/api/content/5374011"},"_links":{"context":"/wiki","self":"https://xxxxxx.atlassian.net/wiki/rest/api/space/TEST","collection":"/rest/api/space","webui":"/spaces/TEST","base":"https://xxxxxx.atlassian.net/wiki"}}


result

```
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 236.0
python_gc_objects_collected_total{generation="1"} 140.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable object found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 64.0
python_gc_collections_total{generation="1"} 5.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="8",patchlevel="8",version="3.8.8"} 1.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 9.3194805248e+010
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 2.5759744e+07
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.61634773694e+09
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 0.32
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 8.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1024.0
# HELP json_exporter monitoring
# TYPE json_exporter gauge
json_exporter{label="jira test label 1"} 1.0
json_exporter{label="jira test label 2"} 1.0
json_exporter{label="jira test label 2"} 1.0
json_exporter{label="jira test label 2"} 8.0
json_exporter{label="conf test label"} 1.0
```
