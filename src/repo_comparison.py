import os
import filecmp
import hashlib
from collections import defaultdict
from .comparator import Comparator, FileMeta, FileComparison, LineMeta
from .plot import plot_similarity_bar_chart


european_root = './resources/european'
asia_root = './resources/asia'
duplicated_report_file = './report/duplicated.md'
partially_duplicated_report_file = './report/partially_duplicated.md'
partially_duplicated_detailed_report_file = './report/partially_duplicated_detailed.md'
fully_unique_files = './report/unique.md'
similarity_bar_chart_picture_directory = './report'

similarity = 80
similarity_lower_bound = 10  # files that are < 10 similar are considered different

md_indent = '&nbsp;&nbsp;&nbsp;&nbsp;' \
            ''
def format_file_path(file_path):
    return f'[{file_path}](../{file_path})'


def write_report_full_duplicates(duplicated_files: list[FileComparison]):
    with open(duplicated_report_file, "w+") as f_dup:
        msg = f'Found {len(duplicated_files)} fully identical files\n\n'
        print(msg.replace('\n', ''))
        f_dup.write(msg)
        for file_comparison in duplicated_files:
            f_dup.write(f'Identical files found:\\\n')
            f_dup.write(f'\t{md_indent}{format_file_path(file_comparison.first_file_meta.file_path)}\\\n')
            #f_dup.write(f'\t{file_comparison.first_file_meta.file_path}\n')
            f_dup.write(f'\t{md_indent}{format_file_path(file_comparison.second_file_meta.file_path)}\n\n')


def write_report_partial_duplicates(partially_duplicated_files: list[FileComparison]):
    partially_duplicated_files = sorted(partially_duplicated_files, key=lambda fc: fc.uniqueness_score)

    msg = f'Found {len(partially_duplicated_files)} partially duplicated files:\n\n'
    print(msg.replace('\n', ''))

    def create_header(file_comparison: FileComparison):
        return f'Partially similar files found. First length {len(file_comparison.first_file_meta.line_metas)}, '\
               f'Second length {len(file_comparison.second_file_meta.line_metas)},  '\
               f'The files are {100 - file_comparison.uniqueness_score}% identical'\
               f'The files differ in {max(len(file_comparison.unique_in_first), len(file_comparison.unique_in_second))} lines:\\\n'

    def create_diff_line_with_line_nr(file_meta: LineMeta):
        return f'\t\t{md_indent*2}{file_meta.line_nr}\t| {file_meta.content}\\\n'


    with open(partially_duplicated_report_file, "w+") as f_part_dup:
        f_part_dup.write(msg)
        for file_comparison in partially_duplicated_files:
            f_part_dup.write(create_header(file_comparison))
            if file_comparison.first_file_meta.file_name != file_comparison.second_file_meta.file_name:
                f_part_dup.write('File names differ\\\n')
            f_part_dup.write(f'\t{md_indent}{format_file_path(file_comparison.first_file_meta.file_path)}\\\n')
            f_part_dup.write(f'\t{md_indent}{format_file_path(file_comparison.second_file_meta.file_path)} \n\n')

    with open(partially_duplicated_detailed_report_file, "w+") as f_part_dup_detailed:
        f_part_dup_detailed.write(msg)
        for file_comparison in partially_duplicated_files:
            f_part_dup_detailed.write(create_header(file_comparison))
            f_part_dup_detailed.write(f'\t{md_indent}{format_file_path(file_comparison.first_file_meta.file_path)}\\\n')
            f_part_dup_detailed.write(f'\t{md_indent}{format_file_path(file_comparison.second_file_meta.file_path)}\\\n')

            f_part_dup_detailed.write(f'\t{md_indent}Unique lines in first:\\\n')
            for first_line_meta in sorted(file_comparison.unique_in_first, key=lambda line_meta: line_meta.line_nr):
                f_part_dup_detailed.write(create_diff_line_with_line_nr(first_line_meta))
            f_part_dup_detailed.write(f'\t{md_indent}Unique lines in second:\\\n')
            for second_line_meta in sorted(file_comparison.unique_in_second, key=lambda line_meta: line_meta.line_nr):
                f_part_dup_detailed.write(create_diff_line_with_line_nr(second_line_meta))
            f_part_dup_detailed.write(f'\n\n')


def write_report_unique_files(fully_unique_first: list[FileMeta], fully_unique_second: list[FileMeta]):
    with open(fully_unique_files, 'w+') as f_unique:
        msg_1 = f'Found {len(fully_unique_first)} 100% unique files for the european repository\\\n'
        # msg_2 = f'Found {len(fully_unique_second)} 100% unique files for second'
        print(msg_1.replace('\n', ''))
        # print(msg_2.replace('\n', ''))
        f_unique.write(msg_1)
        # f_unique.write(msg_2)
        f_unique.write('<br/><br/><br/><br/>\n')
        for first_file_meta in fully_unique_first:
            f_unique.write(f'{md_indent}{len(first_file_meta.line_metas)} lines \t\t {format_file_path(first_file_meta.file_path)}\\\n')
        # f_unique.write('<br/><br/><br/><br/>\n')
        # for second_file_meta in fully_unique_second:
        #     f_unique.write(f'{md_indent}{len(second_file_meta.line_metas)} lines \t\t {format_file_path(second_file_meta.file_path)}\\\n')




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


   # v3 extremely inefficient, but very promising approach

    comparison_matrix: list[list[FileComparison]] = [
        [Comparator.compare_two_file_metas(first_file_meta, second_file_meta)
         for second_file_hash, second_file_meta in dict(second_file_hash_to_file_metas).items()]
        for first_file_hash, first_file_meta in dict(first_file_hash_to_file_metas).items()
    ]

    comp_matrix_last_size = None
    while comp_matrix_last_size != len(comparison_matrix):
        if len(comparison_matrix) == 0 or len(comparison_matrix[0]) == 0:
            break
        comp_matrix_last_size = len(comparison_matrix)
        for row in list(comparison_matrix):
            # find best for first
            best_for_first: FileComparison = row[0]
            best_j = 0
            for j, file_comparison in enumerate(row):
                if file_comparison.get_similarity() > best_for_first.get_similarity():
                    best_for_first = file_comparison
                    best_j = j

            # find best for second´
            best_for_second: FileComparison = comparison_matrix[0][best_j]
            best_i = 0
            for i in range(len(comparison_matrix)):
                file_comparison_2 = comparison_matrix[i][best_j]
                if file_comparison_2.get_similarity() > best_for_second.get_similarity():
                    best_for_second = file_comparison_2
                    best_i = i

            if best_for_second.first_file_meta is best_for_first.first_file_meta:
                # match found
                if best_for_first.get_similarity() == 100:
                    duplicated_files.append(best_for_first)
                elif best_for_first.get_similarity() > similarity_lower_bound:
                    partially_duplicated_files.append(best_for_first)
                else:
                    continue

                # delete row and column
                comparison_matrix.pop(best_i)
                for row in comparison_matrix:
                    row.pop(best_j)
                break


    for row in list(comparison_matrix):
        if row:
            fully_unique_first.append(row[0].first_file_meta)

    if comparison_matrix:
        for comp in comparison_matrix[0]:
            fully_unique_second.append(comp.second_file_meta)

    # v2
    # file to matches
    # first_comparison_dict: dict[str, list[FileComparison]] = defaultdict(list)
    # for first_file_hash, first_file_meta in first_file_hash_to_file_metas.items():
    #     for second_file_hash, second_file_meta in second_file_hash_to_file_metas.items():
    #         first_comparison_dict[first_file_hash].append(
    #             Comparator.compare_two_file_metas(first_file_meta, second_file_meta))
    # for k, v in first_comparison_dict.items():
    #     v.sort(key=lambda elem: elem.uniqueness_score)
    #
    # second_comparison_dict: dict[str, list[FileComparison]] = defaultdict(list)
    # for second_file_hash, second_file_meta in second_file_hash_to_file_metas.items():
    #     for first_file_hash, first_file_meta in first_file_hash_to_file_metas.items():
    #         second_comparison_dict[second_file_hash].append(
    #             Comparator.compare_two_file_metas(second_file_meta, first_file_meta))
    # for k, v in second_comparison_dict.items():
    #     v.sort(key=lambda elem: elem.uniqueness_score)
    #
    #
    # for first_file_hash, sorted_file_comparison_list in dict(first_comparison_dict).items():
    #     most_similar_comparison: FileComparison = sorted_file_comparison_list[-1]
    #     most_similar_for_first = most_similar_comparison.second_file_meta
    #
    #     most_similar_for_second = second_comparison_dict[most_similar_for_first.file_hash][-1].second_file_meta
    #
    #     if first_file_hash == most_similar_for_second.file_hash and most_similar_comparison.get_similarity() > similarity_lower_bound:
    #         # bidirectional match
    #         partially_duplicated_files.append(most_similar_comparison)
    #         del first_comparison_dict[first_file_hash]
    #         del second_comparison_dict[most_similar_for_first.file_hash]
    #
    # for first_file_hash, _ in dict(first_comparison_dict).items():
    #     fully_unique_first.append(first_file_hash_to_file_metas.get(first_file_hash))
    #
    # for second_file_hash, _ in dict(second_comparison_dict).items():
    #     fully_unique_second.append(second_file_hash_to_file_metas.get(second_file_hash))

    #v1


    # for first_file_hash, first_file_meta in dict(first_file_hash_to_file_metas).items():
    #     nearest_to_first: FileComparison = None
    #     for second_file_hash, second_file_meta in dict(second_file_hash_to_file_metas).items():
    #         file_comparison: FileComparison = Comparator.compare_two_file_metas(first_file_meta, second_file_meta)
    #         if not nearest_to_first:
    #             nearest_to_first = file_comparison
    #         elif nearest_to_first.uniqueness_score > file_comparison.uniqueness_score:
    #             nearest_to_first = file_comparison
    #
    #
    #      # bining of the results
    #
    #     if (100 - nearest_to_first.uniqueness_score) < similarity_lower_bound and nearest_to_first.first_file_meta.file_name != nearest_to_first.second_file_meta.file_name:
    #         # different files
    #         fully_unique_first.append(nearest_to_first.first_file_meta)
    #         fully_unique_second.append(nearest_to_first.second_file_meta)
    #         del first_file_hash_to_file_metas[nearest_to_first.first_file_meta.file_hash]
    #         del second_file_hash_to_file_metas[nearest_to_first.second_file_meta.file_hash]
    #
    #     elif nearest_to_first.uniqueness_score == 0:
    #         duplicated_files.append(nearest_to_first)
    #         del first_file_hash_to_file_metas[nearest_to_first.first_file_meta.file_hash]
    #         del second_file_hash_to_file_metas[nearest_to_first.second_file_meta.file_hash]
    #
    #     elif nearest_to_first.uniqueness_score == 100:
    #         fully_unique_first.append(first_file_meta)
    #
    #     else:
    #         # partially overlapping
    #         partially_duplicated_files.append(nearest_to_first)
    #
    # fully_unique_second.extend(second_file_hash_to_file_metas.values())


    # write files

    write_report_full_duplicates(duplicated_files)
    write_report_partial_duplicates(partially_duplicated_files)
    write_report_unique_files(fully_unique_first, fully_unique_second)


    # Crate plots
    all_dups = duplicated_files + partially_duplicated_files

    numbers = [file_comparison.get_similarity() for file_comparison in all_dups] + [0] * len(fully_unique_first)
    plot_similarity_bar_chart(numbers, 'All files', save_to_file_path=f'{similarity_bar_chart_picture_directory}/all_files.png')

    numbers2 = [file_comparison.get_similarity() for file_comparison in partially_duplicated_files] + [0] * len(fully_unique_first)
    plot_similarity_bar_chart(numbers2, 'Full duplicates excluded', save_to_file_path=f'{similarity_bar_chart_picture_directory}/full_matches_excluded.png')

    # duplicated_lines_of_code = 0
    # unique_lines_of_code = 0
    # for d in all_dups:
    #     duplicated_lines_of_code += len(d.duplicate_lines)
    #     unique_lines_of_code += len(d.unique_in_first)
    # unique_lines_of_code += len(fully_unique_first)
    #
    # print(f'Duplicated lines of code {duplicated_lines_of_code}, unique lines of code {unique_lines_of_code}')
    threshold = 50
    length_of_all_comparisons = len(all_dups) + len(fully_unique_first) + len(fully_unique_second)
    length_of_over_threshold = len(list(filter(lambda x: x.get_similarity() > threshold, all_dups)))
    print(f'{len(duplicated_files) * 1.0 / length_of_all_comparisons * 100}% are completely identical')
    print(f'{length_of_over_threshold * 1.0 / length_of_all_comparisons * 100}% files have similarity above {threshold}%')



def run():
    traverse_directories(f'{european_root}', f'{asia_root}')
