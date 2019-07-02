import psutil
pids = psutil.pids()
for pid in pids:
        p = psutil.Process(pid)
        print('pid-%s,pname-%s' % (pid, p.name()))
        # if p.name() == 'dllhost.exe':
            # cmd = 'taskkill /F /IM dllhost.exe'
            # os.system(cmd)

print(psutil.cpu_count())
print(psutil.cpu_times())
