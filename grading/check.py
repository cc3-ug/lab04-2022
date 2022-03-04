import utils
import subprocess
from random import randint

jupiterRoute = '/home/student/image/bin/jupiter'

# checks hanoi.s
def check_hanoi():
    try:
        # run tests
        grade = 0
        wrong = []
        # hanoi
        test1 = [jupiterRoute, './hanoi/hanoi.s']
        task = utils.execute(cmd=test1, timeout=5)
        if task.returncode != 0:
            return (0, utils.failed('runtime error'), task.stderr.decode().strip())
        output = task.stdout.decode().strip()
        if 'mueva el disco de la torre: 1 hacia la torre: 2\nmueva el disco de la torre: 1 hacia la torre: 3\nmueva el disco de la torre: 2 hacia la torre: 3\nmueva el disco de la torre: 1 hacia la torre: 2\nmueva el disco de la torre: 3 hacia la torre: 1\nmueva el disco de la torre: 3 hacia la torre: 2\nmueva el disco de la torre: 1 hacia la torre: 2' in output and 'Jupiter: exit(0)' in output:
            grade += 100
        else:
            wrong.append('hanoi failed')
        
        if wrong == 1:
            return (0, utils.failed('all answers are wrong... ¯\\_(⊙︿⊙)_/¯'), '')
        bad = ','.join(wrong)
        return (grade, utils.passed() if len(wrong) == 0 else utils.incomplete('hanoi error'), '')
    except subprocess.TimeoutExpired:
        return (0, utils.failed('TIMEOUT'), '')
    except Exception as e:
        print(e)
        return (0, utils.failed('memory limit exceeded'), '')

def lab4_riscv():
    not_found = utils.expected_files([
        './hanoi/hanoi.s'
    ])
    if len(not_found) == 0:
        hanoi_result = check_hanoi()
        
        table = []
        table.append(('Hanoi', *hanoi_result[0: 2]))

        errors = ''
        errors += utils.create_error('hanoi.s', hanoi_result[2])
        errors = errors.strip()
        grade = 0
        grade += hanoi_result[0]
        grade = round(grade)
        grade = min(grade, 100)
        report = utils.report(table)
        print(report)
        if errors != '':
            report += '\n\nMore Info:\n\n' + errors
        return utils.write_result(grade, report)
    else:
        utils.write_result(0, 'missing files: %s' % (','.join(not_found)))


if __name__ == '__main__':
    lab4_riscv()
    utils.fix_ownership()
