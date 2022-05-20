# -*- encoding: utf-8 -*-
"""
@File Name      :   auto_qsub.py    
@Create Time    :   2022/5/13 16:59
@Description    :   
@Version        :   
@License        :   MIT
@Author         :   diklios
@Contact Email  :   diklios5768@gmail.com
@Github         :   https://github.com/diklios5768
@Blog           :   
@Motto          :   All our science, measured against reality, is primitive and childlike - and yet it is the most precious thing we have.
"""
__auth__ = 'diklios'

import os

import click


@click.command()
@click.argument('input_dir_path', type=click.Path(exists=True))
@click.option('--prefix', type=str, default='qsub', help='prefix of qsub')
@click.option('--size', type=int, default=10, help='qsub size at one time')
def main(input_dir_path, prefix, size):
    if not input_dir_path or not os.path.exists(input_dir_path) or not os.path.isdir(input_dir_path):
        raise Exception('input_dir_path is not exists or not a directory')
    shell_file_names = [file_name for file_name in os.listdir(input_dir_path) if prefix not in file_name]
    groups = [shell_file_names[i:i + size] for i in range(0, len(shell_file_names), size)]
    for index, group in enumerate(groups):
        # 新建一个qsub文件夹
        with open(os.path.join(input_dir_path,'qsub', f'{prefix}-{size}-{index}.sh'), 'w') as f:
            f.writelines([f'qsub {file_path}\n' for file_path in group])


if __name__ == '__main__':
    main()