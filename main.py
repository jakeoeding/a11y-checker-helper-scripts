from sys import argv, exit
import subprocess

def propagate_changes(a11y_checker_dir):
    print('Building a11y checker')
    subprocess.run(
        ['yarn', 'build'],
        cwd=a11y_checker_dir,
        capture_output=True
    )

    print('Copying build output to web container')
    subprocess.run([
        'docker',
        'cp',
        a11y_checker_dir + '/lib',
        'canvas-lms-web-1:/usr/src/app/node_modules/tinymce-a11y-checker/'
    ])

    print('Restarting webpack container')
    subprocess.run(['docker', 'restart', 'canvas-lms-webpack-1'])

    print('Done')


if __name__ == '__main__':
    if len(argv) < 2:
        print('Must include the absolute path of your tinymce-a11y-checker repo.')
        exit(1)
    propagate_changes(argv[1])
