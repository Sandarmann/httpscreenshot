#!/usr/bin/env python
import os
import sys
import time
import subprocess

global _base_dir
global _logging_folder
global _listen_dir
global _httpscreenshot_file
_httpscreenshot_file = '/root/httpscreenshot/httpscreenshot.py'
_httpscreenshot_cluster_file = '/root/httpscreenshot/screenshotClustering/cluster.py'
_base_dir = '/root/httpscreenshot/'
_logging_folder = _base_dir + 'logs/'
_listen_dir = _logging_folder + 'inbound/'
for dir in [_base_dir,_logging_folder,_listen_dir]:
    if not os.path.exists(dir):
        os.makedirs(dir)



def run_screenshots(scan_url_list, scan_results_dir):
    cmd = "/usr/bin/python {} -l {} -p -t 30 -w 50 -a -vH -r 1".format(_httpscreenshot_file, scan_url_list)
    exit_code = subprocess.call(cmd, shell=True)
    sys.path.append(_logging_folder)
    group_cmd = '/usr/bin/python {} -d {}'.format(_httpscreenshot_cluster_file, scan_results_dir)
    exit_code = subprocess.call(group_cmd, shell=True)


def auto_run():
    scan_requests = os.listdir(_listen_dir)
    if scan_requests:
        for scan in scan_requests:
            print(scan)
            tmp_dir = _logging_folder + scan
            os.makedirs(tmp_dir)
            sys.path.append(tmp_dir)
            scan_url_list = _listen_dir + scan
            run_screenshots(scan_url_list, tmp_dir)
            os.remove(scan_url_list)

if __name__ == '__main__':
    while True:
        auto_run()
        time.sleep(30)
