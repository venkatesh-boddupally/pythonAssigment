# Write a function that provides a change directory (cd) function for an abstract file system.

# Notes:
# Root path is '/'.
# Path separator is '/'.
# Parent directory is addressable as '..'.
# Directory names consist only of English alphabet letters (A-Z and a-z).
# The function should support both relative and absolute paths.
# The function will not be passed any invalid paths.
# Do not use built-in path-related functions.


class Path(object):
    def __init__(self, file_path):
        self.__current_path = file_path

    @property
    def current_path(self):
        return self.__current_path

    def cd(self, new_path):
        i = 0
        new_path_list = new_path.split('/')
        path_length = len(new_path_list)
        path_list = self.current_path.split('/')
        if new_path_list[0] == '':
            path_list = list()
            path_list.append('/' + new_path_list[1])
            i = i + 2
        while i < path_length:
            j = len(path_list)-1
            if new_path_list[i] == '..':
                # moving back in current path
                path_list.pop(j)
            else:
                path_list.append(new_path_list[i])
            i = i+1
        self.__current_path = "/".join(path_list)


path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)
