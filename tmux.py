import sys
import subprocess

def is_tmux_running():
    try:
        subprocess.run(['tmux', 'list-sessions'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False


def update_tmux_status_line(line_number, content):
    command = ['tmux', 'set-option', f'status-format[{line_number}]', content]
    subprocess.run(command)


def set_rows(n):
    if n == 1:
        command = ['tmux', 'set-option', 'status', '2']
        subprocess.run(command)


if is_tmux_running() == True:
    if __name__ == "__main__":
        function_name = ""
        if len(sys.argv) > 1:
            function_name = sys.argv[1]

        if function_name == "update_tmux_status_line" and len(sys.argv) == 4:
            line_number = sys.argv[2]
            content = sys.argv[3]
            update_tmux_status_line(line_number, content)
        elif function_name == "set_rows" and len(sys.argv) == 3:
            n = sys.argv[2]
            set_rows(n)
