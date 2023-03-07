import os
import filecmp
import hashlib
from .comparator import Comparator, FileMeta, FileComparison


european_root = './resources/european'
asia_root = './resources/asia'
duplicated_report_file = './report/duplicated.txt'
partially_duplicated_report_file = './report/partially_duplicated.txt'
low_tolerance_file = './report/low_tolerance.txt'
fully_unique_files = './report/fully_unique.txt'
similarity = 80
uniqueness_tolerance = 100 - similarity  # if file differ more than 20 % they are labeled as different


def traverse_directories(first, second):
    first_file_metas_list = Comparator.create_file_metas_for_folder(first)
    second_file_metas_list = Comparator.create_file_metas_for_folder(second)

    first_file_hash_to_file_metas = {fm.file_hash: fm for fm in first_file_metas_list}
    second_file_hash_to_file_metas = {fm.file_hash: fm for fm in second_file_metas_list}

    duplicated_files: list[tuple[FileMeta, FileMeta]] = list()
    partially_duplicated_files: list[FileComparison] = list()
    fully_unique_first: list[FileMeta] = list()
    fully_unique_second: list[FileMeta] = list()
    low_tolerance_intersections: list[FileComparison] = list()

    for file_hash, file_meta in dict(first_file_hash_to_file_metas).items():
        if file_hash in second_file_hash_to_file_metas:
            duplicated_files.append((file_meta, second_file_hash_to_file_metas[file_hash]))
            del first_file_hash_to_file_metas[file_hash]
            del second_file_hash_to_file_metas[file_hash]

    for first_file_hash, first_file_meta in dict(first_file_hash_to_file_metas).items():
        nearest_to_first: FileComparison = None
        for second_file_hash, second_file_meta in dict(second_file_hash_to_file_metas).items():
            file_comparison: FileComparison = Comparator.compare_two_file_metas(first_file_meta, second_file_meta)
            if not nearest_to_first:
                nearest_to_first = file_comparison
            elif nearest_to_first.uniqueness_score > file_comparison.uniqueness_score:
                nearest_to_first = file_comparison

        if nearest_to_first.uniqueness_score == 0:
            duplicated_files.append((nearest_to_first.first_file_meta, nearest_to_first.second_file_meta))
        elif nearest_to_first.uniqueness_score == 100:
            fully_unique_first.append(first_file_meta)
        elif nearest_to_first.uniqueness_score < uniqueness_tolerance:
            # code is not unique
            partially_duplicated_files.append(nearest_to_first)
            del first_file_hash_to_file_metas[nearest_to_first.first_file_meta.file_hash]
            del second_file_hash_to_file_metas[nearest_to_first.second_file_meta.file_hash]
        else:
            low_tolerance_intersections.append(nearest_to_first)

    fully_unique_second.extend(second_file_hash_to_file_metas.values())


    with open(duplicated_report_file, "w+") as f_dup:
        msg = f'Found {len(duplicated_files)} fully identical files\n\n'
        print(msg.replace('\n', ''))
        f_dup.write(msg)
        for first_file_meta, second_file_meta in duplicated_files:
            f_dup.write(f'Identical files found:\n')
            f_dup.write(f'\t{first_file_meta.file_path}\n')
            f_dup.write(f'\t{second_file_meta.file_path}\n')


    with open(partially_duplicated_report_file, "w+") as f_part_dup:
        msg = f'Found {len(partially_duplicated_files)} files with similarity > {100 - uniqueness_tolerance}%\n\n'
        print(msg.replace('\n', ''))
        f_part_dup.write(msg)

        for file_comparison in partially_duplicated_files:
            f_part_dup.write(f'Partially similar files found. First length {len(file_comparison.first_file_meta.line_metas)}, Second length {len(file_comparison.second_file_meta.line_metas)},  The files are {100 - file_comparison.uniqueness_score}% identical:\n')
            f_part_dup.write(f'\t{file_comparison.first_file_meta.file_path}\n')
            f_part_dup.write(f'\t{file_comparison.second_file_meta.file_path}\n')
            f_part_dup.write(f'\tUnique lines in first:\n')
            for first_line_meta in sorted(file_comparison.unique_in_first, key=lambda line_meta: line_meta.line_nr):
                f_part_dup.write(f'\t\t{first_line_meta.line_nr}\t| {first_line_meta.content}')
            f_part_dup.write(f'\n\tUnique lines in second:\n')
            for second_line_meta in sorted(file_comparison.unique_in_second, key=lambda line_meta: line_meta.line_nr):
                f_part_dup.write(f'\t\t{second_line_meta.line_nr}\t| {second_line_meta.content}')
            f_part_dup.write(f'\n\n')

    with open(low_tolerance_file, "w+") as f_low:
        msg = f'Found {len(low_tolerance_intersections)} that have similarities files with similarity < {100 - uniqueness_tolerance}%\n\n'
        print(msg.replace('\n', ''))
        f_low.write(msg)

        for file_comparison in low_tolerance_intersections:
            f_low.write(f'\nPartially similar files found. First length {len(file_comparison.first_file_meta.line_metas)}, Second length {len(file_comparison.second_file_meta.line_metas)},  The files are {100 - file_comparison.uniqueness_score}% identical:\n')
            f_low.write(f'\t{file_comparison.first_file_meta.file_path}\n')
            f_low.write(f'\t{file_comparison.second_file_meta.file_path}\n')
            if file_comparison.first_file_meta.file_name == file_comparison.second_file_meta.file_name:
                for first_line_meta in sorted(file_comparison.unique_in_first, key=lambda line_meta: line_meta.line_nr):
                    f_low.write(f'\t\t{first_line_meta.line_nr}\t| {first_line_meta.content}\n')
                f_low.write(f'\n\tUnique lines in second:\n')
                for second_line_meta in sorted(file_comparison.unique_in_second,
                                               key=lambda line_meta: line_meta.line_nr):
                    f_low.write(f'\t\t{second_line_meta.line_nr}\t| {second_line_meta.content}\n')
                f_low.write(f'\n\n')


    with open(fully_unique_files, 'w+') as f_unique:
        msg_1 = f'Found {len(fully_unique_first)} 100% unique files in {first}\n'
        msg_2 = f'Found {len(fully_unique_second)} 100% unique files in {second}\n\n'
        print(msg_1.replace('\n', ''))
        print(msg_2.replace('\n', ''))
        f_unique.write(msg_1)
        f_unique.write(msg_2)
        for first_file_meta in fully_unique_first:
            f_unique.write(f'\t{first_file_meta.file_path}\n')
        f_unique.write('\n\n')
        for second_file_meta in fully_unique_second:
            f_unique.write(f'\t{second_file_meta.file_path}\n')



def run():
    traverse_directories(f'{european_root}', f'{asia_root}')
