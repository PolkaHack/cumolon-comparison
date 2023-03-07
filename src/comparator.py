import os
import filecmp
import hashlib
from pathlib import Path
import typing as t
from collections import defaultdict


class LineMeta:
    def __init__(self, file_path: str, line_nr: int, content: str, content_hash: str):
        self.file_path = file_path
        self.line_nr = line_nr
        self.content = content
        self.content_hash = content_hash


class FileMeta:
    def __init__(self, file_path: str, file_hash: str, line_metas: list[LineMeta]):
        self.file_path = file_path
        self.file_name = Path(file_path).name
        self.file_hash = file_hash
        self.line_metas = line_metas
        self.hash_multi_map = self.create_hash_multi_map(line_metas)

    @staticmethod
    def create_hash_multi_map(line_hashes):
        hash_multi_map = defaultdict(list)
        for line_hash in line_hashes:
            hash_multi_map[line_hash.content_hash].append(line_hash)
        return hash_multi_map

    def get_lines_hashes_set(self):
        return set(self.hash_multi_map.keys())

    def is_picture(self):
        return self.file_name.endswith('.png') or self.file_name.endswith('.ico')

    def __repr__(self):
        return f"{self.__class__.__name__}( {self.file_hash}, {len(self.line_metas)} lines, \t{self.file_path} )"


class FileComparison:
    def __init__(self, first_meta: FileMeta, second_meta: FileMeta, uniqueness_score):
        self.first_file_meta = first_meta
        self.second_file_meta = second_meta
        self.uniqueness_score = uniqueness_score  # in percent

        self.duplicate_lines: list[LineMeta] = []
        self.unique_in_first: list[LineMeta] = []
        self.unique_in_second: list[LineMeta] = []

    def __repr__(self):
        return f"{self.__class__.__name__}( {self.uniqueness_score}%, {self.first_file_meta.file_path} <> {self.second_file_meta.file_path} )"


class Comparator:

    @staticmethod
    def calculate_hash_from_path(file_path):
        """
        Calculate the SHA-256 hash of a file.
        """
        with open(file_path, 'rb') as file:
            return Comparator.calculate_hash_from_file(file)

    @staticmethod
    def calculate_hash_from_file(file):
        """
        Calculate the SHA-256 hash of a file.
        """
        hasher = hashlib.sha256()
        buffer = file.read(65536)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = file.read(65536)
        return hasher.hexdigest()

    @staticmethod
    def calculate_hash_from_string(line: str):
        """
        Calculate the SHA-256 hash of a file.
        """
        hasher = hashlib.sha256()
        hasher.update(line.encode('utf-8'))
        return hasher.hexdigest()

    @staticmethod
    def get_line_metas_for_file(file_path) -> list[LineMeta]:
        meta = list()

        # TODO deal with pictures
        if '.png' in file_path or '.ico' in file_path:
            return list()

        with open(file_path, 'r') as file:
            for line_nr, line in enumerate(file.readlines()):
                # todo empty lines and comments
                purified = line.strip()
                if purified:
                    line = purified
                    meta.append(LineMeta(file_path, line_nr, line, Comparator.calculate_hash_from_string(line)))

        return meta

    @staticmethod
    def get_file_meta(file_path) -> FileMeta:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} does not exist")
        return FileMeta(file_path, Comparator.calculate_hash_from_path(file_path), Comparator.get_line_metas_for_file(file_path))

    @staticmethod
    def create_file_metas_for_folder(folder_path) -> list[FileMeta]:
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"Path {folder_path} does not exist")
        if not os.path.isdir(folder_path):
            raise NotADirectoryError(f"Path {folder_path} is not a directory")
        file_metas = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_metas.append(Comparator.get_file_meta(file_path))
        return file_metas

    @staticmethod
    def compare_two_file_metas(first_file_meta: FileMeta, second_file_meta: FileMeta) -> FileComparison:
        # if not os.path.exists(first_path):
        #     print(f"File {first_path} does not exist")
        #     return
        # if not os.path.exists(second_path):
        #     print(f"File {second_path} does not exist")
        #     return
        #
        # first_file_meta = Comparator.get_file_meta(first_path)
        # second_file_meta = Comparator.get_file_meta(second_path)


        if first_file_meta.is_picture() and second_file_meta.is_picture():
            if first_file_meta.file_name == second_file_meta.file_name:
            # TODO make an actual picture comparison
            # Right now picture are compared only by file name
                return FileComparison(first_file_meta, second_file_meta, 0)

        if first_file_meta.file_hash == second_file_meta.file_hash:
            return FileComparison(first_file_meta, second_file_meta, 0)

        first_hash_multi_map = dict(first_file_meta.hash_multi_map)
        second_hash_multi_map = dict(second_file_meta.hash_multi_map)

        duplicate_lines = []
        unique_in_first = []
        unique_in_second = []

        if first_file_meta.file_name == 'index.html' and second_file_meta.file_name == 'index.html':
            # TODO DELETE
            pass

        for line_hash, lines in dict(first_hash_multi_map).items():
            if line_hash in second_hash_multi_map:
                if len(lines) == len(second_hash_multi_map[line_hash]):
                    duplicate_lines.extend(lines)
                    first_hash_multi_map.pop(line_hash)
                    second_hash_multi_map.pop(line_hash)
                else:
                    while line_hash in second_hash_multi_map and line_hash in first_hash_multi_map and second_hash_multi_map[line_hash] and first_hash_multi_map[line_hash]:
                        f = first_hash_multi_map[line_hash].pop()
                        s = second_hash_multi_map[line_hash].pop()
                        if len(first_hash_multi_map[line_hash]) == 0:
                            first_hash_multi_map.pop(line_hash)
                            # del first_hash_multi_map[line_hash]
                        if len(second_hash_multi_map[line_hash]) == 0:
                            second_hash_multi_map.pop(line_hash)
                            # del second_hash_multi_map[line_hash]
                        duplicate_lines.append(f)
                    # min_count = min(len(lines), len(second_hash_multi_map[line_hash]))
                    # duplicate_lines.extend(lines[:min_count])
                    # second_hash_multi_map[line_hash] = second_hash_multi_map[line_hash][:-min_count]
                    # first_hash_multi_map[line_hash] = first_hash_multi_map[line_hash][:-min_count]
            else:
                unique_in_first.extend(lines)

        # for d_line in duplicate_lines:
        #     if d_line.content_hash in second_hash_multi_map:
        #         del second_hash_multi_map[d_line.content_hash]

        for line_hash, lines in second_hash_multi_map.items():
            unique_in_second.extend(lines)

        unique_in_first_count = len(unique_in_first)
        unique_in_second_count = len(unique_in_second)
        duplicate_lines_count = len(duplicate_lines)
        overall_lines = unique_in_first_count + unique_in_second_count + duplicate_lines_count

        if overall_lines > 0:
            uniqueness_score = round((unique_in_first_count + unique_in_second_count) / overall_lines * 100)
        else:
            uniqueness_score = 100
        file_comparison = FileComparison(first_file_meta, second_file_meta, uniqueness_score)
        file_comparison.duplicate_lines = duplicate_lines
        file_comparison.unique_in_first = unique_in_first
        file_comparison.unique_in_second = unique_in_second
        return file_comparison





