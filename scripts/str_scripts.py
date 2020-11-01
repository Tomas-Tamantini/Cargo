def list_to_str(header, full_list, str_fun=str, separator='\n\t'):
    first_sep = '\n\t' if separator == '\n\t' else ' '
    return header + first_sep + separator.join(map(str_fun, full_list))
