import os
import filecmp
import hashlib
from .comparator import Comparator, FileMeta, FileComparison
from .plot import plot_similarity_bar_chart


european_root = './resources/european'
asia_root = './resources/asia'
duplicated_report_file = './report/duplicated.txt'
partially_duplicated_report_file = './report/partially_duplicated.txt'
partially_duplicated_detailed_report_file = './report/partially_duplicated_detailed.txt'
low_tolerance_file = './report/low_tolerance.txt'
fully_unique_files = './report/unique.txt'
similarity_bar_chart_picture_directory = './report'

similarity = 80
similarity_lower_bound = 10 # files that are < 10 similar are considered different


def write_report_full_duplicates(duplicated_files: list[FileComparison]):
    with open(duplicated_report_file, "w+") as f_dup:
        msg = f'Found {len(duplicated_files)} fully identical files\n\n'
        print(msg.replace('\n', ''))
        f_dup.write(msg)
        for file_comparison in duplicated_files:
            f_dup.write(f'Identical files found:\n')
            f_dup.write(f'\t{file_comparison.first_file_meta.file_path}\n')
            f_dup.write(f'\t{file_comparison.second_file_meta.file_path}\n\n')


def write_report_partial_duplicates(partially_duplicated_files: list[FileComparison]):
    partially_duplicated_files = sorted(partially_duplicated_files, key=lambda fc: fc.uniqueness_score)

    msg = f'Found {len(partially_duplicated_files)} partially duplicated files:\n\n'
    print(msg.replace('\n', ''))

    with open(partially_duplicated_report_file, "w+") as f_part_dup:
        f_part_dup.write(msg)

        for file_comparison in partially_duplicated_files:
            f_part_dup.write(
                f'Partially similar files found. First length {len(file_comparison.first_file_meta.line_metas)}, '
                f'Second length {len(file_comparison.second_file_meta.line_metas)},  '
                f'The files are {100 - file_comparison.uniqueness_score}% identical'
                f'The files differ in {max(len(file_comparison.unique_in_first), len(file_comparison.unique_in_second))} lines:\n')
            if file_comparison.first_file_meta.file_name != file_comparison.second_file_meta.file_name:
                f_part_dup.write('File names differ\n')
            f_part_dup.write(f'\t{file_comparison.first_file_meta.file_path}\n')
            f_part_dup.write(f'\t{file_comparison.second_file_meta.file_path}\n\n')


    with open(partially_duplicated_detailed_report_file, "w+") as f_part_dup_detailed:
        f_part_dup_detailed.write(msg)

        for file_comparison in partially_duplicated_files:
            f_part_dup_detailed.write(
                f'Partially similar files found. First length {len(file_comparison.first_file_meta.line_metas)}, '
                f'Second length {len(file_comparison.second_file_meta.line_metas)},  '
                f'The files are {100 - file_comparison.uniqueness_score}% identical'
                f'The files differ in {max(len(file_comparison.unique_in_first), len(file_comparison.unique_in_second))} lines:\n')
            f_part_dup_detailed.write(f'\t{file_comparison.first_file_meta.file_path}\n')
            f_part_dup_detailed.write(f'\t{file_comparison.second_file_meta.file_path}\n')

            f_part_dup_detailed.write(f'\tUnique lines in first:\n')
            for first_line_meta in sorted(file_comparison.unique_in_first, key=lambda line_meta: line_meta.line_nr):
                f_part_dup_detailed.write(f'\t\t{first_line_meta.line_nr}\t| {first_line_meta.content}\n')
            f_part_dup_detailed.write(f'\n\tUnique lines in second:\n')
            for second_line_meta in sorted(file_comparison.unique_in_second, key=lambda line_meta: line_meta.line_nr):
                f_part_dup_detailed.write(f'\t\t{second_line_meta.line_nr}\t| {second_line_meta.content}\n')
            f_part_dup_detailed.write(f'\n\n')


def write_report_unique_files(fully_unique_first: list[FileMeta], fully_unique_second: list[FileMeta]):
    with open(fully_unique_files, 'w+') as f_unique:
        msg_1 = f'Found {len(fully_unique_first)} 100% unique files for first\n'
        msg_2 = f'Found {len(fully_unique_second)} 100% unique files for second\n\n'
        print(msg_1.replace('\n', ''))
        print(msg_2.replace('\n', ''))
        f_unique.write(msg_1)
        f_unique.write(msg_2)
        for first_file_meta in fully_unique_first:
            f_unique.write(f'\t{len(first_file_meta.line_metas)} lines \t\t {first_file_meta.file_path}\n')
        f_unique.write('\n\n')
        for second_file_meta in fully_unique_second:
            f_unique.write(f'\t{len(second_file_meta.line_metas)} lines \t\t {second_file_meta.file_path}\n')


def traverse_directories(first, second):
    first_file_metas_list = Comparator.create_file_metas_for_folder(first)
    second_file_metas_list = Comparator.create_file_metas_for_folder(second)
    print(f'{len(first_file_metas_list)} files found in {first}')
    print(f'{len(second_file_metas_list)} files found in {second}')

    first_file_hash_to_file_metas = {fm.file_hash: fm for fm in first_file_metas_list}
    second_file_hash_to_file_metas = {fm.file_hash: fm for fm in second_file_metas_list}

    duplicated_files: list[FileComparison] = list()
    partially_duplicated_files: list[FileComparison] = list()
    fully_unique_first: list[FileMeta] = list()
    fully_unique_second: list[FileMeta] = list()

    for file_hash, file_meta in dict(first_file_hash_to_file_metas).items():
        if file_hash in second_file_hash_to_file_metas:
            duplicated_files.append(Comparator.compare_two_file_metas(file_meta, second_file_hash_to_file_metas[file_hash]))
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


         # bining of the results

        if (100 - nearest_to_first.uniqueness_score) < similarity_lower_bound and nearest_to_first.first_file_meta.file_name != nearest_to_first.second_file_meta.file_name:
            # different files
            fully_unique_first.append(nearest_to_first.first_file_meta)
            fully_unique_second.append(nearest_to_first.second_file_meta)
            del first_file_hash_to_file_metas[nearest_to_first.first_file_meta.file_hash]
            del second_file_hash_to_file_metas[nearest_to_first.second_file_meta.file_hash]

        elif nearest_to_first.uniqueness_score == 0:
            duplicated_files.append(nearest_to_first)
            del first_file_hash_to_file_metas[nearest_to_first.first_file_meta.file_hash]
            del second_file_hash_to_file_metas[nearest_to_first.second_file_meta.file_hash]

        elif nearest_to_first.uniqueness_score == 100:
            fully_unique_first.append(first_file_meta)

        else:
            # partially overlapping
            partially_duplicated_files.append(nearest_to_first)

    fully_unique_second.extend(second_file_hash_to_file_metas.values())


    # write files

    write_report_full_duplicates(duplicated_files)
    write_report_partial_duplicates(partially_duplicated_files)
    write_report_unique_files(fully_unique_first, fully_unique_second)
    plot_similarity_bar_chart(duplicated_files + partially_duplicated_files, 'All files', save_to_file_path=f'{similarity_bar_chart_picture_directory}/all_files.png')
    plot_similarity_bar_chart(partially_duplicated_files, 'Full duplicates excluded', save_to_file_path=f'{similarity_bar_chart_picture_directory}/full_matches_excluded.png')



def run():
    traverse_directories(f'{european_root}', f'{asia_root}')
