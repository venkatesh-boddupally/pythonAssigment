# Write a function to parse a log file & extract details of Errors & Warnings recorded into a separate file.


def separate_error_and_warning_logs(log_file_path, destination_file_path):
    """
    :param log_file_path: source log file path
    :param destination_file_path: destination log file path
    :return:
    """
    with open(log_file_path, 'r') as f1, open(destination_file_path, 'a') as f2:
        f1_lines = f1.readlines()
        for line in f1_lines:
            if 'ERROR' in line or 'WARNING' in line:
                f2.write(line)
