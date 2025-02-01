import subprocess
import os.path
import sys

if __name__ == '__main__':
	print (sys.argv[1:])
	for i in range(1,26):
		file=f'day{i}.py'
		if(os.path.isfile(file)):
			procArgs = ["python", file]+sys.argv[1:]
			proc=subprocess.run(procArgs, capture_output=True, encoding='UTF-8')
			if(proc.stderr): print(f'Day{i}:{proc.stderr}')
			print(proc.stdout,end='')
